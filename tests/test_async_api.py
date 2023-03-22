import pytest
import httpx
from vinterunofficial import VinterAPIAsync
from unittest.mock import AsyncMock, patch, Mock


@pytest.mark.asyncio
async def test_get_all_active_symbols_async_returns_list():
    """
    Test that get_all_active_symbols returns a list of dicts
    """
    api_key = "my_api_key"
    asset_type = "multi_assets"
    api = VinterAPIAsync(api_key=api_key, asset_type=asset_type)
    api.httpx_client = httpx.AsyncClient()
    mock_response = {
        "result": "success",
        "message": "Success",
        "data": [
            {"symbol": "waves-usd-p-d", "contrib": ["waves-usd-p-r"]},
            {"symbol": "ton-usdt-p-5-d", "contrib": ["ton-usdt-p-r"]},
        ],
        "params": {},
    }
    expected_output = mock_response["data"]
    with patch.object(api.httpx_client, "get", new_callable=AsyncMock) as mock_get:
        mock_get.return_value = AsyncMock(json=Mock(return_value=mock_response))
        result = await api.get_all_active_symbols()
        assert result == expected_output
    await api.httpx_client.aclose()


@pytest.mark.asyncio
async def test_get_latest_data_returns_dict():
    """
    Test that get_latest_data returns a dict
    """
    api_key = "my_api_key"
    asset_type = "single_assets"
    api = VinterAPIAsync(api_key=api_key, asset_type=asset_type)
    api.httpx_client = httpx.AsyncClient()
    mock_response = {
        "result": "success",
        "message": "Success",
        "data": [
            {
                "symbol": "btc-usd-p-r",
                "timestamp": 1647724800,
            }
        ],
        "params": {"symbol": "btc-usd-p-r", "limit": 1},
    }
    expected_output = mock_response["data"]
    with patch.object(api.httpx_client, "get", new_callable=AsyncMock) as mock_get:
        mock_get.return_value = AsyncMock(json=Mock(return_value=mock_response))
        result = await api.get_latest_data("btc-usd-p-r")
        assert result == expected_output
    await api.httpx_client.aclose()


@pytest.mark.asyncio
async def test_get_latest_data_raises_exception():
    """
    Test that get_latest_data raises a ValueError
    """
    api_key = "my_api_key"
    asset_type = "single_assets"
    api = VinterAPIAsync(api_key=api_key, asset_type=asset_type)
    api.httpx_client = httpx.AsyncClient()
    mock_response = {
        "result": "success",
        "message": "Success",
        "data": [],
        "params": {"symbol": "btc-usd-p-r", "limit": 1},
    }
    expected_output = mock_response["data"]
    with patch.object(api.httpx_client, "get", new_callable=AsyncMock) as mock_get:
        mock_get.return_value = AsyncMock(json=Mock(return_value=mock_response))
        with pytest.raises(ValueError):
            await api.get_latest_data("btc-usd-p-r")
    await api.httpx_client.aclose()
   
@pytest.mark.asyncio
async def test_get_latest_value():
    """
    Test that get_latest_value returns a float
    """
    api_key = "my_api_key"
    asset_type = "single_assets"
    api = VinterAPIAsync(api_key=api_key, asset_type=asset_type)
    api.httpx_client = httpx.AsyncClient()
    mock_response = {
        "result": "success",
        "message": "Success",
        "data": [{"symbol": "btc-usd-p-r", "timestamp": 1647724800, "value": 1000}],
        "params": {"symbol": "btc-usd-p-r", "limit": 1},
    }
    expected_output = mock_response["data"][0]["value"]

    with patch.object(api.httpx_client, "get", new_callable=AsyncMock) as mock_get:
        mock_get.return_value = AsyncMock(json=Mock(return_value=mock_response))
        result = await api.get_latest_value("btc-usd-p-r")
        assert result == expected_output
    await api.httpx_client.aclose()


def test_filter_by_symbol():
    """
    Test that _filter_by_symbol returns a list of dicts
    """
    api_key = "my_api_key"
    asset_type = "multi_assets"
    api = VinterAPIAsync(api_key=api_key, asset_type=asset_type)
    symbol = "waves-usd-p-d"
    expected_output = [
        {"symbol": "waves-usd-p-d", "contrib": ["waves-usd-p-r"]},
    ]
    mock_data = [
        {"symbol": "waves-usd-p-d", "contrib": ["waves-usd-p-r"]},
        {"symbol": "ton-usdt-p-5-d", "contrib": ["ton-usdt-p-r"]},
    ]
    result = api._filter_by_symbol(mock_data, symbol)
    assert result == expected_output


@pytest.mark.asyncio
async def test_get_all_active_symbols_async_with_frequency_returns_filtered_list():
    """
    Test that get_all_active_symbols_async returns a list of dicts
    """
    api_key = "my_api_key"
    asset_type = "multi_assets"
    api = VinterAPIAsync(api_key=api_key, asset_type=asset_type)
    api.httpx_client = httpx.AsyncClient()
    mock_response = {
        "result": "success",
        "message": "Success",
        "data": [
            {"symbol": "waves-usd-p-d", "contrib": ["waves-usd-p-r"]},
            {"symbol": "ton-usdt-p-5-r", "contrib": ["ton-usdt-p-r"]},
        ],
        "params": {},
    }
    expected_output = [{"symbol": "waves-usd-p-d", "contrib": ["waves-usd-p-r"]}]
    with patch.object(api.httpx_client, "get", new_callable=AsyncMock) as mock_get:
        mock_get.return_value = AsyncMock(json=Mock(return_value=mock_response))
        result = await api.get_all_active_symbols(frequency="d")
        assert result == expected_output
    await api.httpx_client.aclose()


@pytest.mark.asyncio
async def test_get_all_active_symbols_async_symbol_only_returns_symbol_list():
    """
    Test that get_all_active_symbols_async returns a list of dicts
    """
    api_key = "my_api_key"
    asset_type = "multi_assets"
    api = VinterAPIAsync(api_key=api_key, asset_type=asset_type)
    api.httpx_client = httpx.AsyncClient()
    mock_response = {
        "result": "success",
        "message": "Success",
        "data": [
            {"symbol": "waves-usd-p-d", "contrib": ["waves-usd-p-r"]},
            {"symbol": "ton-usdt-p-5-d", "contrib": ["ton-usdt-p-r"]},
        ],
        "params": {},
    }
    expected_output = ["waves-usd-p-d", "ton-usdt-p-5-d"]
    with patch.object(api.httpx_client, "get", new_callable=AsyncMock) as mock_get:
        mock_get.return_value = AsyncMock(json=Mock(return_value=mock_response))
        result = await api.get_all_active_symbols(symbol_only=True)
        assert result == expected_output
    await api.httpx_client.aclose()