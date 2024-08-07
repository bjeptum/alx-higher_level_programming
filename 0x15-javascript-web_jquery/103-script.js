/* global $ */

// Fetches, displays how to say "Hello" in different languages

$(document).ready(() => {
  const fetchTranslation = () => {
    // Get the language code from the input field
    const languageCode = $('#language_code').val();
    
    // Check if the language code is provided
    if (languageCode) {
      // Construct the API URL using the language code
      const apiUrl = `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`;
      
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
  };

  // Fetch translation when button is clicked
  $('#btn_translate').click(fetchTranslation);

  // Fetch translation when Enter key is pressed in the input field
  $('#language_code').keypress((event) => {
    if (event.which === 13) { // Enter key
      fetchTranslation();
    }
  });
});
