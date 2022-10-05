from array import array
from importlib.machinery import all_suffixes
from multiprocessing.sharedctypes import Value
from os import remove


array = ["naam", "weer", "leeftijd"]

dictionary = {
            1: "voornaam",
            2: "achternaam",
            3: "leeftijd"
            }
dictionary[4] = "Serhat"

# print(dictionary [3])

for key,value in dictionary.items():
    print(key,value)

del dictionary[1]
print (dictionary)


array= [[1,2,4,58],[3,4,5,12],[3,4,5,52]]

# # is gelijk aan:    1 2 4 58
#                     3 4 5 12
#                     3 4 5 52


for i in array: # array= [[1,2,4,58],[3,4,5,12][3,4,5,52]]
    for  k in i: #i=[1,2,4,58]
        print (k)




#functie 2: schrijf een functie die 1 argument
#verwacht. Dit argement is een 2d-array. je 
#delete alle getallen met waarde 10.


array.pop(0) #1ste lijn wordt verwijderd
print(array)

a=["ser", "hat"]


#functie 1: schrijf een functie die 2 argumenten
#verwacht. Beiden argumenten zijn arrays.
#pint elk element uit behalve het getal 10

def functie1(list1, list2):
    for i in list1:
        if i !=10:
            print(i)
    for i in list2:
        if i !=10:
            print(i)

array1 = [1,5,10,15,20]
array2 = [2,4,8,10,12]

functie1(array1, array2)

#functie 2: schrijf een functie die 1 argument
#verwacht. Dit argement is een 2d-array. je 
#delete alle getallen met waarde 10.

# def functie2(array2d):
#     newArray = []                    # newArray is zonde de 10
#     for i in array2d:                # i=[1,5,10,15,20]
#         sArray=[]                    # sArray = []
#         for k in i:                  # k = 1
#             if (k !=10):             # true
#                 sArray.append(k)     # sArray = [1]
#         newArray.append(sArray)        

# ab= [[1,5,10,15,20],[2,4,8,10,12],[1,3,5,9,10]]

# functie2(ab)



