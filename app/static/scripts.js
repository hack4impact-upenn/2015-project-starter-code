$(document).ready(function() {
    $('button').on('click', function() {
        $.ajax({
            url: '/color',
            type: 'GET',
            dataType: 'text',
            contentType: 'application/json',
            error: function(result) {
                console.log('An Ajax error occurred');
            },
            success: function (result) {
                var json = JSON.parse(result);
                $('h1').css('color', json.color);
            }
        });
    });
});
