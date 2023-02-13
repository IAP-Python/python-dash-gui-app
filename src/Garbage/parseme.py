import numpy as np
from io import StringIO

text = StringIO("Beam1_SCOPE4-5172_11 Beam1_SCOPE3-5172_11 Beam2_SCOPE4-5172_12")

beam = "Beam"


# regexp = r"(\d+)\s+(...)"  # match [digits, whitespace, anything]
regexp = r""+beam+"\d+"

# output = np.fromregex(text, regexp, [('num', np.int64), ('key', 'S3')])
output = np.fromregex(text, regexp, [('beam', np.dtype('U19'))])
print(output)
print(output['beam'])
