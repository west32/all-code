from collections import namedtuple


# Location = namedtuple("Location", ["latitude", "longitude"])
def run_example ():


    Apple = namedtuple("Apple", ["species_name", "size","price"])
    apple = Apple("champion", "duży", 20)

    print(apple.species_name)
    print(apple.size)
    print(apple.price)

    print(apple[0])
    print(apple[1])
    print(apple[2])

    for args in apple:
        print(args)
    # location = Location(latitude=54.34,longitude=16.64)
    # # print(location.latitude)
    # # print(location.longitude)
    # # print(type(location))
    #
    # print(location[0])
    #
    # for coordinate in location:
    #     print(coordinate)


if __name__=="__main__":
    run_example()