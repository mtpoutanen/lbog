// alert('ready outside doc');

// var $ = django.jQuery


$(document).ready(function(){
    var user_type0 = $("#id_user_type_0");
    user_type0.attr('rel', 'popover');
    user_type0.attr('title', 'Register as a volunteer or a charitable / non-profit organisation');

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
    id_state_chzn.attr('title', 'Enter your home state (US Only)');
                          // widget=forms.Select(attrs={'class': 'chzn-select', 'data-placeholder': 'Select Country'}))


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