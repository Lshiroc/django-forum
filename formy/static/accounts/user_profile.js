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

    function handle_mousedown(e) {
        window.my_dragging = {};
        my_dragging.pageX0 = e.pageX;
        my_dragging.pageY0 = e.pageY;
        my_dragging.elem = this;
        my_dragging.offset0 = $(this).offset();
        console.log("ehm1");

        function handle_dragging(e) {
            let left = my_dragging.offset0.left + (e.pageX - my_dragging.pageX0);
            let top = my_dragging.offset0.top + (e.pageY - my_dragging.pageY0);
            $(my_dragging.elem).offset({top: top, left: left});
        }

        function handle_mouseup(e) {
            $('body')
            .off('mousemove', handle_dragging)
            .off('mouseup', handle_mouseup);
        }

        $('body')
        .on('mouseup', handle_mouseup)
        .on('mousemove', handle_dragging);
    }

    $('#draggerSquare').mousedown(handle_mousedown)
    $('#profilePicturePreview').mousedown(handle_mousedown)

    $('#imageZoomIn').on(function() {
        console.log("well")
        $('#profilePicturePreview').css('transform', 'scale(1.2)');
    })
    
    $('#imageZoomOut').on(function() {
        $('#profilePicturePreview').css('transform', 'scale(0.8)');
    })

})