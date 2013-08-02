
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
	$('#project-search-results').html(data);
	var wrappers = $('.search-top-wrapper');
	for (var i = 0; i < wrappers.length; i++) {
		var countString = i.toString();
		var wrapperId 	= '#top-'+countString;
		var imageId 	= '#image-'+countString;
		var rowHeight	= $(wrapperId).height();
		// alert(rowHeight);
		// alert(	'wrapperId = ' + wrapperId + '\n' +
		// 		'imageId = ' + imageId + '\n');
				 // + 'rowHeight = ' + rowHeight.toString());
		$(imageId).height(rowHeight);
	}
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