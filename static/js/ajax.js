"use strict";

function replaceRandomQuote(results) {
    $("#random-quote-text").html(results);
}

function showRandomQuote(evt) {
    $.get('/random_quote', replaceRandomQuote);
}

$('#get-random-quote-button').on('click', showRandomQuote);

function replaceAuthoredQuotes(results) {
    $("#quotes-text").html(results);
}

function showAuthoredQuotes(evt) {
    $.get('/authored_quotes', replaceAuthoredQuotes);
}

$('#get-authored-quotes').on('click', showAuthoredQuotes);

function replacePossibleAuthors(results) {
    $("#authors-list-text").html(results);
}

function showPossibleAuthors(evt) {
    $.get('/possible_author_identities', replacePossibleAuthors);
}

$('#get-possible-authors-button').on('click', showPossibleAuthors);
