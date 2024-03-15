let tagContainer = $("#tagContainer");
let tags = [];
let simplemde = new SimpleMDE({ element: $('#contextEditor')[0] })

$(function() {
})
$('#tagInput').on('keydown', function(e) {
    if(e.keyCode == 32 && !e.target.value.trim().includes('\\') && e.target.value.trim().length > 0) {
        let value = e.target.value.trim();
        let newTag = $(`<span id="tag" class="py-1 px-2 flex items-center space-x-2 bg-green-200">
                            <span id="value">${value}</span>
                            <div id="removeTag" class="w-4 h-4 rounded-sm flex justify-center items-center bg-green-400 text-sm "><i class="fa-solid fa-xmark"></i></div>
                        </span>`);
        tagContainer.append(newTag);
        tags.push(value);
        $('#hiddenfield').val(JSON.stringify({tags}));
        e.target.value = "";
    }
})

$('#submitBtn').on('click', function() {
    console.log("submitteddd")
    $.ajax({
        type: "POST",
        url: $(location).attr('pathname'),
        headers: {
            'X-CSRFToken': $('input[name="csrfmiddlewaretoken"]').attr('value')
        },
        data: {
            title: $('#titleInput').val(),
            tags: $('#hiddenfield').val(),
            context: JSON.stringify({context: simplemde.value()}),
        }
    })
})

$(document).on('click', '#removeTag', function() {
    let tagValue = $(this).closest('#tag').find('#value').text();
    tags = tags.filter(tag => tag != tagValue);
    $(this).closest('#tag').remove();
})
