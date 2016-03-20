//function to add the input from the advanced search query (not or nothing in the beginning), AND/OR after it
$(document).ready(function(){
    $('#plus_button').click(function(){
        var toAdd = $('input[name=query_string_advanced]').val();
        var select_not = $("#not_selector option:selected").text();
        var select_and_or = $("#and_or_selector option:selected").text();

        $('.list').append('<div class="item">' + select_not + " " + toAdd + " " + select_and_or + '</div>');
    });
    $(document).on('click','.item',function(){
        $(this).remove();
    });
});
