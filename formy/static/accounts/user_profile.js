$(function() {
    $("#profileImage").on('mouseover', function() {
        $("#editHoverForm").css("display", "flex");
    })
    $("#profileImage").on('mouseout', function() {
        $("#editHoverForm").hide();
    })


    $('#fileSelect').on('change', function(e) {
        if(e.target.files.length) {
            let src = URL.createObjectURL(e.target.files[0]);
			let pic = $('#profilePicturePreview');
			$('#profilePicturePreview').attr('src', src);
			$('#profilePicturePreview').on('load', function() {
				pic.guillotine({width: 300, height: 300});
				$('#zoomIn').click(function() {
					pic.guillotine('zoomIn');
				});
				$('#zoomOut').click(function() {
					pic.guillotine('zoomOut');
				});
			
				// Crop the image based on data gotten from guillotine
				$('#saveImg').on('click', function() {
					let data = pic.guillotine('getData');
					$('#cropDetails').val(JSON.stringify(data));
					
					$('#editHoverForm').submit();
				});
			});
            
        } else {
            console.log("empty huh...")
        }
    })
})