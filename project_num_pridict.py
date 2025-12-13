import random
gusse = random.randint(1,100)
print(gusse)



a = -1
n = 0

while(a != gusse):
    n += 1
    a = int(input("Gusse a number.."))
    
    if(a>gusse):
        print("Please Gusse a smaller number..")
    elif(a<gusse):
        print("Please Gusse a greater number")

print(f"Correct Gusse in {n} attempt. Your number is {gusse}")        