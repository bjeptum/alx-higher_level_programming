/* global $ */

// Updates the text color of header to red using jQuery

$(document).ready(() => {
  // Select the header element using jQuery
  const $header = $('header');
  // Modify the color of the header
  if ($header.length) {
    $header.css('color', '#FF0000');
  }
});
