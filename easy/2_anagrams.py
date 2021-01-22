import re

input = 'niesevehrtfeev'

TRANSCODER = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

def decodeAnagram(anagram):
    wordsfound = {}
    timesfound = 0
    for key in TRANSCODER.keys():
        for letter in key:
            # if key is not found
            if letter not in input:
                break
            # if this is the last letter in the "key" word
            if letter == key[-1]:
                timesfound += 1
                break
        wordsfound[key] = timesfound
        # to fix the bug we'll need to remove the letters used by the algo but only after the complete word has been found
        # TODO: create a function to remove letters from input
        timesfound = 0
    return wordsfound

def transformToIntString(wordsfound_dict):
    result = [];
    for key, value in wordsfound_dict.items():
        if value > 0:
            result.append(TRANSCODER[key])
        pass
    return result

decodedAnagram = decodeAnagram(input)
print(decodedAnagram)
print(transformToIntString(decodedAnagram))