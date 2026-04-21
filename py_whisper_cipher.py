def whisper_cipher(text: str, shift: int) -> str:
    result = ""

    for char in text:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
        else:
            result += char
    return result
