def sectors_capacity(seats):
    capacities = {}
    for seat in seats:
        sector_id = seat["sectorId"]
        if sector_id not in capacities:
            capacities[sector_id] = 1
        else:
            capacities[sector_id] += 1
    return capacities


"""
    seats = [
        {   
            'id': 86174, 
            'sectorId': 61,
            ...
        },
        {
            'id': 86175, 
            'sectorId': 59,
            ...
        },
        {
            'id': 86176, 
            'sectorId': 61,
            ...
        },
        ...
    ]

    capacities = {   
        59: 1, 
        61: 2,
        ...
    }
"""


def sectors_data(sectors, sectors_info, capacities):
    result = []

    for sector in sectors:
        id = sector["id"]
        sector_capacity = capacities[id]
        free_seats = 0
        for price_area in sector['freeSeatsByPriceArea']:
            free_seats += price_area['freeSeatsNo']

        for sector in sectors_info:
            if sector["id"] == id:
                name = sector["name"]
                platform = sector["platform"]
                result.append({'id': id, 'name': name, 'platform': platform,
                               "free": free_seats, "capacity": sector_capacity})
                break

    return result


"""
    sectors = [
        {   
            'id': 59, 
            'seatsReservedFor': 0, 
            'freeSeatsByPriceArea': [
                {
                    'priceAreaId': 3, 
                    'freeSeatsNo': 109
                }
            ]
        },
        {   
            'id': 61, 
            'seatsReservedFor': 0, 
            'freeSeatsByPriceArea': [
                {
                    'priceAreaId': 3, 
                    'freeSeatsNo': 109
                },
                {
                    'priceAreaId': 2, 
                    'freeSeatsNo': 81
                }
            ]
        },
        ...
    ]

    sectors_info = [
        {   
            'id': 61, 
            'name': 'A1', 
            'platform': 'IV im. E. Białasa', 
            ...
        },
        ...
    ]

    capacities = {   
        59: 1, 
        61: 2,
        ...
    }

    result = [
        {
            'id': 216, 
            'name': 'A3', 
            'platform': 'I im. T. Anioły', 
            'free': 0, 
            'capacity': 85
        }, 
        {
            'id': 217, 
            'name': 'A4', 
            'platform': 'I im. T. Anioły', 
            'free': 0, 
            'capacity': 131
        },
        ...
    ]
"""


def additional_sectors_data(sectors_in_sale, sectors_info, capacities):
    result = []

    all_sectors = list(capacities.keys())
    available_sectors = [sector['id'] for sector in sectors_in_sale]
    not_in_sale = list(set(all_sectors) - set(available_sectors))

    for sector in sectors_info:
        if sector["id"] in not_in_sale:
            name = sector["name"]
            platform = sector["platform"]
            result.append({'id': sector["id"], 'name': name, 'platform': platform,
                           "free": 0, "capacity": capacities[sector["id"]]})

    return result
