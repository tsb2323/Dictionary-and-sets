#dictionaries are used to store data values in key:value pairs
#dictionaries are unordered, changeable and indexed
#dictionary["key"]="value"

info={
    "name":"tanvir",
    "age": 22,
    "male": True,
    "subject": ["phthon","java","c"]
    #lists and tuples can also be stored

}
print(info)

#dict["key"]="value"
print(info["name"])
info["name"]="tsb"
print(info)

null_dict={

}
null_dict["23"]="13.7"
print(null_dict)

#nested dictionary
student={
    "name":"tanvir",
    "marks":{
        "m":90,
        "t":30,
    }
}
print(student)

#dicctionary methods
print(list(info.keys()))#return all the keys #typecasted in lists
print(info.values())#return all the values
print(info.items())#return all the key and value paired in tuples
pair=list(info.items())
print(pair[1])

print(info.get("name"))#return the value of key #we can also use info["name"] but if the key is not present it will give error but get will return n

print(info.update({"laptop":"galaxy book"}))
print(info)

#set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
#set={1,2,2,1} it will be stored as {1,2 }because duplicate value not allowed
#list and dictionary can't be stored in set as they are mutable

set={1,2,2,3,4,4,4,4,4,"t","s","j","b"}
print(type(set))
print(set)

#emptyset={} wrong because it is symbole of empty dictionary
#emptyset=set() correct way to declare empty set

#set methods
set.add("z")#add element in set
#add last element in sset
print(set)
set.remove(2)#remove 2 from set
print(set)
print(set.pop())#print any random element from set
set.clear()#clear the set
print(set)

#union and intersection same as maths
set2={33,44,55,11}
set3={10,20,30,11}
set3.union(set2)#return new set with both set and set 2
print(set3.union(set2))
print(set3.intersection(set2))#return common elements
