import random
pb = {
    0 : 25,
    1 : 25,
    2 : 20,
    4 : 10,
    6 : 10,
    # "wicket" : 5,
    # "wide" : 5,
}

def choose(num  : int):
    return random.choices(list(pb.keys()), list(pb.values()) , k = num)

# def choose():
#     return random.choices(list(pb.keys()), list(pb.values()))[0]


