$('#count-button').click(function() {

    // Get the query string from the input field
    var query = $('#id_query').val();
    console.log(query);

    // Make the loading icon visible
    $('#loading-icon').css("visibility", "visible");

    // Call endpoint with the given query
    $.get("/sysrev/get_doc_count/", { query: query }, function(data) {

        // Hide loading icon
        $('#loading-icon').css("visibility", "hidden");

        // Append the result to the HTML element
        $('#document-count').html(data);
        console.log(data);

    });
});
