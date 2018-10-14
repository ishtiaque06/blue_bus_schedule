/*
This JavaScript file uses JQuery to send POST requests to the server
with a specified time that is input on the client side.
The response from the server is then formatted to properly output
into the webpage when the user submits the data into the site.
*/

/*
	The following function fetches future times around when
	the user wants to leave a designated college.
*/
function getTimes(time, destination) {
	$.ajax({
		type: 'POST',
		url: '/' + destination,
		data: time,
		contentType: "application/json;charset:UTF-8",
		success: function(response) {
			response = response.replace(/\\n/g, '\n');
			response = response.replace(/"/g,'');
			$("p#future-times").text(response);
		}
	});
}

$('.future').click(function() {
	var destination = $(this).attr('id');
	var day = $("#day option:selected").text();
	var hour = $("#hour option:selected").text();
	var minute = $("#minute option:selected").text();
	var ampm = $("#ampm option:selected").text();

	if (day == "Day" || hour == "Hour" ||
		minute == "Minute" || ampm == "AM/PM") {
		alert("Please select all the specifications.");
	}
	else {
		var time = hour + ':' + minute + ampm + "," + day;
		getTimes(time, destination);
	}
});