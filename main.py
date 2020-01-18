import eel

eel.init('web')

@eel.expose
def encrypt(USER_TXT,USER_KEY):
    ENCRYPTED_TXT=''
    TEMP_KEY=0
    KEY=0

    
    for char in USER_KEY:
        TEMP_KEY=TEMP_KEY+ord(char)
    print(TEMP_KEY)
    print(type(TEMP_KEY))
    
    while(TEMP_KEY!=0):
        KEY=KEY+TEMP_KEY%10
        TEMP_KEY=TEMP_KEY//10
    print(KEY)

    for char in USER_TXT:
        ENCRYPTED_TXT=ENCRYPTED_TXT+chr(ord(char)+int(KEY))
    return ENCRYPTED_TXT

@eel.expose
def decrypt(USER_TXT,USER_KEY):
    DECRYPTED_TXT=''
    TEMP_KEY=0
    KEY=0
    for char in USER_KEY:
        TEMP_KEY=TEMP_KEY+ord(char)
    print(TEMP_KEY)
    print(type(TEMP_KEY))
    
    while(TEMP_KEY!=0):
        KEY=KEY+TEMP_KEY%10
        TEMP_KEY=TEMP_KEY//10
    print(KEY)
    for char in USER_TXT:
        DECRYPTED_TXT=DECRYPTED_TXT+chr(ord(char)-KEY)
    return DECRYPTED_TXT

eel.start('index.html',size=(1000,600))