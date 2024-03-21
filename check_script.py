import requests
import json
import time
import dbus
from datetime import datetime


api_urls = ['http://admin:Password@opensearch.domain.url:9200/historical','http://admin:Password@opensearch.domain.url:9200/historical','http://admin:Password@opensearch.domain.url:9200/historical', 'http://admin:Password@opensearch.domain.url:9200/historical']

# Time between rotation plus one hour
time_between_rotation = 90000


def check_index_alias_status():
    for api_url in api_urls:
        try:
            response = requests.get(api_url)
            responsejson = json.loads(response.text)
            elementos = len(responsejson)
            elementos = elementos - 1
            res = list(responsejson.keys())[elementos]
            epoch_index_time = responsejson[res]['settings']['index']['creation_date']
            epoch_index_time = epoch_index_time[:-3]
            epoch_index_creation_time = int(epoch_index_time)
            current_epoc_time = int(time.time())
            if (current_epoc_time - epoch_index_creation_time) < time_between_rotation:
                print(f" OK --> ",api_url)
            else:
                print(" FAILED --> ", api_url)
                fail_popup_message("Failed on: " + api_url)
        except requests.exceptions.RequestException as e:
            pass

def fail_popup_message(message):
    bus = dbus.SessionBus()
    notify_object = bus.get_object('org.freedesktop.Notifications','/org/freedesktop/Notifications')
    notify_interface = dbus.Interface(notify_object,'org.freedesktop.Notifications')
    titulo = "IMPORTANT!!!"
    tiempo = 10000 # milliseconds
    notify_id = notify_interface.Notify("DBus Test", 0, "gtk-ok", titulo, message, "", {}, tiempo)
 

check_index_alias_status()
