from pprint import pprint
import requests

TEST_VEHICLE = {
    "license_plate": "HTP80",
    "v_type": "corvette",
    "color": "sliver",
    "parking_spot_no": "1",
    "description": "Dont hurt it!",
    "user_id": "1"
}

URL = "http://127.0.0.1:5000/vehicles"

def test_vehicle_creation():
    out = requests.post(URL, json=TEST_VEHICLE)
    if out.status_code == 201:
        out_json = out.json()
        pprint(out_json)
        return out_json["new_id"]
    else:
        print("Something went wrong while creating a user.")
        return -1 

if __name__ == "__main__":
    new_id = test_vehicle_creation() # VERY USEFUL
