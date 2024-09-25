##[]
#len()
#list()
#in
#insert
#append
#extend
#remove()
#pop()
#del
#clear()

thislist = ["apple", "banana", "chery","orange","kiwi","melon","mango"]
thislist2 = ["marter", "marker", "marry"]
thistuple = ("maint", "tolu")
print(thislist[ -4:-1])

if "apple" in thislist:
    print(f"yes, 'apple' is in this {thislist}")

##to change item on the list

thislist[2:4] = ["fig","mouse"]
print(len(thislist))


###add items

thislist.insert(2, "merger")

thislist.append("carlog")

thislist.extend(thistuple)
thislist.remove("mango")
thislist.pop()

del thislist[-1] # removes the last of the list
del thislist # to delete the entire list

thislist.clear()
#looping to our list
#range for loop
#len() for loop
#while loop
#list comprehension

[print(x) for x in thislist]

thislist = ["apple", "banana", "cherry"]

i=0

while i<len(thislist):
    print(thislist(i))
    i= 1 + i

for x in range(len(thislist)): #x is every item of the list
    print(thislist[x])


