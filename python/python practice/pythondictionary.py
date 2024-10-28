#Accesing elements from a dictionary
new_dict ={1: "Hello",2: "Hi",3:"Hola"}
print(new_dict)
print(new_dict[i])
print(new_dict.get(2))

#updating value
new_dic[i] = "Hey"
print(new_dict)

#Adding value
new_dict[4] = "Nmaste"
print(new_dict)

#creatiing a new dictionary
squares = {1:1,2:4,3:9,4:16,5:25}
print(squares)

#remove a particular item
print(squares.pop[4])
print(squares)

#remove an arbitary item
print(squares.popitem())
print(squares)

#delete a particular item
del squares[1]
print(squares)

#creating a new dictionary
squares = {1:1,2:4,3:9,4:16,5:25}
print(squares)

#remove all items
squares.clear()

#output:{}
print(squares)

#delete the dictionary itself del squares 
#Throws Error on the dictionary has been 

#creating a new dictionary using comprehension
squares = {x: x*x for x  in range (6)}
print(squares)

#Dictionary memberaship test 
squares = {1:!,3:9,5:25,7:49,9:81}
print(1 in squares)
print(2 not  in squares)

#membership tests for key only not value
print(49 in squares)

#Iterating through a dictionary

squares = {1:1,3:9,5:25,7:49}
for i in squares:
    print(squares[i])

#using built-in functions in a dictionary
squares = {1:1,3:9,5:25,7:49,9:81}
print(len(squares))  #prints the length of the dictionary
print(sorted(squares)) #prints the dictionary in sorted order 