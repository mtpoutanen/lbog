$(document).ready(function(){

    var id_keywords = $("#id_keywords");
    id_keywords.attr('rel', 'popover');
    id_keywords.attr('title', 'All keywords must be present');

    var id_skills_chzn = $("#id_skills_chzn");
    id_skills_chzn.attr('rel', 'popover');
    id_skills_chzn.attr('title', 'Will filter developers with any of the skills');

    var id_country_chzn = $("#id_country_chzn");
    id_country_chzn.attr('rel', 'popover');
    id_country_chzn.attr('title', 'If you want to search within a certain country, please select'+
        ' "Selected Country" from the Radius dropdown and leave State and City empty.');

    var id_state_chzn = $("#id_state_chzn");
    id_state_chzn.attr('rel', 'popover');
    id_state_chzn.attr('title', 'Enter state (or choose "n/a (Outside of US and Canada)")');

    var id_city = $("#id_city");
    id_city.attr('rel', 'popover');
    id_city.attr('title', 'Enter City');

});