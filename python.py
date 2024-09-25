myset = {"apple","banana", "cherry", True, 1, 2}
thisset = set(("apple","banana","cherry"))
print(thisset)

myset.add("orange")

print(myset)

#update

tropical = {"pineaple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

#discard()
#remove()

set1 = {"a","b","c"}

set2 = {1,2,1}

set3 = set1.union(set2)

print(set3)

#clear()
#copy
#difference

#check if "apple" is present in the fruits set
fruits = {"apple", "banana", "cherry"}

if "apple" in fruits:
    print('yes "apple" is present')

