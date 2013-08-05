$('#submit-button').click(function() {
    
    var country         = $("#id_country option:selected").text();
    var state           = $("#id_state option:selected").text();
    var city            = $("#id_city").val();
    var errors          = getErrors();
    var countrySearch   = getCountrySearch();

    if (errors != "") {
        error_msg = "Please correct the following fields:\n\n" + errors;
        alert(error_msg);
    } else {
        search_text = country;

        if (state != 'n/a (Outside of US or Canada)') {
         search_text = search_text + "," + state;
        } 

         if (city != '') {
            search_text = search_text + "," + city;
         }
        
        if (countrySearch) {
            callback();
        } else {
            lat = 62.795268
            lon = 22.83263

            $('#id_lat').val(lat);
            $('#id_lon').val(lon);
            callback();
        }
        
        // var clean_text = search_text.split(" ").join("+");
        // $.ajax({
        //     //http://open.mapquestapi.com/nominatim/v1/search.php?format=json&json_callback=renderExampleBasicResults&q=windsor+[castle]&addressdetails=1&limit=3&viewbox=-1.99%2C52.02%2C0.78%2C50.94&exclude_place_ids=41697
        //     url: 'http://open.mapquestapi.com/nominatim/v1/search.php?q=' + clean_text + '&format=json',           
        //     // url: 'http://nominatim.openstreetmap.org/search?q=' + clean_text + '&format=json',
        //     type: "GET",
        //     dataType: "json",
        //     success: function (data) {
        //         if ($.isEmptyObject(data)) {
        //             alert('Could not retrieve coordinates for your city.\n'
        //                 +'Please check the spelling of your city \n'
        //                 +'(English names will work the best).');
        //         } else {
        //         var lat = data[0].lat;
        //         var lon = data[0].lon;
        //             $('#id_lat').val(lat);
        //             $('#id_lon').val(lon);
        //             callback();
        //         }
        //     }
        // });

    }
});