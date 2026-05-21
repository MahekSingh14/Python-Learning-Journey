# Practice Question 2
# You are given a list of programming languages:
# ["Python", "Java", "C++", "Python", "Java", "C"]
# Convert it into a set and print how many unique languages Divya knows.

programmingList=["Python", "Java", "C++", "Python", "Java", "C"]
print(type(programmingList))

# convert a list into list
programmiSet=set(programmingList)
print(type(programmiSet))
print("Enter Divya knows unique language : ",len(programmiSet))