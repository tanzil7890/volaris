# Get future trading days

> `D.calendar(future=True)` will be used

## Requirements

```bash
pip install -r requirements.txt
```

## Collector Data

```bash
# parse instruments, using in volaris/instruments.
python future_trading_date_collector.py --volaris_dir ~/.volaris/volaris_data/cn_data --freq day
```

## Parameters

- volaris_dir: volaris data directory
- freq: value from [`day`, `1min`], default `day`



