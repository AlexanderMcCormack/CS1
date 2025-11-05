

def get_type(length, height, width, sides):
    if 3.5 <= length <= 4.25 and  3.5 >= height <= 6 and .007 <= width <= .016:
        return ("regular post card")
    elif 4.35 <= length <= 6 and  6 >= height <= 11.5 and .007 <= width <= .015:
        return ("large post card")
    elif 3.5 <= length <= 6.125 and  5 >= height <= 11.5 and .016 <= width <= .025:
        return ("Envelope")
    elif 6.125 <= length <= 24 and  11 >= height <= 18 and .25 <= width <= .5:
        return ("LARGE ENVELOPE")
    elif length > 24 and height > 18 and width > .5 and sides <= 84:
        return ("PACKAGE")
    elif length > 24 and height > 18 and width > .5 and 84 < sides <= 130:
        return ("large package")
        

def zone_1(distance):
    if distance >1 and distance <6999:
        return 1 
    elif distance >7000 and distance <19999:
        return 2
    elif distance >20000 and distance <35999:
        return 3
    elif distance >36000 and distance <62999:
        return 4
    elif distance >63000 and distance <84999:
        return 5
    elif distance >85000 and distance <99999:
        return 6
    
def zone_2(distance_2):
    if distance_2 >1 and distance_2 <6999:
        return 1 
    elif distance_2 >7000 and distance_2 <19999:
        return 2
    elif distance_2 >20000 and distance_2 <35999:
        return 3
    elif distance_2 >36000 and distance_2 <62999:
        return 4
    elif distance_2 >63000 and distance_2 <84999:
        return 5
    elif distance_2 >85000 and distance_2 <99999:
        return 6

def find_distance(startdistance, enddistance):
    startzone = zone_1(startdistance)
    endzone = zone_2(enddistance)

    if startzone == 'unmailable' or endzone == 'unmailable':
        return 'unmailable'
    return abs(startzone - endzone)


def find_price(package_type, per_zone):
    
    if package_type == "regular post card":
        return .20 + .03 *(per_zone)
    elif package_type == "large post card":
        return .37 + .03 *(per_zone)
    elif package_type == "envelope":
        return .37 + .04 *(per_zone)
    elif package_type == "LARGE ENVELOPE":
        return .60 + .05 *(per_zone)
    elif package_type == "PACKAGE":
        return 2.95 + .25 *(per_zone)
    elif package_type == "large package":
        return 3.95 + .35 *(per_zone)
def data():
    data = input('').split(',')
    return float(data[0], float(data[1]), float(data[2]), int(data[3]), int(data[4]))

def main(package_type):
    input("what is the legnth, height, and width of your package, and how far is your destination")
    data = input("what is the legnth, height, and width of your package, and how far is your destination")
    data1 = data.split(", ")

    length  = float(data1[0])
    width = float(data1[1])
    height = float(data1[2])
    startzone = int(data1[3])
    endzone = int(data1[4])
    package_type = get_type(length, height, width)
    total_zones = find_distance(startzone, endzone)
    price = find_price(package_type, total_zones)
    print(price)

