function submitQuestion(){
	var title = $("#question-title").val()
	var content = $("#question-content").val()
	var category = $("#question-category").val()
	$.ajax({
		type: "POST"
		url: "../add_question/"
		data: { "title": title,
				"content": content
				"category": category}
		datatype: "json",
		success: function(response) {
			location.reload()
		}
	});
}

'''
NEED TO ADD IN CATEGORIES

need a category field in ask a new questions

need to populate categories in the left hand divider
'''