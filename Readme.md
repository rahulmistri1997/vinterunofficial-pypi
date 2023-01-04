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

# Get all assets (AssetType = single_assets) as while Creating the object we have set AssetType = single_assets
all_active_symbol = [asset["symbol"] for asset in vinter.get_all_active_symbols()]

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

# Get all assets (AssetType = single_assets) as while Creating the object we have set AssetType = single_assets
all_active_symbol = [asset["symbol"] for asset in vinter.get_all_active_symbols()]

selected_symbol = "btc-usd-p-d"

# Get the latest value of the asset
data = vinter.get_data_by_date(selected_symbol, ["2022-12-04", "2022-12-09"])

for asset in data:
    print("The price of {} on {} is {}".format(selected_symbol, asset["created_at"], asset["value"]))

```


