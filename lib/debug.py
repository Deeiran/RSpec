
# # def get_most_common_letter(text):
# #     counter = {}
# #     letters = text.replace(" ","")
# #     for char in letters:

# #         counter[char] = counter.get(char, 0) + 1
# #         print(f" {char} - {counter[char]}")


# #     letter = sorted(counter.items(), key=lambda item: item[1],reverse=True)[0][0]

# #     print(letter)

# # get_most_common_letter("the roof, the roof, the roof is on fire!")


# # print(f"""
# # Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
# # Expected: o
# # Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
# # """)
# # def factorial(n):
# #     if n == 0:
# #         return 1
# #     else:
# #         return n * factorial(n - 1)
# # factorial(5)
# # print('factorial')
# # print (factorial(5))
# # data = [(2, 5), (5, 9), (2, 4), (2,9)]
# # sorted_data = sorted(data, key=lambda x:(x[0],x[1]),reverse=True)
# # print(sorted_data)  # Output: [(1, 5), (2, 7), (3, 9)]


# # data = [(3, 9), (1, 5), (2, 7)]
# # sorted_data = sorted(data, key=lambda x: x[1],reverse = True)
# # print(sorted_data)  # Output: [(1, 5), (2, 7), (3, 9)]

# # class Reminder():
# #     def __init__(self,name):
# #         self.name = name

# #     def remind_me_to(self,task):
# #         self.task = task
    
# #     def remind(self):
# #         return f"{self.name}, {self.task}"

# # reminder = Reminder("senthu")
# # reminder.remind_me_to ("walk the dog")
# # print (reminder.remind())

# def encode(text, key):
#     cipher = make_cipher(key)

#     ciphertext_chars = []
#     for i in text:
#         ciphered_char = chr(65 + cipher.index(i))
#         ciphertext_chars.append(ciphered_char)

#     return "".join(ciphertext_chars)


# def decode(encrypted, key):
#     cipher = make_cipher(key)

#     plaintext_chars = []
#     for i in encrypted:
#         plain_char = cipher[65 - ord(i)]
#         plaintext_chars.append(plain_char)

#     return "".join(plaintext_chars)


# def make_cipher(key):
#     alphabet = [chr(i + 97) for i in range(0, 26)]
#     cipher_with_duplicates = list(key) + alphabet

#     cipher = []
#     for i in range(0, len(cipher_with_duplicates)):
#         if cipher_with_duplicates[i] not in cipher_with_duplicates[:i]:
#             cipher.append(cipher_with_duplicates[i])

#     return cipher

# # When you run this file, these next lines will show you the expected
# # and actual outputs of the functions above.
# print(f"""Running: encode("theswiftfoxjumpedoverthelazydog", "secretkey")
# Expected: EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL
# Actual: {encode('theswiftfoxjumpedoverthelazydog', 'secretkey')}
# """)
# print(f"""
# Running: decode("EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL", "secretkey")
# Expected: theswiftfoxjumpedoverthelazydog
# Actual: {decode('EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL', 'secretkey')}
# """)
class Gratitudes():
    def __init__(self):     
        self.list = []
    
    def add(self, gratitude):
        self.list.append(gratitude)

    def format(self):
            gratitudes_string = ""
            for gratitude in self.list[:-1]:
                gratitudes_string += gratitude + ", "
            gratitudes_string += f"and {self.list[-1]}"
            return f"I am greatful for: {gratitudes_string}."