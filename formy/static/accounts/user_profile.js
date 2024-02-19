$(function() {
    $("#profileImage").on('mouseover', function() {
        $("#editHover").css("display", "flex");
    })
    $("#profileImage").on('mouseout', function() {
        $("#editHover").hide();
    })
})