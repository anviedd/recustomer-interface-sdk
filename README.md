# ReCustomer Interface SDK

## Requirements

* Python (3.6, 3.7, 3.8, 3.9, 3.10)

# Install using `pip`

```shell
pip install ec_cart
```

# Install using `whl`

```shell
python -m pip install path_to_lib.whl
```

## Setting

* Add the following to your Environment

```shell
INTERFACE_ENDPOINT = 'http://127.0.0.1:9009'
INTERFACE_API_KEY = '1234567'
INTERFACE_SERVICE_CODE = 'tracking'
INTERFACE_API_VERSION = 'v1'
```

## Use
```shell
import ec_cart as EcCart

EcCart.Service(system_code='SHOPIFY')

orders = EcCart.Order.find()
```