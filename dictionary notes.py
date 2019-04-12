states = {
     "CA": "california",
     "FL": "Florida",
     "AK": "Alaska",
     "GA": "Georgia"

}

print(states["CA"])
print(states["AK"])


complex_dictionary = {
    "CA": {
        "NAME": "California",
        "POPULATION": 39500000,
        "CITIES": [
            "Fresno",
            "San Francisco",
            "Los Angles"

        ]
    },
    "FL": {
        "NAME": "Florida",
        "POPULATION": 2130000,
        "CITIES": [
            "Miami",
            "Tampa",
            "jacksonville",

        ]
    },
    "AK": {
        "NAME": "Alaska",
        "POPULATION": 37000,
        "Cities": [
            "Anchorage",
            "Fairbanks",
            "Juneau"

        ]
    },
    "GA": {
        "NAME": "Georgia",
        "POPULATION": 1050000,
        "Cities": [
            "Atlanta",
            "savannah",
            "Augusta"
        ]
    }

}



print(complex_dictionary["AK"]['NAME'])





print(complex_dictionary["FL"]['NAME'])
print(complex_dictionary["GA"]['NAME'])

print(complex_dictionary.keys())
print(complex_dictionary.items())

for key, value in complex_dictionary.items():
    print(key)
    print(value)
    print("-" * 20)

# this is what make it look pretty
print()
for state, info in complex_dictionary.items():
    for label, stats in info.items():
        print(label)
        print(stats)
        print("-" * 20)
    print("=" * 20)
    