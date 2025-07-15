#string formatting kibhabe korte hoy
num1 = 230
num2 = 30
print(f"this is my super number {num1 + num2}")

username = "sahil"
print(f"my name is {username}")

#binary type data

list = [1,2,3,4,5,6,7,8,9,10,121,230];

b= bytes(list)
print(type (b))

#binary type data (byteArray)
list1 = [1,2,3,4,5,6,7,8,9,10,121,240];
b1 = bytearray(list1)
b1[2]= 200
print(b1 [2])

#none type data

g = None
print(type(g))

#sequence type data (list)
list2 = ['apple', 'orange' , 'tuntuni' , 'digital' , 'gg buffon']
list2[0] = 'sahil'
print(list2)

#sequence type data (tuple)

li = ('apple', 'meghbalika' , 'kaka', 'buffon')
print(li)

#sequence type data (range)
ran = range(200)
for i in ran:
    print(i)
#operator
#plus
x = 30
x1 = 40
print(x + x1)
#minus
x = 30
x1 = 40
print(x - x1)
#multiplications
x = 30
x1 = 40
print(x * x1)
#divison
x = 2
x1 = 2
print(x / x1)
#modulus %
x = 30
x1 = 40
print(x % x1)

x = 5
x1 = 3
print(x ** x1)

#swapping
c= 50
t = 60
c,t = t,c
print("this is value is now t", t)
print("this is value is now c", c)