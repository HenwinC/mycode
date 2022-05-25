#!/usr/bin/env python3
"""Returning the location of the ISS in latitude/longitude"""
import requests
    
URL= "http://api.open-notify.org/iss-now.json"
def main():
    resp= requests.get(URL).json()
    print(resp)
    print('The current location of ISS:')
    print(resp['iss_position']['latitude'])
    print(resp['iss_position']['longitude'])
    # print(resp['longitude'])

if __name__ == "__main__":
    main()