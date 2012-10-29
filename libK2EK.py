# This Python file uses the following encoding: utf-8
# Python 2.7.3  
# 2012-10-29 ZD
#   This .py file contains a class of functions which translate
# Korean to English by keystroke level.

import codecs

K2EDict =  {
            # First syllables (consonants)
            "ㄱ":"r","ㄲ":"R","ㄴ":"s","ㄷ":"e","ㄸ":"E",
            "ㄹ":"f","ㅁ":"a","ㅂ":"q","ㅃ":"Q","ㅅ":"t",
            "ㅆ":"T","ㅇ":"d","ㅈ":"w","ㅉ":"W","ㅊ":"c",
            "ㅋ":"z","ㅌ":"x","ㅍ":"v","ㅎ":"g",
            # Second syllables (vowels)
            "ㅏ":"k","ㅐ":"o","ㅑ":"i","ㅒ":"O","ㅓ":"j",
            "ㅔ":"p","ㅕ":"u","ㅖ":"P","ㅗ":"h","ㅘ":"hk",
            "ㅙ":"ho","ㅚ":"hl","ㅛ":"y","ㅜ":"n","ㅝ":"nj",
            "ㅞ":"np","ㅟ":"nl","ㅠ":"b","ㅡ":"m","ㅢ":"ml",
            "ㅣ":"l",
            # Third syllables (consonants)
            "":"","ㄳ":"rt","ㄵ":"sw","ㄶ":"sg","ㄺ":"fr",
            "ㄻ":"fa","ㄼ":"fq","ㄽ":"ft","ㄾ":"fx","ㄿ":"fv",
            "ㅀ":"fg","ㅄ":"qt",
            # space and new line
            " ":" ", "\n":"\n", "\r":"\r"}

# This lists are used in a function explodes character into syllables 
FirstSyllables =   ["ㄱ","ㄲ","ㄴ","ㄷ","ㄸ",
                    "ㄹ","ㅁ","ㅂ","ㅃ","ㅅ",
                    "ㅆ","ㅇ","ㅈ","ㅉ","ㅊ",
                    "ㅋ","ㅌ","ㅍ","ㅎ"]
SecondSyllables =  ["ㅏ","ㅐ","ㅑ","ㅒ","ㅓ",
                    "ㅔ","ㅕ","ㅖ","ㅗ","ㅘ",
                    "ㅙ","ㅚ","ㅛ","ㅜ","ㅝ",
                    "ㅞ","ㅟ","ㅠ","ㅡ","ㅢ",
                    "ㅣ"]
ThirdSyllables =   ["","ㄱ","ㄲ","ㄳ","ㄴ",
                    "ㄵ","ㄶ","ㄷ","ㄹ","ㄺ",
                    "ㄻ","ㄼ","ㄽ","ㄾ","ㄿ",
                    "ㅀ","ㅁ","ㅂ","ㅄ","ㅅ",
                    "ㅆ","ㅇ","ㅈ","ㅊ","ㅋ",
                    "ㅌ","ㅍ","ㅎ"]



# This function convert 1 Korean syllable into 
# corresponding English syllable(s). 
# Return type : string
def kor_syllable_to_eng_syllable(syll):
    if syll in K2EDict:
        return K2EDict[syll]
    else:
        return syll 
        #raise IndexError(syll)

# This function explodes 1 Korean character into
# tuple of several Korean syllable(s).
# Return type : 3-tuple of strings
def kor_char_to_syllables(char):
    code = ord(char)
    
    if 0xAC00 <= code and code <= 0xD7A3:   # A full character
        tempcode = code - 0xAC00
        idxJong = tempcode % 28
        idxJung = (tempcode/28) % 21
        idxCho = ((tempcode/28)/21) % 19
        return (    FirstSyllables[idxCho], 
                    SecondSyllables[idxJung],
                    ThirdSyllables[idxJong]     )
    elif 0x3131 <= code and code <= 0x314E: # A consonant
        return ( FirstSyllables[code - 0x3131], "", "" )
    elif 0x314F <= code and code <= 0x3163: # A vowel
        return ( "", SecondSyllables[code - 0x314F], "" )
    else:
        return ( "", "", "" )

# This function converts a Korean string into 
# a Keystroke Equivalent English string
def kor_string_to_keystrokes(string):
    result = ""
    for i in range(len(string)):
        midTuple = kor_char_to_syllables( string[i] )
        tempList = [kor_syllable_to_eng_syllable(midTuple[0]),
                    kor_syllable_to_eng_syllable(midTuple[1]),
                    kor_syllable_to_eng_syllable(midTuple[2])]
        result = result + ("".join(tempList))
    return result

# This function gets (wordlist_name:string) , access that file, 
# does the line to line (Kor -> Keystroke) conversion, 
# writes result to (output_name:string) file.
# If something happens, raise Exception. Return nothing.
def kor_wordlist_to_keystrokes(wordlist_name, output_name):
    in_file = codecs.open(wordlist_name, "r", encoding='utf-8')
    out_file = codecs.open(output_name, "w", encoding='utf-8')
    while True:
        in_line = in_file.readline()
        if not in_line:
            break
        out_line = kor_string_to_keystrokes(in_line) + "\n"
        out_file.write(out_line)

    in_file.close()
    out_file.close()
    return















