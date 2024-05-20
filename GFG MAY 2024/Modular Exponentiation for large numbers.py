class Solution:
	def PowMod(self, x, n, m):
		# Code here
		def mod_exp(base, exponent, mod):
            result = 1
            base = base % mod  # Handle the case where base is greater than mod
            while exponent > 0:
                # If exponent is odd, multiply the base with the result
                if (exponent % 2) == 1:
                    result = (result * base) % mod
                # Now exponent must be even
                exponent = exponent >> 1  # Divide the exponent by 2
                base = (base * base) % mod  # Square the base
            return result
        
        return mod_exp(x, n, m)
