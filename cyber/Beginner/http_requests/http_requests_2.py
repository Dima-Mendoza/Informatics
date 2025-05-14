with open("data.txt", "r") as file:
    content = file.read()

with open("copy_data.txt", "w") as file:
    file.write(content)