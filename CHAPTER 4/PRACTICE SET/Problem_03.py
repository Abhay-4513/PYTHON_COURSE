# Check that a tuple type cannot be changed in python 

a = (1,2,"James")

a[2] = "Jems"
#    a[2] = "Jems"
#    ~^^^
#TypeError: 'tuple' object does not support item assignment
# This will be error......
print(a)