def message_security():
    import random
    import string
    chars=" " + string.digits + string.ascii_letters + string.punctuation
    chars=list(chars)
    keys=chars.copy()
    random.shuffle(keys)

    mess =input("enter a plain text: ")
    cipher=""
    for letters in mess:
        index=chars.index(letters)
        cipher+=keys[index]
        continue
    print(f"cipher text is:{cipher}")

    cipher=input("enter cipher text here:")
    mess=""
    for letters in cipher:
        index=keys.index(letters)
        mess+=chars[index]
    print(f"plain text is:{mess}")
message_security()

