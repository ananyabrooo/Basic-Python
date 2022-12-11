d1=input("data1: ")
d2=input("data2: ")
l1=d1.split(",")
l2=d2.split(",")
dict1=dict(zip(l1,l2))
key=input("key: ")
if key in dict1:
    print("value:",dict1[key])
else:
    print("value:",dict1.get(key,"None"))
#value scan be repeated
#key should be unique, if the key is same then it'll fetch the last aka updated one.
    
    
