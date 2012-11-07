# This Python file uses the following encoding: utf-8
# Python 2.7.3  
# 2012-10-29 ZD
#   This .py file tests libK2EK.py class

import libK2EK

def main():
    print libK2EK.kor_syllable_to_eng_syllable("ㅃ")
    print libK2EK.kor_syllable_to_eng_syllable("ㅏ")
    print libK2EK.kor_syllable_to_eng_syllable("ㄱ")
    print libK2EK.kor_syllable_to_eng_syllable("ㅏ")
    print libK2EK.kor_syllable_to_eng_syllable("ㅇ")
    print libK2EK.kor_syllable_to_eng_syllable("7")

    print libK2EK.kor_char_to_syllables(u'가')
    print libK2EK.kor_char_to_syllables(u'괜')
    print libK2EK.kor_char_to_syllables(u'찮')
    print libK2EK.kor_char_to_syllables(u'다')

    testTuple = libK2EK.kor_char_to_syllables(u'가')
    result = (libK2EK.kor_syllable_to_eng_syllable(testTuple[0]),
                libK2EK.kor_syllable_to_eng_syllable(testTuple[1]),
                libK2EK.kor_syllable_to_eng_syllable(testTuple[2]))

    print result

    print libK2EK.kor_string_to_keystrokes(u"테스트")
    print libK2EK.kor_string_to_keystrokes(u"아 진짜 난 개쩌는거같다")
    print libK2EK.kor_string_to_keystrokes(u"겹모음 쌍자음 복합종성도 괜찮음")

    libK2EK.kor_wordlist_to_keystrokes("korean_frequent_dic.txt", "korean_keystroke_wordlist.txt")

if __name__ == "__main__":
    main()
