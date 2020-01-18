#Library for creating desktop application using web development tools
import eel

#Project folder that contins html, css, js files 
eel.init('web')

#Exposing encrypt function so that js can communicate with python 
@eel.expose
def encrypt(USER_TXT,USER_KEY):
    #Global
    ENCRYPTED_TXT=''
    TEMP_KEY=0
    KEY=0
    
    #Calculating temporary key
    for char in USER_KEY:
        TEMP_KEY=TEMP_KEY+ord(char)
    
    #Calculating the key for encrypting using temporary key
    while(TEMP_KEY!=0):
        KEY=KEY+TEMP_KEY%10
        TEMP_KEY=TEMP_KEY//10

    #Encrypting user text using the key
    for char in USER_TXT:
        ENCRYPTED_TXT=ENCRYPTED_TXT+chr(ord(char)+int(KEY))
    return ENCRYPTED_TXT

#Exposing decrypt function so that js can communicate with python 
@eel.expose
def decrypt(USER_TXT,USER_KEY):
    #Global
    DECRYPTED_TXT=''
    TEMP_KEY=0
    KEY=0

    #Calculating temporary key
    for char in USER_KEY:
        TEMP_KEY=TEMP_KEY+ord(char)
    
    #Calculating the key for decrypting using temporary key
    while(TEMP_KEY!=0):
        KEY=KEY+TEMP_KEY%10
        TEMP_KEY=TEMP_KEY//10
    
    #Decrypting user text using the key
    for char in USER_TXT:
        DECRYPTED_TXT=DECRYPTED_TXT+chr(ord(char)-KEY)
    return DECRYPTED_TXT

#Start eel from the index file
eel.start('index.html',size=(1000,600))
