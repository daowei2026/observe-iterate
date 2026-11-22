__all__ = [
    "df_idx0",
    "np_array",
    "timesearch",
    "first_price",
    "match_price",
    "seek_lts_range",
    "size_scale_factor",
    "scale_size_by_factor",
    "scale_size",
    "union_uti_series",
    "identify_uti_segments",
    "identify_contiguous_segments",
]

import numpy as np
import pandas as pd
import numba as nb


def df_idx0(df):
    idx = df.index
    if isinstance(idx, pd.MultiIndex):
        return idx.get_level_values(0).values
    return idx.values


def np_array(a):
    if isinstance(a, (pd.Series, pd.Index)):
        return a.values
    # todo other cases?
    return a


@nb.njit(nogil=True)
def _timesearch(tsa, tsp):
    tpa = np.searchsorted(tsa, tsp)
    for i in range(1, len(tsp)):
        if tpa[i] < tsa.size and tsa[tpa[i]] != tsp[i]:
            tpa[i] = max(-1, tpa[i] - 1)
    return tpa


def timesearch(tsa, tsp):
    tsa1 = np_array(tsa)
    tsp1 = np_array(tsp)
    if tsp1.dtype.kind == "f" and tsa1.dtype.kind != "f":
        tsa1 = tsa1.view("i8").astype(tsp1.dtype)
    return _timesearch(tsa1, tsp1)


@nb.njit(nogil=True)
def _first_price(price):
    for p in price:
        if np.isfinite(p) and p > 0:
            return p
    return np.nan


def first_price(price):
    return _first_price(np_array(price))


@nb.njit(nogil=True)
def _match_price(tsa, price, tsp):
    assert tsa.ndim == price.ndim == tsp.ndim == 1
    assert tsa.shape == price.shape
    p = np.full_like(tsp, np.nan, dtype=price.dtype)
    for i, tsi in enumerate(np.searchsorted(tsa, tsp)):
        while True:
            if price[tsi] > 0:
                break
            tsi += 1
            if tsi >= tsa.size or tsa[tsi] > tsp[i]:
                break
        p[i] = price[tsi]
    return p


def match_price(df, tsp):
    return _match_price(df.index.values, df.price.values, tsp.values)


@nb.njit(nogil=True)
def _seek_lts_range(ltsa, start_lts, end_lts):
    """
    TODO improve performance with binary search, but tolerating NaNs possibly anywhere

    """
    assert ltsa.ndim == 1
    assert 0 <= start_lts < end_lts

    start_i = 0
    while start_i < ltsa.size:
        if ltsa[start_i] >= start_lts:  # this effectively skips NaNs
            break
        start_i += 1

    end_i, prev_i = ltsa.size, ltsa.size - 1
    while prev_i >= 0:
        if ltsa[prev_i] <= end_lts:  # this effectively skips NaNs
            break
        end_i, prev_i = prev_i, prev_i - 1

    return start_i, end_i


def seek_lts_range(ltsa, start_lts, end_lts):
    return slice(*_seek_lts_range(np_array(ltsa), float(start_lts), float(end_lts)))


def size_scale_factor(min_, max_, size_scale=100):
    if max_ == min_:
        return min_ - 1, size_scale  # scale all points to maximum size
    rng = max_ - min_
    return min_, size_scale / rng


def scale_size_by_factor(ds, size_base, scale_factor):
    base, factor = scale_factor
    if not np.isfinite(factor):
        return np.full_like(ds, size_base)
    scaled_size = size_base + factor * (ds - base)
    return np.where(np.isfinite(scaled_size), scaled_size, size_base)


def scale_size(ds, size_base=20, size_scale=100):
    return scale_size_by_factor(
        ds, size_base, size_scale_factor(ds.min(), ds.max(), size_scale)
    )


def union_uti_series(*uti_series):
    return np.unique(np.concatenate([np_array(s) for s in uti_series], dtype=np.intp))


@nb.njit(nogil=True)
def _identify_uti_segments(utis, n_inter, n_margin, n_max):
    assert n_inter > 0 and n_margin >= 0
    assert n_max > n_margin * 2
    assert utis.ndim == 1 and utis.size >= 1
    segs = np.empty((utis.size, 2), np.intp)
    segc = 0
    start_uti = utis[0]
    segs[segc, 0] = start_uti - n_margin
    for i in range(1, utis.size):
        if (utis[i] - start_uti > n_inter) or (
            utis[i - 1] + n_margin - segs[segc, 0] >= n_max
        ):
            segs[segc, 1] = utis[i - 1] + n_margin
            segc += 1
            start_uti = utis[i]
            segs[segc, 0] = start_uti - n_margin
    segs[segc, 1] = utis[-1] + n_margin
    segc += 1

    return segs[:segc].copy()


def identify_uti_segments(*uti_series, n_inter=7200 * 3, n_margin=600, n_max=7200 * 5):
    utis = union_uti_series(*uti_series)
    return _identify_uti_segments(utis, n_inter, n_margin, n_max)


def identify_contiguous_segments(
    *series_or_indices, n_inter_days=30, n_margin_days=10, n_max_days=60
):
    """
    Merge multiple sorted datetime Series or DatetimeIndex objects and identify contiguous segments,
    splitting long segments and extending each segment by a margin of days at both ends.

    Parameters:
        *series_or_indices (pd.Series or pd.DatetimeIndex): Variable number of pandas Series with dtype datetime64[ns]
            or pandas DatetimeIndex objects, sorted in ascending order.
        n_inter_days (int, optional): Maximum allowed gap in days between consecutive timepoints
                                      to consider as contiguous. Default is 30 days.
        n_margin_days (int, optional): Number of days to extend each segment at both start and end.
                                       Must be less than n_inter_days. Default is 10 days.
        n_max_days (int, optional): Maximum allowed duration in days for any segment.
                                     Segments longer than this will be split into smaller segments.
                                     Default is 60 days.

    Returns:
        List of tuples: Each tuple contains (start, end) timestamps of a contiguous segment,
                        extended by the specified margin days and split if necessary.

    Raises:
        AssertionError: If n_margin_days is not less than n_inter_days.
        TypeError: If any input is neither a pandas Series nor a DatetimeIndex.
    """
    if not series_or_indices:
        return []

    # Ensure n_margin_days is less than n_inter_days to prevent overlapping extensions
    assert n_margin_days < n_inter_days, (
        f"n_margin_days ({n_margin_days}) must be less than n_inter_days ({n_inter_days}) "
        "to prevent overlapping extended segments."
    )

    # Calculate half margins for start and end
    half_margin_start = n_margin_days // 2
    half_margin_end = n_margin_days - half_margin_start

    # Collect all datetime values
    all_datetimes = []
    for idx, input_data in enumerate(series_or_indices, start=1):
        if isinstance(input_data, pd.Series) or isinstance(
            input_data, pd.DatetimeIndex
        ):
            # Extract datetime values using .values and convert to pd.Timestamp
            datetimes = pd.to_datetime(input_data.values, errors="coerce")
            all_datetimes.append(pd.Series(datetimes))
        else:
            raise TypeError(
                f"Input {idx} is of type {type(input_data).__name__}, but only pandas Series and DatetimeIndex are supported."
            )

    # Merge, drop NaT and duplicates, sort
    merged = pd.concat(all_datetimes, ignore_index=True)
    merged = merged.dropna().drop_duplicates().sort_values().reset_index(drop=True)

    if merged.empty:
        return []

    # Identify contiguous segments
    diff = merged.diff()
    group = (diff > pd.Timedelta(days=n_inter_days)).cumsum()
    grouped = merged.groupby(group)
    segments = grouped.agg(["first", "last"]).reset_index(drop=True)

    # Split long segments
    final_segments = []
    for start, end in zip(segments["first"], segments["last"]):
        split_start = start
        while split_start <= end:
            split_end = split_start + pd.Timedelta(days=n_max_days)
            if split_end > end:
                split_end = end
            final_segments.append((split_start, split_end))
            split_start = split_end + pd.Timedelta(days=1)

    # Add margin after splitting with half margins to prevent doubling
    extended_segments = []
    for start, end in final_segments:
        extended_start = start - pd.Timedelta(days=half_margin_start)
        extended_end = end + pd.Timedelta(days=half_margin_end)

        # Set extended_start to midnight
        extended_start = extended_start.normalize()

        # Check if end is exactly at midnight
        if extended_end.normalize() == extended_end:
            # If already at midnight, do not extend further
            extended_end = extended_end
        else:
            # Extend to midnight of the next day
            extended_end = (extended_end + pd.Timedelta(days=1)).normalize()

        extended_segments.append((extended_start, extended_end))

    return extended_segments
