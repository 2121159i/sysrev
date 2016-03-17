(function() {

    $('#count-button').click(function() {

        console.log("Button clicked");

        // Call endpoint with the given query
        $.get("/sysrev/get_document_count/", { query: "dog cancer" }, function(data) {

            console.log(data);

        });
    });



})();

