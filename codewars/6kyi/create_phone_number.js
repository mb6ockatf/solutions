#!/usr/bin/env node
/*
https://www.codewars.com/kata/525f50e3b73515a6db000b83
*/
function createPhoneNumber(numbers){
    var format = "(xxx) xxx-xxxx";
    for(var i = 0; i < numbers.length; i++)
    {
      format = format.replace('x', numbers[i]);
    }
    return format;
  }