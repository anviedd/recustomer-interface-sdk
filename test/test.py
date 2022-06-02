import os

os.environ.setdefault('INTERFACE_ENDPOINT', '')
os.environ.setdefault('INTERFACE_API_KEY', '')
os.environ.setdefault('INTERFACE_SERVICE_CODE', 'tracking')
os.environ.setdefault('INTERFACE_API_VERSION', 'v1')

import ec_cart as EcCart

service = EcCart.Service(system_code='SHOPIFY', ec_url='', access_token='')

EcCart.ReInterfaceResource.activate_service(service)

orders = EcCart.Order.find()

print(orders)

EcCart.ReInterfaceResource.clear_service()

with EcCart.Service.temp(system_code='SHOPIFY', ec_url='', access_token=''):
    orders = EcCart.Order.find()
    print(orders)
