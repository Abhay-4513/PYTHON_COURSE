d = {} # This is the empty dictionary ....

dict_n = {
    "Key":"Value",
    "John":90,
    "Marry":80,
    "Roman":70,
}

print(dict_n["John"]) # This will give the value of the key..

print(dict_n.keys())
print(dict_n.values())
dict_n.get("Rohan") # In .get method if the key is not there in dictionary it will print "None"
# print(dict_n["Ramesh"]) While this one gives the error if there is no such key in the dictionary..

print(dict_n.update({"Abhay":100,"John":95})) # Update method is used to change the value of the keys or adding a new key in the dictionary..
print(dict_n)
