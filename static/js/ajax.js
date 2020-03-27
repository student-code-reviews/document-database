"use strict";

function replaceRandomQuote(results) {
    $("#random-quote-text").html(results);
}

function showRandomQuote(evt) {
    $.get('/random_quote', replaceRandomQuote);
}

$('#get-random-quote-button').on('click', showRandomQuote);

