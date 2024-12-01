import string
text = input("Введіть рядок: ")

clean_text = ""
for char in text:
    if char not in string.punctuation:
        clean_text += char

words = clean_text.split()

new_words = []
for word in words:
    new_words.append(word.capitalize())

hashtag = "#" + "".join(new_words)

if len(hashtag) > 140:
    hashtag = hashtag[:140]

print(hashtag)
