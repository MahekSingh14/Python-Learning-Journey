# Dictionary Basic

student={
    "name": "Mahek Singh",
    "city": "Mau",
    "age": 20,
}
print(type(student))
print(student["name"])
print(student)

# for update
student["city"]= "Indore"
print(student)
student["country"]= "India"
print(student)

# for removing
student.pop("country")
print(student)
print(student.values())
print(student.keys())
print(student.items())
print(student.get("name"))
