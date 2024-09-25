mytuple = ("apple","banana", "cherry")

print(mytuple)

#len()
print(mytuple[0:3])

#if statement

if "apple" in mytuple:
    print('yes, "apple" is in the fruit')
#tuple are unchangeable

y = list(mytuple)
y.append("glory")
mytuple = tuple(y)
print(mytuple)

#unpacking of tuples
(green, yellow, red, brown) = mytuple

print(mytuple)
print(green)

#for
#while
#for in

for x in mytuple:
    print(x)

for x in range(len(mytuple)):
    print(mytuple[x])
