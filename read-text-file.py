file = open("lorem.txt", "r")
lorem = file.read()

print(lorem)

file.close()

with open("lorem.txt", "r") as file:
    print(file.read())

with open("lorem.txt", "w") as file:
    file.write("Voici du texte qui va effacer le lorem ipsum !")

with open("lorem.txt", "r") as file:
    print(file.read())

with open("lorem.txt", "w") as file:
    file.writelines(["Alexane\n", "Philippine\n", "Rim\n"])

with open("lorem.txt", "r") as file:
    for first_name in file:
        if first_name == "Thomas\n" or first_name == "Timothée\n":
            print(f"{first_name} est un garçon")
        else:
            print(f"{first_name} est une fille")
            
with open("lorem.txt", "r") as file:
    print(file.read(7))