name=input("Enter the name of student :")
marks=int(input("Enter the marks of student :"))
grade=None
if marks <= 30 :
    grade="Fail"
elif marks >= 31 and marks <= 50 :
     grade="E"
elif marks >= 51 and marks <= 60 :
    grade="D"
elif marks >= 61 and marks <= 70:
    grade="C"
elif marks >= 71 and marks <= 80 :
    grade="B"
elif marks >= 81 and marks <= 90 :
    grade="A"
elif marks >= 91 and marks <= 100 :
    grade="A++"

else :
    print("Inavild input")

print(f"The Grade of {name} for {marks} marks is {grade}.")

