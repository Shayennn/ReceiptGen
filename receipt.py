from utils import count_thai_word_space, REPLACE_WITH_BLANK_REGEX


class ReceiptBase:
    paper_width = 50


class ReceiptText(ReceiptBase):
    position = 0
    justify = 'left'
    text = "FOOBAR"

    def __init__(self, text: str, position: int = 0, justify: str = 'left'):
        self.text = text.strip()
        self.position = position
        self.justify = justify

    def __str__(self):
        offset = len(self.text) - count_thai_word_space(self.text)
        if self.justify == 'left':
            return f'{" " * self.position}{self.text}'.ljust(self.paper_width + offset)
        elif self.justify == 'right':
            return f'{self.text}{" " * self.position}'.rjust(self.paper_width + offset)
        else:
            total_offset = self.paper_width - count_thai_word_space(self.text)
            return f'{" " * (total_offset // 2)}{self.text}{" " * (total_offset - total_offset // 2)}'

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return count_thai_word_space(self.text)

    def __add__(self, other):
        this = self.__str__()
        other = other.__str__()
        new = ""
        ori_offset = 0
        other_offset = 0
        for i in range(self.paper_width):
            is_ori_ignore = REPLACE_WITH_BLANK_REGEX.match(this[ori_offset + i])
            is_other_ignore = REPLACE_WITH_BLANK_REGEX.match(other[other_offset + i])
            while True:
                if is_ori_ignore:
                    new += this[ori_offset + i] if other[other_offset + i] == ' ' else ''
                    ori_offset += 1
                elif is_other_ignore:
                    new += other[other_offset + i] if this[ori_offset + i] == ' ' else ''
                    other_offset += 1

                is_ori_ignore = REPLACE_WITH_BLANK_REGEX.match(this[ori_offset + i])
                is_other_ignore = REPLACE_WITH_BLANK_REGEX.match(other[other_offset + i])

                if not is_ori_ignore and not is_other_ignore:
                    break

            if other[other_offset + i] != ' ':
                new += other[other_offset + i]
            else:
                new += this[ori_offset + i]
        return ReceiptText(new, self.position, self.justify)
