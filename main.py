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
