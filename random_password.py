import numpy as np
from string import ascii_letters, digits

def password_generator(length: int=8):
    common = ascii_letters + digits + '+-._'
    random_idx = np.random.randint(0, (len(common) - 1), size=length)
    return ''.join(common[x] for x in random_idx)
