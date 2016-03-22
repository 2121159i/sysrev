/**
 * Created by 2121159i on 3/22/2016.
 */
$(document).ready(function(){
    $('#create_button').click(function(){
        var title = $('#id_title').val();
        var query = $('#id_query').val();
        var desc = $('#review_info').val();
        //alert(title);
        if (title!= "" && query!="" && desc!=""){
            //alert('bla');
            $('#create_button').attr("data-toggle", "modal");
            $('#create_button').attr('data-target','.bs-example-modal-sm');
        }

    })
})