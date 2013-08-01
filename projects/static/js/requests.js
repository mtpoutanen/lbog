
function changeStatus(url) {
	$.ajax({
		url: url,
		type: 'GET',
		dataType: 'json',
		success: successFunction
	});
	alert(url);
}

function successFunction(data) {
    if (data.error_message != "") {
    	alert(data.error_message);
    } else {
    	alert('The request has been '+data.status);
    }
}