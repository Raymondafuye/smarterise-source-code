#get()
#keys()
#items()
#in
#pop
#popitem() removes random item
#del()
#clear



thisdic = {
    "brand": "ford",
    "model": "Mustring",
    "year" : 1964,
    "colors" : ["red", "white", "blue"]
    }

print(thisdic["colors"])

thisdic2 = dict(name="ray")

x = thisdic.get("model")

x = {...}

x = thisdic.keys()
y = thisdic.values()
print(x)

thisdic["favourite"] = "power"

print(x)
print(y)

m = thisdic.items()

print(m)

if "model" in thisdic:
    print("yes, 'model' is one of the keys in disctionary")

#thisdic.pop("model")
#print(thisdic)

thisdic.popitem()
print(thisdic)

#del thisdic("model")

#print(thisdic)

#for loop

#items()

for x in thisdic.values():
    print(x)
for x, y in thisdic.items():
    print(x,y)

mydict = thisdic.copy()
print(mydict)
