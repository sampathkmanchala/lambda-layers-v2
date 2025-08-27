import requests
from pyqrcode import create as create_qr_code 

def handler(event,context):
  result = requests.get("www.google.com")
  print("result", result)
  return "Hello World2"

