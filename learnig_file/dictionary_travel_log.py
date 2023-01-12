travle_log = [
    {
        "country" : "France",
        "visits" : 12,
        "cities" : ["Paris", "Lille", "Dijon"]
    },
    {
        "country" : "Germany",
        "visits" : 5,
        "cities" : ["Berlin", "Humburg", "Stuttgart"]
    },
]

def add_new_contry(contry_name, visits, cities):
    new_contry = {}
    new_contry["contry"] = contry_name
    new_contry["visits"] = visits
    new_contry["cities"] = cities
    travle_log.append(new_contry)

add_new_contry("Russia", 2, ["Moscow", "Saint Petersburg"])

print(travle_log)