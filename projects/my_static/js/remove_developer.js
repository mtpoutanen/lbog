function removeDeveloper(url) {
	
	var confirmed = confirm('Are you sure?');
	if(confirmed) {
		$.ajax({
			url: url,
			type: 'GET',
			dataType: 'json',
			success: successFunction
		});
	}
}

function successFunction(data) {
    var error = data.error_message;
    if (error == 'no_errors') {
    	$(data.tr_id).hide();
    } else {
    	alert(error);
    }  
}
