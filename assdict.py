#Use the get method to print the value of the "model" key of the car dictionary
#add the key/value pair "color": "red" to the car dictionary
#get()
car ={

    "brand": "Ford",
    "model": "Musting",
    "year": 1969
} 

print(car.get("model"))
car["color"] = "red"
car.pop("model")
print(car)