# sand-dredger
Python lambda code for 3rd party crawl of all Chinese sand dredgers last known positions

User Requirements:
Go to https://datalastic.com/ and get an API key under the free trial

Replace the dummy API key in sand-dredge.py with your new datalastic API key

Run dredger-poll.py to get a response with the last known positions of dredgers based on mmsis


setup
install boto3 in your env
``` pip3 install boto3 ```
install requests lib
``` pip3 install requests ```
download an unzip the package
``` python3 sand-dredge.py ```

you should get back a JSON package with data for the dredgers from API.  example:
```  dredge dredge dredge...
413368330
{'data': {'uuid': '1e568ed1-37a1-165c-f08e-ac7b460058b2', 'name': 'GT 399', 'mmsi': '413368330', 'imo': '9822205', 'eni': None, 'country_iso': 'CN', 'type': 'Cargo', 'type_specific': 'Hopper Dredger', 'lat': 28.26052, 'lon': 121.5492, 'speed': 0.1, 'course': 256, 'heading': None, 'navigation_status': None, 'destination': 'TAIZHOU', 'last_position_epoch': 1631617620, 'last_position_UTC': '2021-09-14T11:07:00Z', 'eta_epoch': None, 'eta_UTC': None}, 'meta': {'duration': 0.002782048, 'endpoint': '/api/v0/vessel', 'success': True}} ``` 
