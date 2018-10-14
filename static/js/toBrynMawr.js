/*This function puts in a GET request for fetching parsed data
from the server to represent on the site*/

$('.option-toBrynMawr').click(function() {
	$.ajax({
		type: 'GET',
		url: '/to_Bryn_Mawr',
		success: function(response) {
			response = response.replace(/\\n/g, '\n');
			response = response.replace(/"/g,'');
			$("#toDestination").text(response);
		}
	});
});