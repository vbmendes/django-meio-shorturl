
def get_ord_or_self(item):
    try:
        return ord(item)
    except TypeError:
        return item

class BaseRange():
    
    def __init__(self, str_range):
        range_tuple = [ord(r) for r in str_range.split('-')]
        if len(range_tuple) == 1:
            range_tuple *= 2
        self.first_ord, self.last_ord = range_tuple

    def __repr__(self):
        return "<" + self.__class__.__name__ + ":" + self.str_range + ">"

    def __len__(self):
        return 1 + self.last_ord - self.first_ord

    def __contains__(self, item):
        item = get_ord_or_self(item)
        return self.first_ord <= item <= self.last_ord

    def value_of(self, digit):
        if not digit in self:
            raise ValueError, "This digit is not contained in %s." % (repr(self))
        return get_ord_or_self(digit) - self.first_ord

    def digit_for(self, value):
        if len(self) <= value:
            raise ValueError, "This value cannot be converted for a digit of %s." % repr(self)
        else:
            return chr(self.first_ord + value)

    def str_range(self):
        return chr(self.first_ord) + "-" + chr(self.last_ord)
    str_range = property(str_range)
        

class BaseConverter(object):
    
    characters = '0-9,A-Z,a-z'
    
    def __init__(self, ranges):
        self.ranges = [BaseRange(base_range) for base_range in ranges.split(',')]

    def base(self):
        return sum([len(base_range) for base_range in self.ranges])
    base = property(base)

    def to_decimal(self, number):
        value = 0
        for i, digit in enumerate(number[::-1]):
            value += self.base ** i * self.value_of(digit) 
        return value

    def from_decimal(self, value):
        ret = ''
        decimal = 0
        while value > 0:
            remainder = value % (self.base ** (decimal + 1))
            ret = self.digit_for(remainder/(self.base ** decimal)) + ret
            value -= remainder
            decimal += 1
        return ret

    def value_of(self, digit):
        current_base = 0
        for base_range in self.ranges:
            try:
                return base_range.value_of(digit) + current_base
            except ValueError:
                pass
            current_base += len(base_range)
        raise ValueError, "This digit is not contained in any of %s digits" % repr(self)
        
    def digit_for(self, value):
        current_base = 0
        for base_range in self.ranges:
            try:
                return base_range.digit_for(value - current_base)
            except ValueError:
                pass
            current_base += len(base_range)
        raise ValueError, "This value cannot be converted to a single digit"

bin = BaseConverter("0-1")
hexconv = BaseConverter("0-9,A-F")
b62 = BaseConverter("0-9,A-Z,a-z")

