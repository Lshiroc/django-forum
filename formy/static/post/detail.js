$(function() {
    let simplemde = new SimpleMDE({ element: $("#textEditor")[0] })

    $('.parse').each(function() {
        console.log("parsed")
        $(this).html(marked.parse(JSON.parse($(this).attr("data-content")).context))
    })

    $('#submitBtn').on('click', function() {
        console.log(JSON.stringify(simplemde.value()), $(location).attr('pathname') )
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
})