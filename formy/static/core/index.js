$(function() {
    // adds how long ago post was posted via moment.js
    $('.postTimeHidden').each(function() {
        let date = $(this).text();
        let longAgo = moment.utc(date, "MMM. DD, YYYY, h:mm a").local().fromNow();
        $(this).closest('.additionalData').find('.postTime').text(longAgo)
    })
})