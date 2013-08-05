// $("#filter-button").click(function() {
  
// });

function getErrors() {

	var tempErrors 		= "";
	var country         = $("#id_country option:selected").text();
	var state           = $("#id_state option:selected").text();
	var city            = $("#id_city").val();
	var radius          = $("#id_radius option:selected").val();

	var countryEmpty    = (country == "Country...");
	var stateEmpty    	= (state == "State...");
	var cityEmpty    	= (city == "");

	if (countryEmpty && stateEmpty && cityEmpty) {
    	// do nothing, as the user is not filtering by geography
    } else {
    	if (country     == "Country...") {
    		tempErrors += "- Please select a country...\n";
    	}
    	if (state       == "State..."
    		&& radius 	!= 'same_country') {
    		tempErrors += "- Please select a state...\n";
    	}
    	if (city        == ""
    		&& radius 	!= 'same_country') {
    		tempErrors += "- Please enter a city\n";
		}
	}
	return tempErrors;
}

function callback() {
	var skills = new Array();
	$('#id_skills option:selected').each(function(index, value) {
							skills.push($(value).text());
					});
	// call the search function as ajax
	$.ajax({
		type: 'GET',
		url: $('#search-url').attr('rel'),
		data: {
			'country': 		$("#id_country option:selected").text(),
			'lat': 			$('#id_lat').val(),
			'lon': 			$('#id_lon').val(),
			'radius':		$('#id_radius').val(),
			'keywords':     $('#id_keywords').val(),
			'skills': 		skills,
			'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(), 
		},
		dataType: 'html',
		success: searchSuccess,
	});
}

function searchSuccess(data, textStatus, jqXHR) {
	
	$('#search-li > a').trigger('click');
	$('#search-results').html(data);
	resizeImages();
}

function getCountrySearch() {
	var country         = $("#id_country option:selected").text();
    var state           = $("#id_state option:selected").text();
    var city            = $("#id_city").val();
    var radius          = $("#id_radius option:selected").val();
    var countrySearch 	= false;
    if (country != 'Country...'
    	&& radius == 'same_country') {
    	countrySearch = true;
    } else if (country == 'Country...') {
    	// a crude way to check whether the user is filtering by geography
    	countrySearch = true;
    }

    return countrySearch;
}

$(document).ready(function(){
	$('#tabs div').hide();
	$('#tabs div:first').show();
	$('#tabs ul li:first').addClass('active');
	 
	$('#tabs ul li a').click(function(){
		$('#tabs ul li').removeClass('active');
		$(this).parent().addClass('active');
		var currentTab = $(this).attr('href');
		$('#tabs > div').hide();
		$(currentTab).show();
		// $(currentTab+' > div').show();
		return false;
});
});