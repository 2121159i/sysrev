
// Make a request on input field change
$('#id_query').bind('input', function() {

    // Get the query string from the input field
    var query = $('#id_query').val();
    if (query == "") {
        console.log("Empty");
        $('#document-count').html("");
        $('#loading-icon').css("visibility", "hidden");
        return;
    }

    // Make the loading icon visible
    $('#loading-icon').css("visibility", "visible");

    // Call endpoint with the given query
    $.get("/sysrev/get_doc_count/", { query: query }, function(data) {

        // Hide loading icon
        $('#loading-icon').css("visibility", "hidden");

        // Attach the result to the HTML element
        $('#document-count').html(data.count + " documents found");
        console.log(data);

    });
});
