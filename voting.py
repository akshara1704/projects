Garv16 = 0
Manya_Lipi = 0
Akshara11= 0
Muskani= 0
count = 0
a=0
while a != 1:
    choice = input("Enter G to vote on Garv16 , M to vote on Manya_Lipi , A to vote on Akshara11, MU for Muskani =")
    if choice == "G":
        print("YOU have votted on Garv16")
        Garv16 = Garv16 + 1
    print()
    if choice == "M":
        print("YOU have votted on Manya_Lipi")
        Manya_Lipi = Manya_Lipi + 1
    print()
    if choice == "A":
        print("YOU have votted on Akshara11")
        Akshara11 = Akshara11 + 1
    print()
    if choice == "MU":
        print("YOU have votted on Muskani")
        Muskani = Muskani + 1
    count = count + 1
    print()
    a = int(input("press 1 to end voting and 0 to continue="))
print()
print("Total votes that voters have given=", count)
print("votes for Garv16=", Garv16)
print("votes for Manya_Lipi=", Manya_Lipi)
print("votes for Muskani=", Muskani)
if Garv16 > Manya_Lipi and Garv16 > Akshara11 and Garv16 > Muskani:
    print("Garv won")
    winner=print("garv")
if Manya_Lipi > Garv16 and Manya_Lipi > Akshara11 and Manya_Lipi > Muskani:
    print("Lipi won")
if Akshara11 > Garv16 and Akshara11 > Manya_Lipi and Akshara11 > Muskani:
    print("Akshara won")
if Muskani > Garv16 and Muskani > Manya_Lipi and Muskani > Akshara11:
    print("Muskani won")