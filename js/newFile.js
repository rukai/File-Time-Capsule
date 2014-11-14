function validateForm(){
    //Get date from datetime picker and store it in a hidden field
    unixTime = $("#datetimeInput").data("DateTimePicker").getDate().unix();
    $("#datetimeSubmit").val(unixTime);
    return true;
}

$(function () {
    //activates date time picker
    $('#datetimeInput').datetimepicker();
    $("#datetimeInput").data("DateTimePicker").show();
});
