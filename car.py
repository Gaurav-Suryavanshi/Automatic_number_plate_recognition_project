import requests
import json
import sys
regions = ['in'] # Change to your country
with open('car-number-plate-delhi-vehicle-registration-license-india-european-standard-sizes_97886-10341.jpg', 'rb') as fp:
    response = requests.post(
        'https://api.platerecognizer.com/v1/plate-reader/',
        data=dict(regions=regions),  # Optional
        files=dict(upload=fp),
        headers={'Authorization': 'Token 'YOUR_TOKEN'})
plate_number = response.json()['results'][0]['plate']
print("plate number is : " +plate_number.upper())
