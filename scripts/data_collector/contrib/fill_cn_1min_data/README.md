# Use 1d data to fill in the missing symbols relative to 1min


## Requirements

```bash
pip install -r requirements.txt
```

## fill 1min data

```bash
python fill_cn_1min_data.py --data_1min_dir ~/.volaris/csv_data/cn_data_1min --volaris_data_1d_dir ~/.volaris/volaris_data/cn_data
```

## Parameters

- data_1min_dir: csv data
- volaris_data_1d_dir: volaris data directory
- max_workers: `ThreadPoolExecutor(max_workers=max_workers)`, by default *16*
- date_field_name: date field name, by default *date*
- symbol_field_name: symbol field name, by default *symbol*

