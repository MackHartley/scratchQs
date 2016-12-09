function submitQuestion(){
	var title = $("#questionTitle").val()
	var content = $("#questionDescription").val()
	var category = $("#questionCategory").val()
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