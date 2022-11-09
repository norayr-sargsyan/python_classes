import os

# 1

# sum1 = 0
# sum2 = 0
# new_dict = {}
# path = "text_1.txt"
# with open(path, "r") as txt1:
#     for line in txt1:
#         sum1 += 1
#         for letter in line:
#             if letter.isdigit():
#                 sum2 += 1
#         new_dict[sum1] = sum2
#         sum2 = 0
#
# print(new_dict)

# 2

# sum1 = 0
# sum2 = 0
# new_dict = {}
# path = "text_1.txt"
# with open(path, "r") as txt1:
#     for line in txt1:
#         sum1 += 1
#         for letter in line:
#             if letter.isdigit():
#                 sum2 += int(letter)
#         new_dict[sum1] = sum2
#         sum2 = 0
#
# print(new_dict)

# 3

# dict_sps_word = []
# path = "text_1.txt"
# with open(path, "r") as txt1:
#     list1 = txt1.read().split()
#     for word1 in list1:
#         if word1.startswith("<<") and word1.endswith(">>"):
#             dict_sps_word.append(word1)
# print(dict_sps_word)
#
# 4

# new_string = ""
# path = "text_1.txt"
# with open(path, "r") as txt1:
#     for line in txt1:
#         for letter in line:
#             if not letter.isdigit():
#                 new_string += letter
#
#
# file_path = os.path.join(os.getcwd(), "text_2.txt")
# with open(file_path, "a") as file:
#     file.write(new_string)
