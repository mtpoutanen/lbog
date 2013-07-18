
$('#submit-button').click(function() {

    var username        = $("#id_username").val();
    var password1       = $("#id_password1").val();
    var password2       = $("#id_password2").val();

    var country         = $("#id_country option:selected").text();
    var state           = $("#id_state option:selected").text();
    var state_id        = $("#id_state").val();
    var city            = $("#id_city").val();
    // var post_code       = $("#id_post_code").val();
    // var address         = $("#id_address").val();
    var errors = getErrors(username, password1, password2, country, state, city);

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

function getErrors(username, password1, password2, country, state, city) {
    var tempErrors = "";
    if (username    == "") {
        tempErrors += "- Please enter a username\n";
    }
    if (password1   == "") {
        tempErrors += "- Please enter a password\n";
    }
    if (password2   == "") {
        tempErrors += "- Please confirm password\n";
    }
    if (password1 != password2) {
        tempErrors += "- Passwords don't match\n";
    }
    if (country     == "Please select a country") {
        tempErrors += "- Please select a country\n";
    }
    if (state       == "Please select a state") {
        tempErrors += "- Please select a state\n";
    }
    if (city        == "") {
        tempErrors += "- Please enter a city\n";
    }
    return tempErrors;
}

$('#id_user_type_0').change(function () {
    var skills_div = $("#skills_div");
    if (this.checked) {
        skills_div.removeClass('hidden');
    } 
});

$('#id_user_type_1').change(function () {
    var skills_div = $("#skills_div");
    if (this.checked) {
        skills_div.addClass('hidden');
    } 
});

$(document).ready(function(){

    var user_type0 = $("#id_user_type_0");
    user_type0.attr('rel', 'popover');
    user_type0.attr('title', 'Register as a volunteer or a charitable / non-profit organisation');

    if (user_type0.checked) {
        $('#skills_div').removeClass('hidden');
    }

    var user_type1 = $("#id_user_type_1");
    user_type1.attr('rel', 'popover');
    user_type1.attr('title', 'Register as a volunteer or a charitable / non-profit organisation');

    var id_username = $("#id_username");
    id_username.attr('rel', 'popover');
    id_username.attr('title', 'Enter a username');

    var id_email = $("#id_email");
    id_email.attr('rel', 'popover');
    id_email.attr('title', 'Enter an email address');

    var id_first_name = $("#id_first_name");
    id_first_name.attr('rel', 'popover');
    id_first_name.attr('title', 'Enter your first name (optional)');

    var id_last_name = $("#id_last_name");
    id_last_name.attr('rel', 'popover');
    id_last_name.attr('title', 'Enter your last name (optional)');

    var id_title = $("#id_title");
    id_title.attr('rel', 'popover');
    id_title.attr('title', 'Enter your title in your organisation (optional)');

    var id_company_name = $("#id_company_name");
    id_company_name.attr('rel', 'popover');
    id_company_name.attr('title', 'Enter your company name (optional)');

    var id_country = $("#id_country");
    id_country.attr('class', 'chzn-select');
    
    var id_country_chzn = $("#id_country_chzn");
    id_country_chzn.attr('rel', 'popover');
    id_country_chzn.attr('title', 'LBOG collects some '
        + 'data on its members\' location to better be able to match volunteers with projects');

    var id_state = $("#id_state");
    id_state.attr('class', 'chzn-select');

    var id_state_chzn = $("#id_state_chzn");
    id_state_chzn.attr('rel', 'popover');
    id_state_chzn.attr('title', 'Enter your home state (or choose n/a (Outside of US and Canada))');

    var id_city = $("#id_city");
    id_city.attr('rel', 'popover');
    id_city.attr('title', 'LBOG collects some '
        + 'data on its members\' location to better be able to match volunteers with projects');

    var id_post_code = $("#id_post_code");
    id_post_code.attr('rel', 'popover');
    id_post_code.attr('title', 'Enter your post code / zip code (optional)');

    var id_address = $("#id_address");
    id_address.attr('rel', 'popover');
    id_address.attr('title', 'Enter your street address (optional)');


});

$(".chzn-select").chosen();