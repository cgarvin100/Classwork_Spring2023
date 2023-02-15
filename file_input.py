in_file = open("input_data.txt")

fruits = in_file.readlines()
print(fruits)
in_file.close()
print(fruits)

in_file = open("input_data.txt", "r")
first_line = in_file.readline()
print(first_line.strip("\n"))
in_file.close()


