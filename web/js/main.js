

function enctxt(){
    var USER_TEXT=document.getElementById('userTxt').value
    var USER_KEY=document.getElementById('userKey').value

    if(USER_TEXT!='' && USER_KEY!=''){
        eel.encrypt(USER_TEXT,USER_KEY)(
            function(ENCRYPTED_TXT){
                document.getElementById('output').innerHTML=ENCRYPTED_TXT
            }
        )
    }
    else{
        document.getElementById('output').innerHTML='Encrypt Your Text...'
    }
   
    
}

function detxt(){
    var USER_TEXT=document.getElementById('userTxt').value
    var USER_KEY=document.getElementById('userKey').value

    if(USER_TEXT!='' && USER_KEY!=''){
        eel.decrypt(USER_TEXT,USER_KEY)(
            function(DECRYPTED_TXT){
                document.getElementById('output').innerHTML=DECRYPTED_TXT
            }
        )
    }
    else{
        document.getElementById('output').innerHTML='Encrypt Your Text...'
    }
}

    


