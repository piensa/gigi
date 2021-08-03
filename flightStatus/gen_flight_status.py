import json
import os
import requests


def flight_status2geojson(data: dict, coordinates: list) -> dict:
    coordinates2 = []
    id_ = f"{data['Response']['flightInfo']['flightNumberInfo']}-{data['Response']['flightInfo']['expectedArrival']}"  # noqa

    position = [
        data['Response']['flightInfo']['longitude'],
        data['Response']['flightInfo']['latitude'],
        data['Response']['flightInfo']['altitude']
    ]

    coordinates2 = coordinates

    if coordinates and coordinates[-1] != position:
        coordinates2.append(position)
    else:
        coordinates2 = [position]

    geojson = {
        'ID': id_,
        'type': 'Feature',
        'geometry': {
            'type': 'LineString',
            'coordinates': coordinates2
        },
        'properties': data['Response']['flightInfo']
    }

    return geojson


def get_flight_status() -> dict:
    # with open('raw-data.json') as fh:
    #    return json.load(fh)

    url = 'http://airborne.gogoinflight.com/abp/ws/absServices/statusTray'
    return requests.get(url).json()


if __name__ == '__main__':

    coordinates = []
    filename = 'flightStatus.geojson'

    flight_status_data = get_flight_status()

    if os.path.exists(filename):
        with open(filename) as fh:
            data2 = json.load(fh)
            coordinates = data2['geometry']['coordinates']

    geojson_data = flight_status2geojson(flight_status_data, coordinates)

    print(json.dumps(geojson_data, indent=4))
    with open(filename, 'w') as fh:
        json.dump(geojson_data, fh, indent=4)
