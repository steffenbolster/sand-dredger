import hashlib
import json
import os
import boto3

import requests

use_api = True

def getAisData(api_key, mmsi):
    params = {
        'api-key': api_key,
        'mmsi': mmsi
    }
    method = 'vessel'
    api_base = 'https://api.datalastic.com/api/v0/'
    api_result = requests.get(api_base+method, params)
    api_response = api_result.json()
    print(api_response)
    return api_response['data']

def main():
    # the main function loops through the MMSI codes for identified dredgers and return known data for those dredgers
    # source - www.vesselfinder.com
    print('dredge dredge dredge...')
    # the below is not a real API key.  you need to paste in your API key from datalastic
    api_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    # the below are MMSI codes associated with all known Chinese dredgers from above source.
    mmsis = [
            "413368330",
            "413266590",
            "413378050",
            "412070420",
            "413375380",
            "412044750",
            "412303150",
            "413040170",
            "413368150",
            "413355510",
            "412018470",
            "414401730",
            "412379830",
            "413450130",
            "412018530",
            "412043810",
            "413380310",
            "412044510",
            "412044770",
            "413450730",
            "412053050",
            "413439280",
            "413363180",
            "413335440",
            "413350620",
            "412044760",
            "412379280",
            "413217170",
            "413040180",
            "413699480",
            "413486920",
            "413491530",
            "413040020",
            "413381580",
            "422453200",
            "412441550",
            "413472940",
            "413491530",
            "412375290",
            "413221520",
            "413017070",
            "412303160",
            "412765420",
            "413260450",
            "413439530",
            "412045240",
            "413487270",
            "412018470",
            "412270580",
            "412379830",
            "412052510",
            "413274630",
            "413297380",
            "413331000",
            "412525000",
            "413472070",
            "413266590",
            "413430220",
            "413263180",
            "412373720",
            "413217170",
            "413355510",
            "413381570",
            "413335440",
            "412018470",
            "413472940",
            "412379490",
            "413486920",
            "413272210",
            "412044760",
            "412477530",
            "412303150",
            "413355510",
            "413486920",
            "412379830",
            "413306090",
            "413368150",
            "412018470",
            "413236760",
            "414352290",
            "413376050", 
            "413472070"
            ]
    smaq = []
    for mmsi in mmsis:
        try:
            print(mmsi)
            vessel_data = getAisData(api_key, mmsi)
            smaq.append(vessel_data)
        except KeyError:
            print('KeyError, check your API key bro...')
    return smaq

main()
