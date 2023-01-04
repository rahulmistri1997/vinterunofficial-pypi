# Unofficial Wrapper for the Vinter API

This is an unofficial wrapper for the Vinter API. It is not affiliated with Vinter in any way.

## Installation

```bash
pip install vinterunofficial
```

## Documentation
[VinterAPIDocumentation](https://www.vinterapi.com/)

## Usage

## Valid AssetType
- single_assets
- multi_assets

### Get Latest Data
```python
from vinterunofficial import VinterAPI

# vinter = VinterAPI(<APIKEY>, <AssetType>)
vinter = VinterAPI(123456, "single_assets")

selected_symbol = "btc-usd-p-d"

# Get the latest value of the asset
data = vinter.get_latest_data(selected_symbol)

current_price = data[0]["value"]
created_at = data[0]["created_at"]

print("The current price of {} is {} at {}".format(selected_symbol, current_price, created_at))

```

### Get Historical Data
```python
from vinterunofficial import VinterAPI

# vinter = VinterAPI(<APIKEY>, <AssetType>)
vinter = VinterAPI(123456, "single_assets")

selected_symbol = "btc-usd-p-d"

# Get the latest value of the asset
data = vinter.get_data_by_date(selected_symbol, ["2022-12-04", "2022-12-09"])

for asset in data:
    print("The price of {} on {} is {}".format(selected_symbol, asset["created_at"], asset["value"]))

```

### Get All Active Symbols
```python
from vinterunofficial import VinterAPI

single_assets = VinterAPI(123456, "single_assets")
multi_assets = VinterAPI(123456, "multi_assets")

all_active_symbol_multi = [asset["symbol"] for asset in multi_assets.get_all_active_symbols()]
all_active_symbol_single = [asset["symbol"] for asset in single_assets.get_all_active_symbols()]

print("All active symbols for multi assets: {}".format(all_active_symbol_multi))
print("All active symbols for single assets: {}".format(all_active_symbol_single))

```
