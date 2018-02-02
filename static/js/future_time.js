/*
This JavaScript file uses JQuery to send POST requests to the server
with a specified time that is input on the client side.
The response from the server is then formatted to properly output
into the webpage when the user submits the data into the site.
*/
$(document).ready(function() {

	
	$("#time-to-Haverford").click(function() {
		//Parsing data from option selected with times for trip to HC
		var day = $("#day option:selected").text();
		var hour = $("#hour option:selected").text();
		var minute = $("#minute option:selected").text();
		var ampm = $("#ampm option:selected").text();
		//This block prevents invalid inputs from being sent to the server
		if (day == "Day" || hour == "Hour" ||
			minute == "Minute" || ampm == "AM/PM") {
			alert("Please select all the specifications.");
		}
		//This block sends a POST request to the server and formats
		//the response into a multi-lined string.
		else {
			var time = hour + ':' + minute + ampm + "," + day;
			$.post({
				type: 'POST',
				url: '/time_to_Haverford',
				data: JSON.stringify(time),
				contentType: "application/json;charset:UTF-8",
				success: function(response) {
					response = response.replace(/\\n/g, '\n');
					response = response.replace(/"/g,'');
					$("p#future-times").text(response);
				}
			});
		}
	});
	
	$("#time-to-BrynMawr").click(function() {
		//Parsing data from option selected with times for trip to BMC
		var day = $("#day option:selected").text();
		var hour = $("#hour option:selected").text();
		var minute = $("#minute option:selected").text();
		var ampm = $("#ampm option:selected").text();

		//This block prevents invalid inputs from being sent to the server
		if (day == "Day" || hour == "Hour" ||
			minute == "Minute" || ampm == "AM/PM") {
			alert("Please select all the specifications.");
		}
		//This block sends a POST request to the server and formats
		//the response into a multi-lined string.
		else {
			var time = hour + ':' + minute + ampm + "," + day;
			$.post({
				type: 'POST',
				url: '/time_to_BrynMawr',
				data: JSON.stringify(time),
				contentType: "application/json;charset:UTF-8",
				success: function(response) {
					response = response.replace(/\\n/g, '\n');
					response = response.replace(/"/g,'');
					$("p#future-times").text(response);
				}
			});
		}
	});
});