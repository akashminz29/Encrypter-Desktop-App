#Library for creating desktop application using web development tools
import eel

#Project folder that contins html, css, js files 
eel.init('web')

#Exposing encrypt function so that js can communicate with python 

def createKey(USER_KEY):
    TEMP_KEY=0
    KEY=0
    for char in USER_KEY:
        TEMP_KEY=TEMP_KEY+ord(char)
    
    #Calculating the key for encrypting using temporary key
    while(TEMP_KEY!=0):
        KEY=KEY+TEMP_KEY%10
        TEMP_KEY=TEMP_KEY//10
    return KEY

@eel.expose
def encrypt(USER_TXT,USER_KEY):
    #Global variable 
    ENCRYPTED_TXT=''
    
    #Encrypting user text using the key
    for char in USER_TXT:
        ENCRYPTED_TXT=ENCRYPTED_TXT+chr(ord(char)+createKey(USER_KEY))
    return ENCRYPTED_TXT

#Exposing decrypt function so that js can communicate with python 
@eel.expose
def decrypt(USER_TXT,USER_KEY):
    #Global Variables
    DECRYPTED_TXT=''

    #Decrypting user text using the key
    for char in USER_TXT:
        DECRYPTED_TXT=DECRYPTED_TXT+chr(ord(char)-createKey(USER_KEY))
    return DECRYPTED_TXT

#Start eel from the index file
eel.start('index.html',size=(1000,600))
