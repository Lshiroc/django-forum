$(function() {
    let simplemde = new SimpleMDE({ element: $("#textEditor")[0] })

    $('.parse').each(function() {
        console.log("parsed")
        $(this).html(marked.parse($(this).attr("data-content")))
    })
})