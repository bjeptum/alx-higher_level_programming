/* global $ */

// Adds, removes, and clears elements using jQuery

$(document).ready(() => {
  // Add new <li> element to the list
  $('#add_item').click(() => {
    const newItem = $('<li>Item</li>');
    $('ul.my_list').append(newItem);
  });

  // Remove last <li> element from the list
  $('#remove_item').click(() => {
    $('ul.my_list li').last().remove();
  });

  // Clear all <li> elements from the list
  $('#clear_list').click(() => {
    $('ul.my_list').empty();
  });
});
