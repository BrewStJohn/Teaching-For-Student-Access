// set up variables
var key = 5;
var range = 26;
var aCode = 65;
var zCode = aCode + range;

// run main function when page load
window.onload = function() {
  // get the submit button from HTML
  var submitButton = document.getElementById("submit");

  // run the encryption/decryption when button is
  // clicked
  submitButton.onclick = processInput;
}

// eyncrypt with regular Caesar cipher
function encipher(message) {
  // set up enciphered text
  var encipherBox = document.getElementById("encipher");
  encipherBox.innerHTML = "";

  // for each letter in the message, shift the ascii
  // code by the key and add it ot the ned of the text
  // in the output box
  for (var i = 0; i < message.length; i++) {
    // get current charater ascii code
    var letter = message.charCodeAt(i);
    var newLetter = letter;

    // if character is a letter, add the shift key 
    // to the ascii code
    if (letter >= aCode && letter <= zCode) {
      newLetter += key;
      // ensure that the new code is actually a letter
      if (newLetter >= zCode) {
        newLetter -= range;
      }
    }

    // get character from new ascii code and add it 
    // to the enciphered text
    newLetter = String.fromCharCode(newLetter);
    encipherBox.innerHTML += newLetter;
  }
}

// decrypt with Caesar cipher
function decipher(message) {
  // set up enciphered text
  var decipherBox = document.querySelector("#decipher");
  decipherBox.innerHTML = "";

  // for each letter in the message, shift the ascii
  // code by the key and add it ot the ned of the text
  // in the output box
  for (var i = 0; i < message.length; i++) {
    // get current charater ascii code
    var letter = message.charCodeAt(i);
    var newLetter = letter;

    // if character is a letter, add the shift key 
    // to the ascii code
    if (letter >= aCode && letter <= zCode) {
      newLetter -= key;
      // ensure that the new code is actually a letter
      if (newLetter < aCode) {
        newLetter += range;
      }
    }

    // get character from new ascii code and add it 
    // to the enciphered text
    newLetter = String.fromCharCode(newLetter);
    decipherBox.innerHTML += newLetter;
  }
}

// find the nth digit of pi
function piDigit(n) {
  var digit = Math.floor(Math.PI * Math.pow(10, n)) % 10;
  return digit;
}

// encrypt with regular Caesar cipher
function strongEncipher(message) {
  // set up enciphered text
  var encipherBox = document.getElementById("strongEncipher");
  encipherBox.innerHTML = "";

  // for each letter in the message, shift the ascii
  // code by the key and add it to the end of the text
  // in the output box
  for (var i = 0; i < message.length; i++) {
    // get current character ascii code
    var letter = message.charCodeAt(i);
    var newLetter = letter;

    // if character is a letter, add the shift key 
    // to the ascii code
    if (letter >= aCode && letter <= zCode) {
      newLetter += piDigit(i);
      // ensure that the new code is actually a letter
      if (newLetter > zCode) {
        newLetter -= range;
      }
    }

    // get character from new ascii code and add it 
    // to the enciphered text
    newLetter = String.fromCharCode(newLetter);
    encipherBox.innerHTML += newLetter;
  }
}

// decrypt with regular Caesar cipher
function strongDecipher(message) {
  // set up enciphered text
  var decipherBox = document.getElementById("strongDecipher");
  decipherBox.innerHTML = "";

  // for each letter in the message, shift the ascii
  // code by the key and add it to the end of the text
  // in the output box
  for (var i = 0; i < message.length; i++) {
    // get current character ascii code
    var letter = message.charCodeAt(i);
    var newLetter = letter;

    // if character is a letter, add the shift key 
    // to the ascii code
    if (letter >= aCode && letter <= zCode) {
      console.log(piDigit(i))
      newLetter -= piDigit(i);
      // ensure that the new code is actually a letter
      if (newLetter < aCode) {
        newLetter += range;
      }
    }

    // get character from new ascii code and add it 
    // to the enciphered text
    newLetter = String.fromCharCode(newLetter);
    decipherBox.innerHTML += newLetter;
  }
}

// trigger the (en/de)ciphering
function processInput() {
  // get the input text
  var inputBox = document.querySelector("#rawInput");
  var rawInput = inputBox.value;
  rawInput = rawInput.toUpperCase();

  // trigger the output functions
  encipher(rawInput);
  strongEncipher(rawInput);
  decipher(rawInput);
  strongDecipher(rawInput);
}