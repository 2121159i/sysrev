$(document).ready(function() {
	$('.btn.btn-default.delete').click(function () {

		var $id = $(this).attr('id');
		$.post("/sysrev/delete_review/", {id: $id}, function (data) {
		});
	});

	//$('.btn btn-default').click().map(function() {
	//	var id = $(this).attr('id');
	//	alert(id);
		// Call endpoint with the given query

});