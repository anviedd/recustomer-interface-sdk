import os

os.environ.setdefault('INTERFACE_ENDPOINT', 'http://127.0.0.1:9009')
os.environ.setdefault('INTERFACE_API_KEY', '')
os.environ.setdefault('INTERFACE_REQUEST_SERVICE_CODE', 'tracking')
os.environ.setdefault('INTERFACE_API_VERSION', 'v1')

import ec_cart as EcCart

service = EcCart.Service(
    system_code='SHOPIFY', ec_url='',
    access_token=''
)

variant = service.Variant.find(42599108903155)

print(variant)
