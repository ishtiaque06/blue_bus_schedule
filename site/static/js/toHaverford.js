/*function toHaverford() {
	document.getElementById("toDestination").innerHTML = "These are the next buses to Haverford.";
}*/

$(document).ready(function() {
	$("button.option-toHaverford").click(function() {
		$("p#toDestination").text("The next buses to Haverford are these: ");
	});
});