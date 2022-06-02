import os

os.environ.setdefault('INTERFACE_ENDPOINT', '')
os.environ.setdefault('INTERFACE_API_KEY', '')
os.environ.setdefault('INTERFACE_REQUEST_SERVICE_CODE', 'tracking')
os.environ.setdefault('INTERFACE_API_VERSION', 'v1')

import ec_cart as EcCart

service = EcCart.Service(ec_url='', access_token='')

EcCart.ReInterfaceResource.activate_service(service)

orders = EcCart.Order.find(system_code='SHOPIFY', id=4748013043955)

print(orders)

# # EcCart.ReInterfaceResource.clear_service()
#
#
# orders = EcCart.Order.find()
#
# print(orders)