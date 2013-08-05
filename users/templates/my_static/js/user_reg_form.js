// $('#id_user_type_0').change(changeFields($('#id_user_type_0').val()));
// $('#id_user_type_0').change(changeFields($('#id_user_type_1').val()));

$(document).ready(function () {
	if ($('.main-errors').text().indexOf('Please correct the following fields') > -1) {
		if ($('#id_user_type_0').attr('checked')) {
			$('#charity-mandatory').hide();
			$('#charity-label').html('Company Name:');
		}
		$('#profile-fields').removeClass('hidden');
		$('#profile-message').hide();
	}
})


$(document).ready(function () {
    $("input[name=user_type]:radio").change(function () {
        changeFields($(this).val());
    })
})

function changeFields(userType) {
	
	$('#profile-fields').hide();
	$('#profile-message').hide();
	$('#profile-fields').removeClass('hidden');
	
	if (userType == 'Charity') {
		$('#charity-mandatory').show();
		$('#charity-label').html('Charity Name:');
	 	$('#skills-div').hide();
	 	$('#allow-contact-div').hide();	
	} else {
		$('#charity-mandatory').hide();
		$('#charity-label').html('Company Name:');
		$('#skills-div').show();
	 	$('#allow-contact-div').show();
	}

	$('#profile-fields').show('fast');
}