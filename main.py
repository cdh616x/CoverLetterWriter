with open("company.txt", mode="r") as f:
    read = (f.read())
    print(read)
    with open("lucky.txt", mode="a") as f:
        x = input("What word would you like to replace?")
        y = input("What would would you like to replace it with?")
        z = input("What file name would you like to save it under?")
        new_read = read.replace(x, y)
        with open(f"{z}.txt", mode="w") as f:
            f.write(new_read)
