/*
Copyright 2014 Lucas Kent
Licenced under the GNU GPL V3
*/

function validateForm(){
    return validateUsername() && validatePassword();
}

/*Check a username is entered*/
function validateUsername(){
    /*Grab data*/
    var usernameMessage = document.getElementById("username-message");
    var username = document.getElementById("username").value;

    /*Check*/
    if(username.length == 0){
        warningMessage(usernameMessage, "Please enter your usename here.");
        return false;
    }
    else{
        successMessage(usernameMessage);
        return true;
    }
}

/* Check password has more then 5 characters*/
function validatePassword(){
    /*Grab data*/
    var passwordMessage = document.getElementById("password-message");
    var password = document.getElementById("password").value;

    /*Check*/
    if(password.length < 6){
        warningMessage(passwordMessage, 'Needs more than 5 characters.');
        return false;
    }
    else{
        successMessage(passwordMessage);
        return true;
    }
}

