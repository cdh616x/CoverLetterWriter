def create_new_coverletter(params):
    list = [f"{params}"]
    with open("company.txt") as letter_file:
        letter_contents = letter_file.read()
        company = input("What company are you sending this application to?")
        if company == "":
            print("Need company name; try again!")
            quit()
        for i in list:
            x = letter_contents.replace("[company_name]", company)
            with open(f"./output/{i}_cover_letter.txt", mode="w") as comp_letter:
                comp_letter.write(x)


def replace_position(params, file):
    with open(f"{file}") as letter_file:
        letter_contents = letter_file.read()
        x = letter_contents.replace("[open_position]", params)
        with open(f"{file}", mode="w") as pos_letter:
            pos_letter.write(x)


subject = str(input("What would you like to prefix the file's name with?"))
create_new_coverletter(subject)

position_title = str(input("What is the name of the position you are applying for?"))

if position_title == "":
    print("Need position name; try again!")
    quit()

file_name = str(input("What is the name of the file? (*prefix*_cover_letter") + "_cover_letter.txt")
if file_name == "":
    print("Need file name; try again!")
    quit()

replace_position(position_title, "./output/" + file_name)
