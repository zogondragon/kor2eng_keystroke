# This Python file uses the following encoding: utf-8
# Python 2.7.3  
# 2012-11-08 ZD
# This script processes propernoun_freq.txt (kor) into 
# its keystroke equivalent propernoun_dic.txt

import codecs
import string
import re

def main():
    in_file = codecs.open("propernoun_freq.txt", 
                            "r", encoding='utf-8')
    out_file = codecs.open("propernoun_dic.txt",
                            "w", encoding='utf-8')

    while True:
        in_line = in_file.readline()
        if not in_line:
            break
        fields = in_line.split() 
        out_line = re.sub("\d+", "", fields[1]) + "\n"
        out_file.write(out_line)

    in_file.close()
    out_file.close()
        


if __name__ == "__main__":
    main()
