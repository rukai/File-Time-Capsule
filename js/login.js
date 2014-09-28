/*
Copyright 2014 Lucas Kent
Licenced under the GNU GPL V3
*/

function validateForm(){
    return validateUsername && validatePassword();
}

/*Check a username is entered*/
function validateUsername(){
    /*Grab data*/
    var usernameMessage = document.getElementById("username-message");
    var username = document.getElementById("username").value;

    /*Check*/
    if(username.length == 0){
        usernameMessage.innerHTML = "Please enter your usename here.";
        warningMessage(usernameMessage);
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
        passwordMessage.innerHTML = "Must contain more than 5 characters.";
        warningMessage(passwordMessage);
        return false
    }
    else{
        successMessage(passwordMessage);
        return true;
    }
}

/* Takes a message element and gives a success message with proper styling*/
function successMessage(messageElement){
    messageElement.style.visibility = "visible";
    messageElement.innerHTML = "All Good!";
    messageElement.classList.remove("text-warning");
    messageElement.classList.add("text-success");

    parrentElement = messageElement.parentNode;
    parrentElement.classList.remove("has-warning");
    parrentElement.classList.add("has-success");
}

/* Takes a message element and styles it for a warning message*/
function warningMessage(messageElement){
    messageElement.style.visibility = "visible";
    messageElement.classList.remove("text-success");
    messageElement.classList.add("text-warning");

    parrentElement = messageElement.parentNode;
    parrentElement.classList.remove("has-success");
    parrentElement.classList.add("has-warning");
}
