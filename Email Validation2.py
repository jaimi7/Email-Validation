import re
email=input("Enter Email ID : ")
condition="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
if re.search(condition,email):
    print("Right Email")
else:
    print("Wrong Email")