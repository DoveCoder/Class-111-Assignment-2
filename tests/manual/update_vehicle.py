from pprint import pprint
import requests

TEST_VEHICLE_DATA = {
    "license_plate": "HTP20",
    "v_type": "toyota",
    "color": "black",
    "parking_spot_no": "4",
    "description": "My buddy!",
    "user_id": "2"
}

URL = "http://127.0.0.1:5000/2/vehicles"

def update_vehicle():
    out = requests.put(URL, json=TEST_VEHICLE_DATA)
    if out.status_code == 200:
        pprint(out.json())
    else:
        print("Something went wrong when trying to update.")

if __name__ == "__main__":
    update_vehicle()
