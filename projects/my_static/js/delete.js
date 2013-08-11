function deleteContent(url) {
	confirmed = confirm('Are you sure?');
	if (confirmed) {
		$.post(url, { 'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val() }).done(
			function(data) {
		  		if ((data.error_message) != 'no_errors') {
		  			alert(data.error_message);
		  		} else {
		  			$(data.div_id).hide();
		  			alert('Deleted successfully.');
		  		}
		});
	}
}

function deactivate(url, login_url, logout_url) {
	confirmed = confirm('Are you sure?\nPlease note that your projects will remain in the database.');
	if (confirmed) {
		$.post(url, { 'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val() }).done(
			function(data) {
		  			window.location = logout_url;
		  			// window.location = login_url;
		  			// alert('Your account has been deactivated.');
			});
	}
}