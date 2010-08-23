from django.test import TestCase

from shorturl import baseconv

class BaseRangeTests(TestCase):

    def setUp(self):
        self.range = baseconv.BaseRange("a-z")
    
    def test_base_range_repr(self):
        self.assertEqual(repr(self.range), "<BaseRange:a-z>")

    def test_base_range_first_ord(self):
        self.assertEqual(self.range.first_ord, 97)
    
    def test_base_range_last_ord(self):
        self.assertEqual(self.range.last_ord, 122)

    def test_base_range_len(self):
        self.assertEqual(len(self.range), 123 - 97)

    def test_base_range_contains(self):
        self.assert_('a' in self.range)
        self.assert_('z' in self.range)
        self.assert_(99 in self.range)
        self.assert_(96 not in self.range)
        self.assert_(123 not in self.range)

    def test_base_range_value(self):
        self.assertEqual(self.range.value_of('a'), 0)
        self.assertEqual(self.range.value_of('z'), 25)


class UnaryBaseRangeTests(TestCase):

    def setUp(self):
        self.range = baseconv.BaseRange('a')

    def test_unary_base_range_len(self):
        self.assertEqual(len(self.range), 1)

    def test_unary_base_range_contains(self):
        self.assert_('a' in self.range)
        self.assert_('b' not in self.range)

    def test_unary_base_range_value(self):
        self.assertEqual(self.range.value_of('a'), 0)

    def test_unary_base_range_invalid_value(self):
        self.assertRaises(ValueError, self.range.value_of, ('b',))


class BaseConverterTests(TestCase):
    
    def setUp(self):
        self.converter = baseconv.BaseConverter("0-1")

    def test_base_convert_simple_base(self):
        self.assertEqual(self.converter.base, 2)

    def test_base_convert_value(self):
        self.assertEqual(self.converter.value_of('0'), 0)
        self.assertEqual(self.converter.value_of('1'), 1)

    def test_base_convert_to_decimal(self):
        self.assertEqual(self.converter.to_decimal('100'), 4)

    def test_base_convert_digit_for(self):
        self.assertEqual(self.converter.digit_for(0), '0')
        self.assertEqual(self.converter.digit_for(1), '1')

    def test_base_convert_from_decimal(self):
        self.assertEqual(self.converter.from_decimal(4), '100')


class HexConverterTests(TestCase):
    
    def setUp(self):
        self.converter = baseconv.BaseConverter("0-9,A-F")

    def test_hex_convert_to_decimal_A(self):
        self.assertEqual(self.converter.to_decimal('A'), 10)

    def test_hex_convert_to_decimal_2A(self):
        self.assertEqual(self.converter.to_decimal('9F'), 159)

    def test_hex_convert_from_decimal_10(self):
        self.assertEqual(self.converter.from_decimal(10), 'A')

    def test_hex_convert_from_decimal_159(self):
        self.assertEqual(self.converter.from_decimal(159), '9F')


class Base62ConverterTests(TestCase):

    def setUp(self):
        self.converter = baseconv.b62

    def test_b62_convert_to_decimal_9Zz(self):
        self.assertEqual(self.converter.to_decimal('9Zz'), 36827)

    def test_b62_convert_from_decimal_36827(self):
        self.assertEqual(self.converter.from_decimal(36827), '9Zz')

