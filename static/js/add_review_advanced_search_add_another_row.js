//function to add the input from the advanced search query (not or nothing in the beginning), AND/OR after it
$(document).ready(function(){
    $('#plus_button').click(function(){
        var toAdd = $('input[name=query_string_advanced]').val();
        var selectNot = $("#not_selector option:selected").text();
        var selectAndOr = $("#and_or_selector option:selected").text();
        $('.list').append('<div class="item">' + selectNot + " " + toAdd + " " + selectAndOr + '</div>');

    });
    $(document).on('click','.item',function(){
        $(this).remove();
    });
});
