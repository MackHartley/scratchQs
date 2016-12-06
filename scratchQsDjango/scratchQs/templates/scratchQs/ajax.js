function submitQuestion(){
	var text = $("#question-field").val()
	$.ajax({
		type: "POST"
		url: "../add_question/"
		data: {"question": text}
		datatype: "json",
		success: function(response) {
			location.reload()
		}
	});
}