$(function() {
    $("#profileImage").on('mouseover', function() {
        $("#editHoverForm").css("display", "flex");
    })
    $("#profileImage").on('mouseout', function() {
        $("#editHoverForm").hide();
    })

    $('#fileSelect').on('change', function(e) {
        console.log("changed", e.target.files.length);
        if(e.target.files.length) {
            let src = URL.createObjectURL(e.target.files[0]);
            $('#profilePicturePreview').attr('src', src);
            
            // $('#editHoverForm').submit();
        } else {
            console.log("empty huh...")
        }
    })
})