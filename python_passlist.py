from itertools import product

# پایه کلمات
base_words = ["name", "famly", "namefamly"]
numbers = ["", "123", "2024", "786"]
symbols = ["", "!", "@", "#", "$"]

# تولید ترکیب‌ها
with open("password_list.txt", "w") as file:
    for word in base_words:
        for num in numbers:
            for sym in symbols:
                file.write(f"{word}{num}{sym}\n")
                file.write(f"{word.capitalize()}{num}{sym}\n")
                file.write(f"{word.upper()}{num}{sym}\n")
