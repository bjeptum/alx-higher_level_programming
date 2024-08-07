/* global $ */

// Fetches and displays how to say "Hello" in different languages based on user input

$(document).ready(() => {
  $('#btn_translate').click(() => {
    // Get the language code from the input field
    const languageCode = $('#language_code').val();
    
    // Check if the language code is provided
    if (languageCode) {
      // Construct the API URL using the language code
      const apiUrl = `https://fourtonfish.com/hellosalut/?lang=${languageCode}`;
      
      // Fetch the translation from the API
      $.get(apiUrl, (data) => {
        // Update the text of the DIV#hello with the translation
        $('#hello').text(data.hello);
      }).fail(() => {
        // Handle errors if the API request fails
        $('#hello').text('Error: Unable to fetch translation.');
      });
    } else {
      // Handle case where no language code is provided
      $('#hello').text('Please enter a language code.');
    }
  });
});
