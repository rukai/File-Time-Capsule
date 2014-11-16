//Calls all validation methods to ensure new file form is valid
function validateForm(){
    //order ensures first element is checked first
    return validateFile() && validateDate() && setDateSubmit() && validateComment();
}

//Get date from datetime picker and store it in a hidden field
function setDateSubmit(){
    unixTime = $("#datetimeInput").data("DateTimePicker").getDate().unix();
    $("#datetimeSubmit").val(unixTime);
    return true;
}

//Ensures date chosen by the user is valid
function validateDate(){
    dateMessage = $("#date-message")[0];

    date = $("#datetimeInput").data("DateTimePicker").getDate();
    if(date == null){
        warningMessage(dateMessage, "Invalid date")
        return false;
    }

    //succeed
    successMessage(dateMessage);
    return true;
}

//Ensures file chosen by the user is valid
function validateFile(){
    //grab files
    fileMessage = $("#file-message")[0];
    files = $('[name="file"]')[0].files;

    //Check file is selected
    if (files.length == 0){
        warningMessage(fileMessage, "No file selected.");
        return false;
    }

    //get size in MB
    size = (files[0].size / 1024) / 1024;
    
    //check file > 10 MB
    if(size > 10){
        warningMessage(fileMessage, "Must be less then 10 MB.")// maybe say "currently x MB?"
        return false;
    }

    //Succeed
    successMessage(fileMessage);
    return true;
}

//Ensures comment chosen by the user is valid
function validateComment(){
    commentMessage = $("#comment-message")[0];
    successMessage(commentMessage);
    return true;
}

//activates date time picker
$(function () {
    $('#datetimeInput').datetimepicker();
    $("#datetimeInput").data("DateTimePicker").show();
});
