#list
dogs = [ "Ronger", "omi", "Turjoy Omi"]
print(sorted(dogs,key = str.lower))
print(dogs)

#tuples
names = ("Turjoy", "Islam", "Omi")
names[-1]
names.index("Omi")
len(names)
print(sorted(names))

dictionary
name = {"name": "Turjoy", "age": 23}
print(name.pop("name"))
print(name)
print(list(name.keys()))

# sets
set1 = {"Turjoy", "Omi"}
set2 = {"Omiss"}
mod = set1 | set2
print(mod)