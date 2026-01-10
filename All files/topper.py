n = int(input("Number of students : "))
studs = []
for i in range(n):
    roll=int(input('Enter roll number : '))
    name = input('Enter name : ')
    marks = float(input('Enter marks : '))
    studs.append((roll,name,marks))
    max = 0
for s in studs:
    if s[2]>max:
        max = s[2]
        topper = s[1]
print('Topper is : ',topper)