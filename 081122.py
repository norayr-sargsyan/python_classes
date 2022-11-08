import os

sum1 = 0
sum2 = 0
new_string = ""
with open(f"text_1.txt") as txt1:

    for line in txt1:
        for letter in line:
            if letter.isdigit():
                sum1 += int(letter)
                sum2 += 1
            else:
                new_string += letter
print(sum1)
print(sum2)

file_path = os.path.join(os.getcwd(), "text_2.txt")
with open(file_path, "a") as file:
    file.write(new_string)
