import configparser as cfgparse

KEY_SESSION = 97
KEY_USER = 17
KEY_OPEN = KEY_SESSION * KEY_USER
SAMPLE_TEXT = \
    "Я помню чудное мгновенье:\n" \
    "Передо мной явилась ты\n"    \
    "Как мимолётное видение\n"    \
    "Как гений чистой красоты"

def encrypt(text):
    ciphertext = ""
    key_padded = (str(KEY_OPEN) * (len(text) // len(str(KEY_OPEN)) + 1))[:len(text)]
    for i in range (len(text)):
        k = ord(text[i])
        enc = k ^ int(key_padded[i])
        ciphertext += str(chr(enc))
    
    return ciphertext

def save_to_file(text = ""):
    if text == "": 
        return 0
    s = encrypt(text)
    config_parser = cfgparse.ConfigParser()
    config_parser.add_section("main")
    config_parser.set("main", "public_key", str(KEY_OPEN))
    config_parser.set("main", "message", s)
    config_parser.write(open(".\\demo-06\\mess1.txtx", mode = "w", encoding = "utf-8"))
    #print(text)


if __name__ == "__main__":
    save_to_file(text = SAMPLE_TEXT)