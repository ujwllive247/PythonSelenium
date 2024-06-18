#       The all() function returns True if all items in an iterable are true, otherwise it returns False.


#

# If the iterable object is empty, the all() function also returns True.



myList = ["name","Detail", "password"]

print(all(myList))



#.....Check if all items in a list are True:


mylist1 = [0, 1, 1]
x = all(mylist1)
print(x)          # Due to zero, this programme return ....False.....


#...Check if all items in a tuple are True:

mytuple = (0, True, False)
x = all(mytuple)

print(x)

#..........Check if all items in a set are True:

myset = {0, 1, 0}
x = all(myset)

print(x)



#Check if all items in a set are True:

mydict = {0 : "Apple", 1 : "Orange"}
x = all(mydict)

 #.........Check if all items in a dictionary are True:
mydict = {0 : "Apple", 1 : "Orange"}
x = all(mydict)