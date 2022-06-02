# ReCustomer Interface SDK

The ReCustomer Interface Python Library

Documentation for version: 0.0.1

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

    * In case you only have 1 session

        ```shell
        import ec_cart as EcCart

        service = EcCart.Service(system_code='SHOPIFY', ec_url='', access_token='')
        ```
    * In case you have more than one session

        ```shell
        import ec_cart as EcCart

        service = EcCart.Service()
        ```

2. Now you're ready to make authorized API requests to your shop!

    * Active Service
        ```shell
        EcCart.ReInterfaceResource.activate_service(service)
        ```

    * In case you only have 1 session
        ```shell
        orders = EcCart.Order.find()
        ```

    * In case you have more than one session
        ```shell
        shopify_orders = EcCart.Order.find(system_code='SHOPIFY', ec_url='', access_token='')
        ec_cube_orders = EcCart.Order.find(system_code='EC_CUBE', ec_url='', access_token='')
        ```
   
4. It is best practice to clear your service when you're done. A temporary service does this automatically

    ```shell
    EcCart.ReInterfaceResource.clear_service()
    ```
