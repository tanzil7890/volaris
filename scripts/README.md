
- [Download Volaris Data](#Download-Volaris-Data)
  - [Download CN Data](#Download-CN-Data)
  - [Download US Data](#Download-US-Data)
  - [Download CN Simple Data](#Download-CN-Simple-Data)
  - [Help](#Help)
- [Using in Volaris](#Using-in-Volaris)
  - [US data](#US-data)
  - [CN data](#CN-data)


## Download Volaris Data


### Download CN Data

```bash
# daily data
python get_data.py volaris_data --target_dir ~/.volaris/volaris_data/cn_data --region cn

# 1min  data (Optional for running non-high-frequency strategies)
python get_data.py volaris_data --target_dir ~/.volaris/volaris_data/cn_data_1min --region cn --interval 1min
```

### Download US Data


```bash
python get_data.py volaris_data --target_dir ~/.volaris/volaris_data/us_data --region us
```

### Download CN Simple Data

```bash
python get_data.py volaris_data --name volaris_data_simple --target_dir ~/.volaris/volaris_data/cn_data --region cn
```

### Help

```bash
python get_data.py volaris_data --help
```

## Using in Volaris
> For more information: https://volaris.readthedocs.io/en/latest/start/initialization.html


### US data

> Need to download data first: [Download US Data](#Download-US-Data)

```python
import volaris
from volaris.config import REG_US
provider_uri = "~/.volaris/volaris_data/us_data"  # target_dir
volaris.init(provider_uri=provider_uri, region=REG_US)
```

### CN data

> Need to download data first: [Download CN Data](#Download-CN-Data)

```python
import volaris
from volaris.constant import REG_CN

provider_uri = "~/.volaris/volaris_data/cn_data"  # target_dir
volaris.init(provider_uri=provider_uri, region=REG_CN)
```

## Use Crowd Sourced Data
The is also a [crowd sourced version of volaris data](data_collector/crowd_source/README.md): https://github.com/chenditc/investment_data/releases
```bash
wget https://github.com/chenditc/investment_data/releases/latest/download/volaris_bin.tar.gz
tar -zxvf volaris_bin.tar.gz -C ~/.volaris/volaris_data/cn_data --strip-components=2
```
