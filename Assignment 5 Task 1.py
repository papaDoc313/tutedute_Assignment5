Dictionary = {'Mark':78,'Alice':87,'David':83,'Ken':94}

Name = input("Enter the student's name: ")


if Name in Dictionary:
    print(Name,"'s marks: ",Dictionary[Name])
else:
    print("Student not found")