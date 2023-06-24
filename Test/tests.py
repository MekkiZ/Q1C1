"""system module."""

import unittest


class DataTest(unittest.TestCase):
    """
    param: Module with Class
    """

    def test_check_encode_each_letter_value(self):
        from controllers_part import Control
        c = Control()
        value_out = ''  # match of letter with this index = 4 last of value of first item
        # '0004, 8701, 2022-08-03, 14/16 Rue Bernard Gante, VILLEMOMBLE, 93250, KIRRMAN, rache,
        # 1325830@gmail.com'
        for count, value in enumerate(c.clean_data_and_make_object()[1]):
            value_out = value

        self.assertEqual(value_out, '4121L5Rh5')


if __name__ == '__main__':
    unittest.main()
