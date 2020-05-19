#!/usr/bin/env python3

import re, pyperclip

def tp():
    text =(pyperclip.paste())
    text_regex = re.compile(r'\d\d:\d\d:\d\d\s\s開始\s\w-\d-\d\d[-]?\s?\s?[-]?(.*)')
    sentence_list = text_regex.findall(text)
    print(str(sentence_list))
    new_text = '\n'.join(sentence_list)
    print(new_text)
    pyperclip.copy(new_text)

tp()


