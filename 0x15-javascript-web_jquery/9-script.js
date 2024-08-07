/* global $ */

// Fetches URL and display value
$(document).ready(function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
    $('#hello').text(data.hello);
  });
});
