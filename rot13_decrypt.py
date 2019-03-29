### ROT13 decrypt using codecs lib
import codecs
import sys
import os
phrase = sys.argv[1:]
str = ' '.join(phrase).replace(" ","")
decrypt_str = codecs.decode(str, 'rot_13')
print(decrypt_str)
