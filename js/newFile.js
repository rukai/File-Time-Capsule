//Calls all validation methods to ensure new file form is valid
function validateForm(){
    return validateDate() && setDateSubmit() && validateFile() && validateComment();
}

//Get date from datetime picker and store it in a hidden field
function setDateSubmit(){
    unixTime = $("#datetimeInput").data("DateTimePicker").getDate().unix();
    $("#datetimeSubmit").val(unixTime);
    return true;
}

//Ensures date chosen by the user is valid
function validateDate(){
    return true;
}

//Ensures file chosen by the user is valid
function validateFile(){
    file = $('[name="file"]')[0];
    filename = file.value;
    //get size in MB
    size = (file.size / 1024) / 1024;
    
    if (filename == ""){//No file selected
        return false;
    }
    else if(size > 10){//file > 10 MB
        return false;
    }
    else{
        return true;
    }
}

//Ensures comment chosen by the user is valid
function validateComment(){
    return true;
}

//activates date time picker
$(function () {
    $('#datetimeInput').datetimepicker();
    $("#datetimeInput").data("DateTimePicker").show();
});
