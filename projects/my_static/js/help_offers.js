
function changeStatus(url) {
	$.ajax({
		url: url,
		type: 'GET',
		dataType: 'json',
		success: successFunction
	});
	// alert(url);
}

function successFunction(data) {
    $("."+data.div_id).html(data.status);
    $("."+data.div_id).removeClass('pending accepted rejected').addClass(data.status);
    if (data.status == 'accepted') {
    	var message = 'You have '+data.status+' the offer to help and a notification has been sent to the'
    				+ ' developer. You may want to send him/her an email to work out the details'
    				+ ' on how to get started. If you have enough developers, please change the project status'
    				+ ' to "Project under way"' ;
    	alert(message);
    } else {
    	var message = 'The help offer has been rejected and the developer has been notified.'
    					+ ' Good luck with the search'
    	alert(message)
    }
}