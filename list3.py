fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

# for x in fruits:
#     if "a" in x:
#         newlist.append(x)


  
newlist = [x for x in fruits if "a" in x]
newlist2 = [x for x in fruits if x != "apple"]
print(newlist)
print(newlist2)

numer = [y for y in range(10) if y<5]
print(numer)

