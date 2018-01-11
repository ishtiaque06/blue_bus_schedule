/*function toBrynMawr() {
	document.getElementById("toDestination").innerHTML = "These are the next buses to Bryn Mawr.";
}*/

$(document).ready(function() {
	$("button.option-toBrynMawr").click(function() {
		$("p#toDestination").text("The next buses to Bryn Mawr are these: ");
	});
});