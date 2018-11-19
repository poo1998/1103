import random
secret_number = random.randint (9,10)
while (True):
      guess = input("guess a number between 9 and 10>")
      if(guess == secret_number):
        print("player high and computer wins")
        break
else:
    print("player high and computer wins")
    print("computer genrate = {}".format(secret_number))
    if(secret_number>guess):
        print ("computer is high computer to player")
    else:
        print("player number is comare to computer")



