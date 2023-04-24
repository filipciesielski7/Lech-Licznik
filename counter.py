from utils import stand_name


def stadium_capacity(sectors_in_sale, sectors_not_in_sale):
    capacity = 0
    for sector in sectors_in_sale + sectors_not_in_sale:
        capacity += sector["capacity"]
    return capacity


def free_seats(sectors_in_sale):
    free = 0
    for sector in sectors_in_sale:
        free += sector["free"]
    return free


def not_available_seats(sectors_not_in_sale, sectors_not_available):
    unavailable_seats = 0
    for sector in sectors_not_in_sale:
        for not_available_sector in sectors_not_available:
            if(sector["name"] == not_available_sector["sector"] and sector["platform"] == stand_name(not_available_sector["stand"])):
                unavailable_seats += sector["capacity"]
                break
    return unavailable_seats
