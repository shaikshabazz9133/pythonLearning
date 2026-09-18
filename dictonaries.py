# A dictionary is an ordered collection of key-value pairs. Keys must be unique and immutable.

# di = {'apple': 15, 1: [1, 2, 3], 'set': 3}
# print(len(di))
# thekeys = di.keys()
# thevalues = di.values()
# print(thekeys)
# print(thevalues)
# print(di[1][1])

# 1. Creating a Dictionary
studentInfo = {
    "name": "shahid",
    "age": 22,
    "course": "Computer Science",
    "grades": [85, 90, 95]
}
print(f"Student Dictionary: {studentInfo}")

# 2. Accessing Values
print(f"Name (using brackets): {studentInfo['name']}")
print(f"Course (using get): {studentInfo.get('course')}")

# 3. Adding and Updating Key-Value Pairs
studentInfo["age"] = 23  # Updates existing key
studentInfo["city"] = "bangalore"  # Adds a new key-value pair
print(f"Updated Dictionary: {studentInfo}")

# 4. Removing Items
removedGrade = studentInfo.pop("grades")  # Removes key and returns its value
print(f"Removed item value: {removedGrade}")
print(f"After pop: {studentInfo}")

# popitem() removes the last inserted item
lastItem = studentInfo.popitem()
print(f"Popped last item: {lastItem}")

# 5. Dictionary Methods (Keys, Values, Items)
personInfo = {"name": "shahid", "age": 22, "job": "Engineer"}

print(f"Keys: {personInfo.keys()}")
print(f"Values: {personInfo.values()}")
print(f"Items (Key-Value pairs): {personInfo.items()}")

# 6. Looping through a Dictionary
print("\nLooping through dictionary:")
for dictKey, dictValue in personInfo.items():
    print(f"{dictKey} -> {dictValue}")
