import json
import requests
import time

def send_event(measurement_id, api_secret, event_name, event_params):
    ss = "1693324901"
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
    measurement_id = "G-M2W6S3W2G0"
    api_secret = "K0K8jYcfT5eZr6MhPbySkw"
    event_name = "fridge_door_open"
    event_params = {
        # "user_id": "julien",
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