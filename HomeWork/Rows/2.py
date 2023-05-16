text = input("Введіть текст: ")

reserved_words = input("Введіть список зарезервованих слів через кому: ").split(",")

for word in reserved_words:

   text = text.replace(word.strip(), word.strip().upper())

print("Змінений текст:")

print(text)