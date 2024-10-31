# formatted string 

name = 'Johnny'
age = 55

#print('hi ' + name + '. You are ' + str(age) + ' years Old ')
print(f'hi {name}. You are {age} years old') # f string Prefered
print('hi {new_name}. You are {age} years old'.format(new_name="GD", age = 20))