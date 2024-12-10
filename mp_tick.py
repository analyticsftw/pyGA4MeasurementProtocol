import json, requests, time
from config import settings

def send_event(measurement_id, api_secret, event_name, event_params):
    ss = settings['client_id'] #arbitrary client ID

    ts = str(time.time()).split(".")[0] #timestamp in seconds

    # Build the Measurement Protocol Endpoint URL with parameters
    url = "https://www.google-analytics.com/mp/collect?measurement_id=" + measurement_id + "&api_secret=" + api_secret
    headers = {"Content-Type": "application/json"}
    event = {
        'name': event_name, 
        'params': event_params 
    }
    events = [event]
    body = {
        "client_id": ss+"."+ts,
        "events": events
    }
    # Send the event
    response = requests.post(url, headers=headers, data=json.dumps(body))
    return response


if __name__ == "__main__":
    ts = str(time.time()).split(".")[0]
    print(ts)
    # This will equal True if the timestamp is even, False if it's odd
    if (int(ts) % 2) == 0:
        myBool = True
        myEvent = "tick" 
    else:
        myBool = False
        myEvent = "tock" 
    measurement_id = settings['measurement_id']
    api_secret = settings['api_secret']
    event_name = myEvent
    event_params = {
        "timestamp": ts,
        "timestamp_micros": ts+"000"
    }

    response = send_event(measurement_id, api_secret, event_name, event_params)
    with open("mp_tick.log", "a") as f:
        f.write(f"Event *{event_name}* sent successfully with code {response.status_code} and parameters:\n")
        f.write(json.dumps(event_params, indent=4))
        f.write("\n")