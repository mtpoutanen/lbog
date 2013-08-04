function getNotifications() {
	
	var value 				= $('#id_status').val();
	var url_to_be_changed 	= $('#search-url').attr('rel');
	var url 				= url_to_be_changed.replace('placeholder', value);
	// call the search function as ajax
	// alert(url);
	$.ajax({
		type: 'GET',
		url: url,
		data: {
			'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(), 
		},
		dataType: 'html',
		success: searchSuccess,
	});
}

function searchSuccess(data, textStatus, jqXHR) {
	$('.fill-area').html(data);
	resizeImages();
}