# fahrenheit = celsius * 1.8 + 32
def ctof(c):
    return (c * 1.8) + 32
c = int(input("temperature in Celsius:"))
print(ctof(c))
def ftoc(f):
    return (f - 32) / 1.8
f = int(input("temperature in Fareinheight:"))
print(ftoc(f))
