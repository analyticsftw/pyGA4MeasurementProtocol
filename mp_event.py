import json, requests, time
from config import settings

def send_event(measurement_id, api_secret, event_name, event_params):
    ss = settings['client_id']
    ts = str(time.time()).split(".")[0]

    url = "https://www.google-analytics.com/mp/collect?measurement_id=" + measurement_id + "&api_secret=" + api_secret
    headers = {"Content-Type": "application/json"}
    event = {'name': event_name, 'params': event_params }
    events = [event]
    body = {
        "client_id": ss+"."+ts,
        "events": events
    }
    response = requests.post(url, headers=headers, data=json.dumps(body))
    return response


if __name__ == "__main__":
    ts = str(time.time()).split(".")[0]
    measurement_id = settings['measurement_id']
    api_secret = settings['api_secret']
    event_name = "fridge_door_open"
    event_params = {
        "firmware_version": "20230901",
        "model": "Connected fridge",
        "brand": "Artic King",
        "timestamp_micros": ts+"000"
    }

    response = send_event(measurement_id, api_secret, event_name, event_params)
    if response.status_code == 204:
        print("Event *"+event_name+"* sent successfully with parameters:")
        print(json.dumps(event_params, indent=4))
        
    else:
        print("Error sending event: {}".format(response.status_code))