class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Remove leading and trailing whitespaces
        s = s.strip()
        
        # Define flags to track presence of different components
        has_digit = False
        has_decimal = False
        has_exponent = False
        
        # Iterate through each character in the string
        for i, char in enumerate(s):
            if char.isdigit():
                # If the character is a digit, update the flag
                has_digit = True
            elif char == '.':
                # If the character is a decimal point, it can only appear once and cannot be followed by another decimal point or exponent
                if has_decimal or has_exponent:
                    return False
                has_decimal = True
            elif char in ('e', 'E'):
                # If the character is an exponent, it can only appear once and must be preceded by a digit
                if has_exponent or not has_digit:
                    return False
                has_exponent = True
                has_digit = False  # Reset the digit flag as the exponent must be followed by an integer
            elif char in ('+', '-'):
                # If the character is a sign, it can only appear at the beginning of the string or after an exponent
                if i != 0 and s[i - 1] not in ('e', 'E'):
                    return False
            else:
                # If the character is not a digit, decimal point, exponent, or sign, it's invalid
                return False
        
        # If there's at least one digit and no invalid characters are encountered, it's a valid number
        return has_digit
