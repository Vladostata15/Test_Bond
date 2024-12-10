a = 10
b = 5
print(a)
for i in range (5):
    print(a+a)
if a > 10:
    print(a + b)

stations_in_israel = [
    "tel aviv savidor center",
    "jerusalem malha",
    "haifa center hashmona",
    "tel aviv hashalom",
    "tel aviv university",
    "ashdod ad halom",
    "afula",
    "beersheba merkaz",
    "netanya",
    "rishon lezion moshe dayan",
    "hadera west",
    "herzliya",
    "rehovot",
    "binyamina",
    "nahariya",
    "modiin",
    "kiryat shmona",
    "ramat gan",
    "beit shemesh",
    "bat yam yoseftal"
]
while True:
    start = input("You are starting from: ").lower()
    if start not in stations_in_israel:
        print("The name of the station is incorrect! Try again!")
    else:
        break

while True:
    finish = input("You are going to: ").lower()
    if finish not in stations_in_israel:
        print("The name of the station is incorrect! Try again!")
    else:
        break

perStation = 8
price = abs(stations_in_israel.index(finish) - stations_in_israel.index(start))*perStation

sum = 0
while sum < price:
    print("You need to pay more:", price-sum)
    pay = int(input("Enter the sum: "))
    sum+=pay
if sum>price:
    print("You have back:", sum-price)

print("Have a good trip!")




import time
while True:
    password = input("Enter the password: ")
    if len(password) != 4:
        print("Try again!")
    else:

        break
check = False
list = [0,0,0,0]
startTime = time.time()
for i in range (10):
    list[0] = i
    for _ in range(10):
        list[1] = _
        if password == (f"{list[0]}{list[1]}{list[2]}{list[3]}"):
            finishTime = time.time()
            check = True
            print("Your password is:",(f"{list[0]}{list[1]}{list[2]}{list[3]}"))
            break
        for _1 in range(10):
            list[2] = _1
            if password == (f"{list[0]}{list[1]}{list[2]}{list[3]}"):
                check = True
                print("Your password is:", (f"{list[0]}{list[1]}{list[2]}{list[3]}"))
                finishTime = time.time()
                break
            for _2 in range(10):
                list[3] = _2
                if password == (f"{list[0]}{list[1]}{list[2]}{list[3]}"):
                    check = True
                    print("Your password is:", (f"{list[0]}{list[1]}{list[2]}{list[3]}"))
                    finishTime = time.time()
                    break
    if check == True:
        break
print(f"It took to hack your password: {finishTime-startTime}s")
