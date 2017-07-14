import cs50

count = 0;
print("How much change is owed? ")
change = cs50.get_float()

while change < 0:
    print("Retry: ", end="")
    change = cs50.get_float()

change = change*100
change = round(change)

while change >= 25:
    count = count + 1
    change = change - 25
while change >= 10:
    count = count + 1
    change = change - 10
while change >= 5:
    count = count + 1
    change = change - 5
if change > 0:
    count = count + change

print("{}".format(count))
    