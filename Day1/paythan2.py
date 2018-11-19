#storing our age

age= input("enter your age>")
print("my age= {}".format(age))

if (age>=0 and age<1):
    print("infant")

elif(age>=1and age<18):
    print("child")
elif(age>=18 and age <60):
    print("adult")
else:
    print("senior citizen")




        


