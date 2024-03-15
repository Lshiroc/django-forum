let simplemde = new SimpleMDE({ element: $("#textEditor")[0] })
$(function() {
    console.log("detail.js loaded")
    
    
})
marked.setOptions({
    breaks: true,
    gfm: true,
})
$('.parse').each(function() {
    console.log("parsed")
    $(this).html(marked.parse(JSON.parse($(this).attr("data-content")).context).replaceAll(/\r\n|\r|\n/g, '<br />'))
})
$('#submitBtn').on('click', function() {
    console.log(JSON.stringify(simplemde.value()), $(location).attr('pathname'))
    console.log("submitteddd")
    $.ajax({
        type: "POST",
        url: $(location).attr('pathname'),
        headers: {
            'X-CSRFToken': $('input[name="csrfmiddlewaretoken"]').attr('value')
        },
        data: {
            context: JSON.stringify({context: simplemde.value()}),
        }
    })
})
