$('#submit-button').click(function() {

    var country         = $("#id_country option:selected").text();
    var state           = $("#id_state option:selected").text();
    var state_id        = $("#id_state").val();
    var city            = $("#id_city").val();

    var errors = getErrors();

    if (errors != "") {
        error_msg = "Please correct the following fields:\n\n" + errors;
        alert(error_msg);
    } else {
        search_text = country;

        if (state != 'n/a (Outside of US or Canada)') {
         search_text = search_text + "," + state;
     } 

     search_text = search_text + "," + city;

        //  if (post_code != "") {
        //     search_text = search_text + "," + post_code;
        // }

        // if (address != "") {
        //     search_text = search_text + "," + address;
        // }
        
        var clean_text = search_text.split(" ").join("+");
        // alert(clean_text);
        $.ajax({
            url: 'http://nominatim.openstreetmap.org/search?q=' + clean_text + '&format=json',
            type: "GET",
            dataType: "json",
            success: function (data) {
                if ($.isEmptyObject(data)) {
                    alert('Could not retrieve coordinates for your city.\n'
                        +'Please check the spelling of your city \n'
                        +'(English names will work the best).');
                } else {
                var lat = data[0].lat;
                var lon = data[0].lon;
                    $('#id_lat').val(lat);
                    $('#id_lon').val(lon);
                    $('#profile-form').submit();
                }
            }
        });

}
});