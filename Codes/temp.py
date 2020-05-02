import json

fname = input("Enter a file Name: ")
file = open(fname).read()

js = json.loads(file)

for element in js:
    user = element[0]
    course = element[1]
    role = element[2]

    if user is None or course is None or role is None:continue

    print(user, course, role)
