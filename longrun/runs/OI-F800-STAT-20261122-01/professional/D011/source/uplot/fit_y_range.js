function fitYRangePerXR() {
  const renderers = fig.renderers;
  function isFullyHidden(cds) {
    return renderers.filter(r => r.data_source === cds)
      .every(r => !r.visible);
  }

  const xr_start = fig.x_range.start;
  const xr_end = fig.x_range.end;
  
  // 检查是否是对数坐标轴
  const isLogAxis = fig.y_scale && fig.y_scale.type === 'LogScale';

  let min_y = Infinity, max_y = -Infinity;

  for (const [cds, x_field, y_fields] of y_fits) {
    // ignore this CDS if all renderers referencing it are hidden
    if (isFullyHidden(cds)) continue;

    const x_ds = cds.data[x_field];
    if (!x_ds) {
      console.error(`[${x_field}] not in cds!`, cds);
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

    // Check y values in range
    for (const y_field of y_fields) {
      const y_ds = cds.data[y_field];
      if (!y_ds) {
        console.error(`[${y_field}] not in cds!`, cds);
        continue;
      }
      for (let i = start_i; i < end_i; i++) {
        if (x_ds[i] < xr_start || x_ds[i] >= xr_end)
          continue; // ignore such data points, they are here due to not monotonicly sorted
        const y = y_ds[i];
        // 对数坐标轴只考虑正数，线性坐标轴考虑所有有限数值
        if (isFinite(y) && (!isLogAxis || y > 0)) {
          if (y < min_y) min_y = y;
          if (y > max_y) max_y = y;
        }
      }
    }
  }

  if (isFinite(min_y) && isFinite(max_y)) {
    setTimeout(() => {
      if (isLogAxis) {
        // 对数坐标轴的处理
        const log_min = Math.log10(min_y);
        const log_max = Math.log10(max_y);
        const log_margin = (log_max - log_min) * 0.1;
        
        fig.y_range.start = Math.pow(10, log_min - log_margin);
        fig.y_range.end = Math.pow(10, log_max + log_margin);
      } else {
        // 线性坐标轴的处理
        const margin = (max_y - min_y) * 0.1;
        fig.y_range.start = min_y - margin;
        fig.y_range.end = max_y + margin;
      }
      console.log(`y_range set to [${fig.y_range.start}, ${fig.y_range.end}] (${isLogAxis ? 'log' : 'linear'} axis)`);
    }, 20);
  }
}

// Handle x-range changes
const xrUpdHndlrSymbol = Symbol.for('xrUpdHndlrFitY');
clearTimeout(fig[xrUpdHndlrSymbol]);
fig[xrUpdHndlrSymbol] = setTimeout(fitYRangePerXR, 50);
