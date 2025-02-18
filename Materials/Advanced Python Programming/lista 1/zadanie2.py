import string

def is_palindrom(text):
    text = text.translate(str.maketrans('', '', string.punctuation)).replace(" ", "").lower()
    
    if text == text[::-1]:
        return True
    else:
        return False
    
print(is_palindrom("Eine güldne, gute Tugend: Lüge nie!"))
print(is_palindrom("Míč omočím."))
print(is_palindrom("kajak . kajak / ? kajak"))