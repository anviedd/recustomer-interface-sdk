import os
import time

os.environ.setdefault('INTERFACE_ENDPOINT', 'http://0.0.0.0:9009')
os.environ.setdefault('INTERFACE_API_KEY', '')
os.environ.setdefault('INTERFACE_REQUEST_SERVICE_CODE', 'tracking')
os.environ.setdefault('INTERFACE_API_VERSION', 'v1')

import ec_cart as EcCart

service = EcCart.Service(
    system_code='SHOPIFY', ec_url='',
    access_token=''
)

variant = service.ScriptTag.delete(id=12)
print(variant)
