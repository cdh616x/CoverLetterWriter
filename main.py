list = ["Lucky", "Collin", "Sixes"]

print(list)

PLACEHOLDER = "[name]"

with open("company.txt") as letter_file:
    letter_contents = letter_file.read()
    for i in list:
        x = letter_contents.replace("[name]", i)
        print(f"{x}\n\n")
        with open(f"./output/{i}.txt", mode="a") as comp_letter:
            comp_letter.write(x)
