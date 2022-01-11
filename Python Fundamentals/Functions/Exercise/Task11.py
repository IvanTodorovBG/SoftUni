

def loading_bar(load):
    if load == 0:
        print("0% [..........]\nStill loading...")
    elif load == 10:
        print("10% [%.........]\nStill loading...")
    elif load == 20:
        print("20% [%%........]\nStill loading...")
    elif load == 30:
        print("30% [%%%.......]\nStill loading...")
    elif load == 40:
        print("40% [%%%%......]\nStill loading...")
    elif load == 50:
        print("50% [%%%%%.....]\nStill loading...")
    elif load == 60:
        print("60% [%%%%%%....]\nStill loading...")
    elif load == 70:
        print("70% [%%%%%%%...]\nStill loading...")
    elif load == 80:
        print("80% [%%%%%%%%..]\nStill loading...")
    elif load == 90:
        print("90% [%%%%%%%%%.]\nStill loading...")
    elif load == 100:
        print("100% Complete!\n[%%%%%%%%%%]")


loading_bar(int(input()))
