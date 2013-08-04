
$('#id_country').change(function() {
	$('#id_country_chzn').children().css({'color': '#333333'});
});

$('#id_state').change(function() {
	$('#id_state_chzn').children().css({'color': '#333333'});
});

$('#id_status').change(function() {
	$('#id_status_chzn').children().css({'color': '#333333'});
});

$('#id_description').keyup(function(){
	var remChar = 1000
    if(this.value.length > remChar){
        return false;
    }
    $("#remainingC").html((remChar - this.value.length) + ' / 1000');
});

$('#id_message').keyup(function(){
	var remChar = 500
    if(this.value.length > remChar){
        return false;
    }
    $("#remainingC").html((remChar - this.value.length) + ' / '+remChar.toString());
});