class User:
    #pass  # pass keyword makes it so that you can pass the class attributes and behaviour
    def __init__(self,user_id,user_name): #self refers to the object being initialized, you can add other parameters
        """This will be called everytime an object is created.
        This is basically a constructor."""
        print("You have updated the class")
        self.id = user_id
        self.user_name = user_name
        self.followers = 0
        self.following = 0

    def follow(self,user): # always needs a self method, so that it always knows the object that calls it
        user.followers += 1
        self.following += 1

# user_1 = User()
# user_1.id = "001"  # using the dot notation and values, you can add attributes to the class
# user_1.username = "angela" ### This still works, however with a parameter it should work better
user_1 = User("001","angela")
user_2 = User("002","jack")
user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)


