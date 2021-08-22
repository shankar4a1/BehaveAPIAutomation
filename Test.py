import random
import string

char_set = string.ascii_uppercase + string.digits
print(''.join(random.sample(char_set * 6, 6)))
