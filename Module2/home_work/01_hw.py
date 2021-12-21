n = int(input("шоколадки размером n "))
m = int(input("шоколадки размером m "))
k = int(input("долек отломить k "))


if k%n==0 or k%m==0:
    print("YES")
else:
    print("No")
