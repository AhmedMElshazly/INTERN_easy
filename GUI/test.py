path = r"C:\Users\Ahmed Mohamed\Desktop\INTERN_easy\test.xlsx"

temp = str()
for id, char in enumerate(path):
    if char == "\\":
        Id = id
path = path[:Id+1]

print(path)
