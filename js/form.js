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
