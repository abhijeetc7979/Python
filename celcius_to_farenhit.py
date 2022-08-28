#fahrenheit = celsius * 1.8 + 32

def ctof(c):
    return (c*1.8) + 32
c= int(input('temperature in Celsius:'))
print(ctof(c))


# int(input('temperature in Celsius:'))
#
# f = (c * 1.8) + 32
#
# print(f)

def ftoc(f):
    return (f-32)/1.8
f= int(input('temperature in Fareinheight:'))
print(ftoc(f))