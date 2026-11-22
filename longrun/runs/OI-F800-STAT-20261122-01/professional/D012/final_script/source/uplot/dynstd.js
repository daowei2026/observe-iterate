function stdUpdPerXR() {
  const renderers = fig.renderers;
  function isFullyHidden(cds) {
    return renderers.filter(r => r.data_source === cds)
      .every(r => !r.visible);
  }

  const xr_start = fig.x_range.start;
  const xr_end = fig.x_range.end;

  let adj_min_y = undefined, adj_max_y = undefined;
  function upd_y_rng(y) {
    if (!isFinite(y)) return;
    if (adj_max_y === undefined || y > adj_max_y) adj_max_y = y;
    if (adj_min_y === undefined || y < adj_min_y) adj_min_y = y;
  }

  function std_ds_pair(cds, fn) {
    const prestd_fn = '__prestd_' + fn;
    const ds = cds.data[fn];
    if (!(prestd_fn in cds.data)) {
      // live ctrls may update the cds without putting a __prestd_ column into it
      cds.data[prestd_fn] = ds.slice();
    }
    return [cds.data[prestd_fn], ds];
  }

  for (const dynstd of dynstd_list) {
    // note: must process base_cds, even if it isFullyHidden()

    const base_x_ds = dynstd.base_cds.data[dynstd.base_x];
    if (!base_x_ds) {
      console.error(`[${x_field}] not in cds!`, dynstd.base_cds);
      continue;
    }
    const ds_len = base_x_ds.length;
    let start_i = 0;
    let end_i = ds_len;

    // Find start index
    for (let i = 0; i < ds_len; i++) {
      if (base_x_ds[i] >= xr_start) {
        start_i = i > 0 ? i - 1 : 0;
        break;
      }
    }

    // Find end index
    if (xr_end !== undefined) {
      for (let i = ds_len - 1; i >= 0; i--) {
        if (base_x_ds[i] < xr_end) {
          end_i = i + 1;
          break;
        }
      }
    }

    let bl = NaN;
    const [ds_prestd, ds] = std_ds_pair(dynstd.base_cds, dynstd.base_y);
    switch (dynstd.method) {
      case 'diff':
        for (let i = start_i; i < end_i; i++) {
          if (!isFinite(bl)) {
            const prestd = ds_prestd[i];
            if (isFinite(prestd)) bl = prestd;
          }
          upd_y_rng(
            ds[i] = ds_prestd[i] - bl
          );
        }
        break;
      case 'diff-back':
        for (let i = end_i - 1; i >= start_i; i--) {
          if (!isFinite(bl)) {
            const prestd = ds_prestd[i];
            if (isFinite(prestd)) bl = prestd;
          }
          upd_y_rng(
            ds[i] = ds_prestd[i] - bl
          );
        }
        break;
      case 'ratio':
        for (let i = start_i; i < end_i; i++) {
          if (!isFinite(bl)) {
            const prestd = ds_prestd[i];
            if (isFinite(prestd)) bl = prestd;
          }
          upd_y_rng(
            ds[i] = ds_prestd[i] / bl
          );
        }
        break;
      case 'ratio-back':
        for (let i = end_i - 1; i >= start_i; i--) {
          if (!isFinite(bl)) {
            const prestd = ds_prestd[i];
            if (isFinite(prestd)) bl = prestd;
          }
          upd_y_rng(
            ds[i] = ds_prestd[i] / bl
          );
        }
        break;
      default:
        console.error('Unsupported dynstd method: [' + dynstd.method + '] !!');
    }
    for (const y of dynstd.extra_ys) {
      const [ds_prestd, ds] = std_ds_pair(dynstd.base_cds, y);
      switch (dynstd.method) {
        case 'diff':
        case 'diff-back':
          for (let i = start_i; i < end_i; i++) {
            upd_y_rng(
              ds[i] = ds_prestd[i] - bl
            );
          }
          break;
        case 'ratio':
        case 'ratio-back':
          for (let i = start_i; i < end_i; i++) {
            upd_y_rng(
              ds[i] = ds_prestd[i] / bl
            );
          }
          break;
        default:
          console.error('Unsupported dynstd method: [' + dynstd.method + '] !!');
      }
    }
    dynstd.base_cds.change.emit();

    if (isFinite(bl)) {
      for (const [cds, xy_pairs] of dynstd.driven_list) {
        // ignore this CDS if all renderers referencing it are hidden
        if (isFullyHidden(cds)) continue;

        for (const [x, y] of xy_pairs) {
          const x_ds = cds.data[x];
          if (!x_ds) {
            console.error(`[${x}] not in cds!`, cds);
            continue;
          }
          const ds_len = x_ds.length;
          let start_i = 0;
          let end_i = ds_len;

          // Find start index
          for (let i = 0; i < ds_len; i++) {
            if (x_ds[i] >= xr_start) {
              start_i = i > 0 ? i - 1 : 0;
              break;
            }
          }

          // Find end index
          if (xr_end !== undefined) {
            for (let i = ds_len - 1; i >= 0; i--) {
              if (x_ds[i] < xr_end) {
                end_i = i + 1;
                break;
              }
            }
          }

          const [ds_prestd, ds] = std_ds_pair(cds, y);
          switch (dynstd.method) {
            case 'diff':
            case 'diff-back':
              for (let i = start_i; i < end_i; i++) {
                if (x_ds[i] < xr_start || x_ds[i] >= xr_end)
                  continue; // ignore such data points, they are here due to not monotonicly sorted
                upd_y_rng(
                  ds[i] = ds_prestd[i] - bl
                );
              }
              break;
            case 'ratio':
            case 'ratio-back':
              for (let i = start_i; i < end_i; i++) {
                if (x_ds[i] < xr_start || x_ds[i] >= xr_end)
                  continue; // ignore such data points, they are here due to not monotonicly sorted
                upd_y_rng(
                  ds[i] = ds_prestd[i] / bl
                );
              }
              break;
            default:
              console.error('Unsupported dynstd method: [' + dynstd.method + '] !!');
          }
        }
        cds.change.emit();
      }
    }
  }

  if (isFinite(adj_min_y) && isFinite(adj_max_y)) {
    setTimeout(() => { // y_range change may fail if set immediately here
      const adj_y = (adj_max_y - adj_min_y) * 0.1;
      fig.y_range.start = adj_min_y - adj_y;
      fig.y_range.end = adj_max_y + adj_y;

      console.log(`[${new Date().getTime()}] figure ${fig}{${fig.title.text}}`
        + `\n    y_range set to [${fig.y_range.start} ~ ${fig.y_range.end}]`);
    }, 20);
  }
}

console.log(`[${new Date().getTime()}] figure ${fig}{${fig.title.text}} ${cb_obj} changed:
  [${fig.x_range.start} ~ ${fig.x_range.end}]`);

const xrUpdHndlrSymbol = Symbol.for('xrUpdHndlr');
clearTimeout(fig[xrUpdHndlrSymbol]);
fig[xrUpdHndlrSymbol] = setTimeout(stdUpdPerXR, 50);
