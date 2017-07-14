import cs50

print("height: ", end="")
num = cs50.get_int()

while num > 23 or num < 0:
    print("Retry: ", end="")
    num = cs50.get_int()


for i in range(num):
    for j in range(num-i-1):
        print(" ", end="")
    for k in range(i+2):
        print("#", end="")
    print("")
 
    
