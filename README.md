# ReCustomer Interface SDK

The ReCustomer Interface Python Library

Documentation for version: 0.1.0

# Usage

## Requirements

* Python (3.6, 3.7, 3.8, 3.9, 3.10)

- You need to provide us with relevant information about the system you connect to including API key, endpoint, API
  version

## Installation

We do not release the SDK to the public. Use it by installing directly from GitHub instead.

Use the version you want to install. It can be the main branch or any commit.

* Use main branch
    ```shell
    python -m pip install git+https://github.com/anviedd/recustomer-interface-sdk.git#egg=ec_cart
    ```

* Use commit
    ```shell
    python -m pip install git+https://github.com/anviedd/recustomer-interface-sdk.git@{commitID}#egg=ec_cart
    ```
  
* Note. if you have installed it before. Please remove it before reinstalling it.
    ```shell
    pip uninstall ec_cart
    ```

## Getting Started

### Settings

- Add the following to your Environment

    ```shell
    INTERFACE_ENDPOINT = 'http://127.0.0.1:9009'
    INTERFACE_API_KEY = '1234567'
    INTERFACE_REQUEST_SERVICE_CODE = 'tracking'
    INTERFACE_API_VERSION = 'v1'
    ```

### Use

1. Need to initialize the service to use.

    ```shell
    import ec_cart as EcCart
    
    service = EcCart.Service(system_code='SHOPIFY', ec_url='', access_token='')
    ```

2. Now you're ready to make authorized API requests to your shop!

    ```shell
    orders = service.Order.find()
    ```
   * Create Script Tag
        ```shell
        script_tag = service.ScriptTag.create(event="", src="")
        - event: Valid values: "onload"
        - src: The URL of the remote script.
        ```
   * Delete Script tag
        ```shell
        script_tag = service.ScriptTag.delete(id="1234")
        ```
   * Detail Script Tag
        ```shell
        script_tag = service.ScriptTag.find(id="1234")
        ```

### Support Model

* Order
* Product
* Variant
* ScriptTag