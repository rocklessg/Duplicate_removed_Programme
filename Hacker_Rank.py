def name(char):
    while True:
        if len(char) < 3:
            print("Name must be at least three character long")
        elif len(char) > 50:
            print("Name can be maximum of 50 character long")
        else:
            print("Name looks good!")


char = input("Enter your Name: ")
count = 0
while count <= 5:
    if len(char) < 3:
        print("Name must be at least three character long")
        break
    elif len(char) > 50:
        print("Name can be maximum of 50 character long")
        break
    else:
        print("Name looks good!")
        break
