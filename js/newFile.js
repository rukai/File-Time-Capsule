function validateForm(){
    unixTime = $("#datetimeInput").data("DateTimePicker").getDate().unix();
    $("#datetimeInput").val(unixTime);
    return true;
}

$(function () {
    $('#datetimeInput').datetimepicker();
    $("#datetimeInput").data("DateTimePicker").show();
});
