# Python classes review graded
# Problem 1:
#
# Create a Movie class with the following properties/attributes: movieName, rating, and yearReleased.
#
# Override the default str (to-String) method and implement the code that will print the value of all the properties/attributes of the Movie class
#
# In your main function create two instances of the Product class
#
# Assign a value of your choosing for each property/attribute
#
# Print all properties to the console.
#
# Remember, this is the basic model of a Python file with a class
#
# class Movie:
#     def __init__(self):
#     # Class constructor code and property handling
#
#     OTHER PROPERTIES AND METHODS HERE
#
# def main():
# # Create class instance(s) and perform other activities in/from this function
# }
#
# main()
# Problem 2:
#
# Create a class Product that represents a product sold online.
#
# A Product has price, quantity and name properties/attributes.
#
# Override the default str (to-String) method and implement the code that will print the value of all the properties/attributes of the Product class
#
# In your main function create two instances of the Product class
#
# Assign a value of your choosing for each property/attribute
#_
# Print all properties to the console.



class Movie:
    def __init__(self,movieName, rating, yearReleased):
        self.movieName = movieName
        self.rating =rating
        self.yearReleased =yearReleased

def problem1():
    movieanalysis1 = Movie ("ColorPurple", "RatedR", "1985")
    movieanalysis2 = Movie("BestMan", "RatedPg","1990")
    movieanalysis1,movieanalysis2.printproblem1()

    my_instance_str = f'Properties fr the Class movieName\n\n = {self.movieName}\n' \
                  f'rating = {self.rating}\n' \
                  f' yearReleased= {self.yearReleased_p}\n' \
problem1()

return my_instance_str

/2.
class Plasticplates():

def __init__(self, name , quantity, price):

    self.name = name
    self.quantity = quantity
    self.price = price

    def mywork(self):
        print(f"{self.name}, {self.price}, {self.quantity},")
mywork():
printmywork

def problem2():
    online1 = Plasticplates ("Paperplates",""$250.00","300")
    online1 = Plasticplates ("Glassplates","$300.00","500)
    online1.printmywork()

    my_instance_str = f'Properties fr the Class Plasticplates\n\n = {self.name}\n' \
                      f'price = {self.price}\n'
                      f'quantity= {self.quantity_p}\n
problem2():
printproblem2()