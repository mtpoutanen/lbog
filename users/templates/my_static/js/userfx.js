
function getErrors() {
    var tempErrors = "";
    var country         = $("#id_country option:selected").text();
    var state           = $("#id_state option:selected").text();
    var city            = $("#id_city").val();

    if (country     == "Country...") {
        tempErrors += "- Please select a country...\n";
    }
    if (state       == "State...") {
        tempErrors += "- Please select a state...\n";
    }
    if (city        == "") {
        tempErrors += "- Please enter a city\n";
    }
    return tempErrors;
}

function getCountrySearch() {
    return false;
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

    var id_title = $("#id_title");
    id_title.attr('rel', 'popover');
    id_title.attr('title', 'Enter your title in your organisation (optional)');

    var id_country = $("#id_country");
    id_country.attr('class', 'chzn-select');
    
    var id_country_chzn = $("#id_country_chzn");
    id_country_chzn.attr('rel', 'popover');
    id_country_chzn.attr('title', 'LBOG collects some '
        + 'geographic data on its members\' location to better be able to match volunteers with projects');

    var id_state = $("#id_state");
    id_state.attr('class', 'chzn-select');

    var id_state_chzn = $("#id_state_chzn");
    id_state_chzn.attr('rel', 'popover');
    id_state_chzn.attr('title', 'Enter your home state (or choose n/a (Outside of US and Canada))');

    var id_city = $("#id_city");
    id_city.attr('rel', 'popover');
    id_city.attr('title', 'LBOG collects some '
        + 'geographic data on its members\' location to better be able to match volunteers with projects');

    var id_allow_contact = $("#id_allow_contact");
    id_allow_contact.attr('rel', 'popover');
    id_allow_contact.attr('title', 'If you choose to opt out from this '
        + 'your profile will only be visible to the charities you have '
        + 'contacted and the developers working on the same projects.\n\n'
        + 'It will also not appear in the developer search results.');


});

function callback() {
    $('#profile-form').submit();
}