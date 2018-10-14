/*This function puts in a request for fetching parsed data
from the server to represent on the site*/

$('.option-toHaverford').click(function() {
	$.ajax({
		type: 'GET',
		url: '/to_Haverford',
		success: function(response) {
			response = response.replace(/\\n/g, '\n');
			response = response.replace(/"/g,'');
			$("#toDestination").text(response);
		}
	});
});