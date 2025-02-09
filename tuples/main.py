stuDetails=("surabahi",89)

#packing
address=("227","Brickfield Shelter","Bangalore","Karantaka","562107")

for x in address:
    print (x,end="")


 #unpacking
houseno,apartName,city,state,pin =address

print()
print("HNO",houseno)
print("APT NO",apartName)
print(city)
print(state)
print(pin)

#A tuple can also be created without using parentheses
my_tuple =3,4.6,"dog"
print(my_tuple)

#nested tuple
n_tuple=("mouse",[8,4,6],(1,2,3))

#nested index 
print(n_tuple[0][3])
print(n_tuple[1][1])

#accessing tuple elements using slicing

my_tuple=("p","r","o","g","r","a","m","i","z")

#elements 2nd to 4th
#output :("t","o","g")
print(my_tuple[1:4])

#elements beginning to 2nd
#output:("p","r")
print(my_tuple[:-7])

#elements 8th to end
#output: ("i","z")
print(my_tuple[7:])

#elements 8th to end
#output ("p","r","o","g","r","a","m","i","z")
print(my_tuple[:])

#changing tuple values
my_tuple=(4,2,3,[6,5])


#TypeError:"tuple" object does not support item assignment
#my_tuple[1]=9

#However item of mutable element can be changed
my_tuple[3][0] #output:(4,2,3,[9,5])

#tuple can bve reassigned
my_tuple=("p","r","o","g","r","a","m","i","z")

#output :("p","r","o","g","r","a","m","i","z")
print(my_tuple)