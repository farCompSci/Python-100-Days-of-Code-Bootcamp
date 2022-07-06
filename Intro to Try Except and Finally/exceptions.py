try:
    file = open("somefile.txt")
except FileNotFoundError:
    # print("There was an error")
    file = open("somefile.txt","w")
except KeyError:
    print("That key does not exist")
finally:
    raise TypeError("This is a made-up error")