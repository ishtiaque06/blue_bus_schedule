/*This function puts in a request for fetching parsed data
from the server to represent on the site*/

$(function() {
              $('button.option-toBrynMawr').bind('click', function() {
                $.getJSON('/to_Bryn_Mawr', function(response) {
                  $("p#toDestination").text(response);
                });
                return false;
              });
            });

