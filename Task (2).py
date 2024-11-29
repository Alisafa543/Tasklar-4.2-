my_dict = {"Country" : "Azerbaijan" , "City" : "Baku" , "Village" : "Bine"}
secim = input("Daxil edin: ")
if secim == "1":
    k = list(my_dict.keys())
    print(k)
elif secim == "2":
    v = list(my_dict.values())
    print(v)
elif secim == "":
    print("Ad daxil etmediniz.")
else :
    print("Yanlis secim etdiniz.")