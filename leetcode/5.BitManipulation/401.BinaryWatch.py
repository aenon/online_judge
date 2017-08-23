# 401. Binary Watch 

# A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).

# Each LED represents a zero or one, with the least significant bit on the right.

# off         off         on          on
# off     on      on      off     off     on 

# For example, the above binary watch reads "3:25".

# Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.

# Example:

# Input: n = 1
# Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]

# Note:

#     The order of output does not matter.
#     The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
#     The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".


class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        The bin() method
        """
        return_list = []
        for hour in range(12):
            for minute in range(60):
                if sum(map(lambda number: int(bin(number)[2:].count('1')), [hour, minute])) == num:
                    return_list += [str(hour) + ":" + str(minute).zfill(2)]
        return return_list

class Solution1(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        x = x & (x - 1): turn off the rightmost 1
        """
        
        def bit_count(binnum):
            count = 0
            while binnum:
                binnum  &= binnum - 1
                count += 1
            return count
        
        return_list = []
        for hour in range(12):
            for minute in range(60):
                if bit_count(hour) + bit_count(minute) == num:
                    return_list += ['{}:{}'.format(str(hour), str(minute).zfill(2))]
        return return_list

class Solution2(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        
        def bit_count(binnum):
            count = 0
            while binnum:
                binnum  &= binnum - 1
                count += 1
            return count
        return ['{}:{}'.format(str(hour), str(minute).zfill(2)) for hour in range(12) for minute in range(60) if bit_count(hour) + bit_count(minute) == num]