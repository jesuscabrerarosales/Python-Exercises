text = 'This is a text'
number = 1234567890
number_01 = 1.234567890
bool = False
# NOT CHANGE THE VALUE IF THE VARIABLE IS UPPER
PI = 3.14

print(type(number_01))
print(text , number)

# List
print([1,1,1,1,])

# Tupla
print((1,2,3))

# Dictorionies
Dic = {
    "1" : "Name",
    "2" : "Last Name"

}
print(Dic.get('1'))

if(Dic.get('1')):
    print("Jesus")
    bool = True

print(Dic.get('2'))

if(Dic.get('2')):
    print("Cabrera")
    bool = True

if(bool):
    print("Ese fue tu nombre completo")
else:
    print("Error")