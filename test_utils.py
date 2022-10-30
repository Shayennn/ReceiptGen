from unittest import TestCase

from utils import count_thai_word_space


class UtilsTests(TestCase):
    def test_count_thai_chars_should_return_correctly(self):
        string = "สวัสดีครับคุณครู"
        self.assertEqual(count_thai_word_space(string), 11)

    def test_count_thai_chars_should_return_correctly_with_english(self):
        string = "ABCDEF"
        self.assertEqual(count_thai_word_space(string), 6)

    def test_count_thai_chars_should_return_correctly_with_mixed_lang(self):
        string = "ABCDEFฟากากุฟ"
        self.assertEqual(count_thai_word_space(string), 12)

    def test_count_thai_chars_should_ignore_padding_space(self):
        string = "  ABCDEFฟากากุฟ  "
        self.assertEqual(count_thai_word_space(string), 12)
