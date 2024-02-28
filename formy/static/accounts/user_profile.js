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
					let canvas = document.createElement('canvas');
					let ctx = canvas.getContext('2d');
					
					canvas.width = data.w * data.scale;
					canvas.height = data.h * data.scale;
					ctx.drawImage(pic[0], data.x, data.y, data.w, data.h, 0, 0, data.w*data.scale, data.h*data.scale);
					let croppedImg = new Image();
					croppedImg.src = canvas.toDataURL();
					$('#test').append(croppedImg);
				});
			});
            
            // $('#editHoverForm').submit();
        } else {
            console.log("empty huh...")
        }
    })
})