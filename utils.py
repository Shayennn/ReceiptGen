import re

REPLACE_WITH_BLANK_REGEX = re.compile(r'[\u0E31\u0E34-\u0E3A\u0E47-\u0E4E]')


def count_thai_word_space(text):
    text = REPLACE_WITH_BLANK_REGEX.sub('', text)
    return len(text.strip())
