print('hello world')
# a = 10
# b = 20
# if a>b:
#     print('this is correct')
# else:
#     print('This  is incorrect ')


x=y=z = "hello"
print(x,y)

# print({1,2,3,4,5,1},type({1,2,3,4,5}))


string = "This is my string"
print(len(string))
# print(string[0:10])


'''reversing the string'''
print(string[::-1])


# reverse string
print(string[-3:-1])
print(string[-1::-2],'\n')
print(string[-4:-1])


print(string[0::2])
print(x[0::2])


a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"


b = a.replace('H','J')
print(b)

#split
splt = a.split(",")
print(splt)

#format string 
real = 'This is the value'
print(f'Python {real}')

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))




# form keys
x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)

print(thisdict)


#lambda function
function = lambda x: x**2

print(function(5))
