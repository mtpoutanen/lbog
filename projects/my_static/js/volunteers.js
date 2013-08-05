
function getErrors() {
    
    var title           = $("#id_title").val();
    var need_locals     = $("#id_need_locals").val();
    var skills          = $("#id_skills").val();

    var country         = $("#id_country option:selected").text();
    var state           = $("#id_state option:selected").text();
    var city            = $("#id_city").val();

    var tempErrors = "";
    if (title    == "") {
        tempErrors += "- Please enter a title\n";
    }    
    
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

function getMyLocation() {
    var country     = $('#p_country').text();
    var state       = $('#p_state').text();
    var city        = $('#p_city').text();

    var country_id = $("#id_country option:contains("+country+")").val();
    $("#id_country").val(country_id).trigger("liszt:updated");

    var state_id = $("#id_state option:contains("+state+")").val();
    $("#id_state").val(state_id).trigger("liszt:updated");

    $('#id_city').val(city);
}

function callback() {
    $('#project-form').submit();
}

$(document).ready(function(){

    var user_type1 = $("#id_title");
    user_type1.attr('rel', 'popover');
    user_type1.attr('title', 'A good title gives a quick overview of the project at a glance.\n'
     + 'For example: "A youth rugby team needs a website"\n'
     +'or: "An Indian charity looking for a fundraising app"');

    var id_company_name = $("#id_need_locals");
    id_company_name.attr('rel', 'popover');
    id_company_name.attr('title', 'Please tick this box if you think the project requires\n'
        + 'physically meeting the developers. This is a must for\n'
        + 'projects such as teaching computer skills, but it may\n'
        + 'limit the pool of potential developers for projects such\n'
        + 'such as creating a website.');

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
        + 'data on its members\' location to better be able to match volunteers with projects');

    var id_description = $("#id_description");
    id_description.attr('rel', 'popover');
    id_description.attr('title', 'A good description of your needs will make it easier\n'
        + 'for developers to find your project.');

    var id_image = $("#id_image");
    id_image.attr('rel', 'popover');
    id_image.attr('title', 'A good image will help your project stand out from the others');


});

