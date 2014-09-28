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

/* Takes a message element and gives a success message with appropriate styling*/
function successMessage(messageElement){
    messageElement.style.visibility = "visible";
    messageElement.innerHTML = '<span class="glyphicon glyphicon-ok"></span> All Good!';
    messageElement.classList.remove("text-warning");
    messageElement.classList.add("text-success");

    parrentElement = messageElement.parentNode;
    parrentElement.classList.remove("has-warning");
    parrentElement.classList.add("has-success");
}

/* Takes a message element and warning message, styling it appropiately*/
function warningMessage(messageElement, messageString){
    messageElement.innerHTML = '<span class="glyphicon glyphicon-warning-sign"></span> ' + messageString
    messageElement.style.visibility = "visible";
    messageElement.classList.remove("text-success");
    messageElement.classList.add("text-warning");

    parrentElement = messageElement.parentNode;
    parrentElement.classList.remove("has-success");
    parrentElement.classList.add("has-warning");
}
