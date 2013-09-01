$('#submit-button').click(function() {
    // Get the data
    var country         = $("#id_country option:selected").text();
    var state           = $("#id_state option:selected").text();
    var city            = $("#id_city").val();
    
    // See if the data was entered correctly. This function is implemented
    // in different ways for different purposes 
    var errors          = getErrors();
    // Check if the user is searching within one country (returns false
    // when creating or altering profiles or projects)
    var countrySearch   = getCountrySearch();

    if (errors != "") {
        error_msg = "Please correct the following fields:\n\n" + errors;
        alert(error_msg);
    } else {
        // if there are no errors, concatenate the search parameters
        search_text = country;
        if (state != 'n/a (Outside of US or Canada)') {
         search_text = search_text + "," + state;
        } 
        if (city != '') {
           search_text = search_text + "," + city;
        }     
        // only applies to searches, see above 
        if (countrySearch) {
            callback();
        } else {
            // standard case, the search text is formatted in to MapQuest API
            // friendly format and used as a parameter in an ajax call.
            var clean_text = search_text.split(" ").join("+");
            $.ajax({
                url: 'http://open.mapquestapi.com/nominatim/v1/search.php?q='
                     + clean_text + '&format=json',           
                type: "GET",
                dataType: "json",
                success: function (data) {
                    // show error message, if no coordinates were retrieved
                    if ($.isEmptyObject(data)) {
                        alert('Could not retrieve coordinates for your city.\n'
                            +'Please check the spelling of your city \n'
                            +'(English names will work the best).');
                    } else {
                    // Coordinates retrieved successfully. Callback function has
                    // has different implementations for different purposes.
                    var lat = data[0].lat;
                    var lon = data[0].lon;
                        $('#id_lat').val(lat);
                        $('#id_lon').val(lon);
                        callback();
                    }
                }
            });
        } 
    }
});