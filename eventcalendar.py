import math
from datetime import datetime, timedelta

months = [
    "Early Spring",
    "Spring",
    "Late Spring",
    "Early Summer",
    "Summer",
    "Late Summer",
    "Early Autumn",
    "Autumn",
    "Late Autumn",
    "Early Winter",
    "Winter",
    "Late Winter",
]

hour_ms = 50000
day_ms = 24 * hour_ms
month_length = 31
year_length = len(months)

month_ms = month_length * day_ms
year_ms = year_length * month_ms

year_zero = 1560275700000

zoo_start = year_zero + year_ms * 66
zoo_time_length = year_ms / 2

pets = ["Elephant", "Giraffe", "Blue Whale", "Tiger", "Lion", "Monkey"]

def get_offset(month, day, hour=0):
    return months.index(month) * month_length * day_ms + (day - 1) * day_ms + hour * hour_ms

def time_to_skyblock_year(time):
    return math.floor((time - year_zero) / year_ms) + 1

def get_zoo_pet(time):
    iterations = math.floor((time - zoo_start) / zoo_time_length)
    return pets[iterations % len(pets)]

def get_jacob_event_times():
    times = []
    month = 0
    while month < 12:
        day = 2
        while day <= 31:
            times.append({
                "start": get_offset(months[month], day),
                "end": get_offset(months[month], day),
            })
            if day == 30:
                break
            day += 3
            if day > 31:
                day = 1  
                month += 1
                if month == 12:
                    break  
    return times

def get_dark_auction_event_times():
    times = []
    month = 0
    while month < 12:
        day = 1
        while day <= 31:
            times.append({
                "start": get_offset(months[month], day),
                "end": get_offset(months[month], day),
            })
            if day == 29:
                break
            day += 3
            if day > 31:
                day = 1  
                month += 1
                if month == 12:
                    break  
    return times

def get_fallen_star_cult_times():
    times = []
    for month in range(12):
        for i in range(1, 5):
            times.append({
                "start": get_offset(months[month], i * 7),
                "end": get_offset(months[month], i * 7, 6),
            })
    return times

def get_unique_list_by(array, key):
    return list({item[key]: item for item in array}.values())

event_times ={
    "BANK_INTEREST": {
        "name": "Bank Interest",
        "times": [
            {"start": get_offset("Early Spring", 1), "end": get_offset("Early Spring", 1)},
            {"start": get_offset("Early Summer", 1), "end": get_offset("Early Summer", 1)},
            {"start": get_offset("Early Autumn", 1), "end": get_offset("Early Autumn", 1)},
            {"start": get_offset("Early Winter", 1), "end": get_offset("Early Winter", 1)},
        ],
    },
    "DARK_AUCTION": {
        "name": "Dark Auction",
        "times": get_dark_auction_event_times(),
    },
    "ELECTION_BOOTH_OPENS": {
        "name": "Election Booth Opens",
        "times": [{"start": get_offset("Late Summer", 27), "end": get_offset("Late Summer", 27)}],
    },
    "ELECTION_OVER": {
        "name": "Election Over",
        "times": [{"start": get_offset("Late Spring", 27), "end": get_offset("Late Spring", 27)}],
    },
    "FALLEN_STAR_CULT": {
        "name": "Cult of the Fallen Star",
        "times": get_fallen_star_cult_times(),
    },
    "FEAR_MONGERER": {
        "name": "Fear Mongerer",
        "times": [{"start": get_offset("Autumn", 26), "end": get_offset("Late Autumn", 3)}],
    },
    "JACOBS_CONTEST": {
        "name": "Jacob's Farming Contest",
        "times": get_jacob_event_times(),
    },
    "JERRYS_WORKSHOP": {
        "name": "Jerry's Workshop",
        "times": [{"start": get_offset("Late Winter", 1), "end": get_offset("Late Winter", 31)}],
    }
}
