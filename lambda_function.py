import json
import requests
from utils import getDate
from sectors import sectors_capacity, sectors_data, additional_sectors_data


def get_data(eventId):
    s = requests.session()

    s.get(f'https://bilety.lechpoznan.pl/Stadium/Index?eventId={eventId}')

    cookies = s.cookies.get_dict()

    response_seats = s.post("https://bilety.lechpoznan.pl/Stadium/GetWGLSeats",
                            params={"eventId": eventId}, cookies=cookies)

    response_free_seats = s.post("https://bilety.lechpoznan.pl/Stadium/GetWGLSectorsInfo",
                                 params={"eventId": eventId}, cookies=cookies)

    response_sectors_info = s.post("https://bilety.lechpoznan.pl/Stadium/GetWGLSectors",
                                   params={"eventId": eventId}, cookies=cookies)

    seats = response_seats.json()

    free_seats = response_free_seats.json()

    sectors_info = response_sectors_info.json()

    date = getDate(free_seats['timestamp'])
    capacities = sectors_capacity(seats["seats"])
    sectors_in_sale = sectors_data(
        free_seats['sectors'], sectors_info["sectors"], capacities)
    sectors_not_in_sale = additional_sectors_data(
        sectors_in_sale, sectors_info["sectors"], capacities)

    return sectors_in_sale, sectors_not_in_sale, date


def lambda_handler(event, context):
    id = 2250
    in_sale, not_in_sale, date = get_data(id)
    print(in_sale, not_in_sale, date)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
