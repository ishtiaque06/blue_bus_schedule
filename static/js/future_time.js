$(document).ready(function() {
	$("#time-to-Haverford").click(function() {
		var day = $("#day option:selected").text();
		console.log(day);
		var hour = $("#hour option:selected").text();
		console.log(hour);
		var minute = $("#minute option:selected").text();
		console.log(minute);
		var ampm = $("#ampm option:selected").text();
		console.log(ampm);
		if (day == "Day" || hour == "Hour" ||
			minute == "Minute" || ampm == "AM/PM") {
			alert("Please select all the specifications.");
		}
		else {
			var time = hour + ':' + minute + ampm + ", " + day;
			$.ajax({
				type: 'POST',
				url: '/time_to_Haverford',
				data: JSON.stringify(time),
				contentType: "application/json;charset:UTF-8",
				success: function() {
					alert("it works!");
				}
			});
		}
	});
	$("#time-to-BrynMawr").click(function() {
		var day = $("#day option:selected").text();
		console.log(day);
		var hour = $("#hour option:selected").text();
		console.log(hour);
		var minute = $("#minute option:selected").text();
		console.log(minute);
		var ampm = $("#ampm option:selected").text();
		console.log(ampm);
		if (day == "Day" || hour == "Hour" ||
			minute == "Minute" || ampm == "AM/PM") {
			alert("Please select all the specifications.");
		}
		else {
			var time = hour + ':' + minute + ampm + ", " + day;
			alert(time);
		}
	});
});