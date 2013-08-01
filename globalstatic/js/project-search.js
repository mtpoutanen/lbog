
// $("#filter-button").click(function() {
  
// });

function getErrors() {

	var tempErrors 		= "";
	var country         = $("#id_country option:selected").text();
	var state           = $("#id_state option:selected").text();
	var city            = $("#id_city").val();
	var radius          = $("#id_radius option:selected").val();

	var countryEmpty    = (country == "Please select a country");
	var stateEmpty    	= (state == "Please select a state");
	var cityEmpty    	= (city == "");

	if (countryEmpty && stateEmpty && cityEmpty) {
    	// do nothing, as the user is not filtering by geography
    } else {
    	if (country     == "Please select a country") {
    		tempErrors += "- Please select a country\n";
    	}
    	if (state       == "Please select a state"
    		&& radius 	!= 'same_country') {
    		tempErrors += "- Please select a state\n";
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
	$('#project-search-results').html(data);
}

function getCountrySearch() {
	var country         = $("#id_country option:selected").text();
    var state           = $("#id_state option:selected").text();
    var city            = $("#id_city").val();
    var radius          = $("#id_radius option:selected").val();
    var countrySearch 	= false;
    if (country != 'Please select a country'
    	&& radius == 'same_country') {
    	countrySearch = true;
    } else if (country == 'Please select a country') {
    	// a crude way to check whether the user is filtering by geography
    	countrySearch = true;
    }

    return countrySearch;
}