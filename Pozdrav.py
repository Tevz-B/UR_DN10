oseba = " Študent "

dolzina = 10
for i in range(dolzina):
    if i == 2:
        print(f"{' Pozdrav ':*^20}")
    if i == 5:
        print(f"{oseba:*^20}")
    else:
        print(f"{'':*^20}")
