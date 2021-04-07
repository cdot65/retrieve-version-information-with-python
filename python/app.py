from jnpr.junos import Device
from pprint import pprint
import json


with Device(host='dallas-fw0', user='automation', password='juniper123') as network_device:
    try:
        show_version = network_device.rpc.get_software_information({'format': 'json'})
    except:
        pass

pprint(show_version)