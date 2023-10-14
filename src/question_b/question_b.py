#write functions here, don't add input('') statements here!
def get_miles_per_hour(km, mins):
    kph_To_mph = km * (.621371)
    Mph = kph_To_mph * (mins / 60)

    if(km < 0 or mins < 0):
        print("Invalid arguments")

    return Mph