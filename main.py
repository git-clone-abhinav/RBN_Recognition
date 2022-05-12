from fd_adv import *
from pytess import *

print(get_torso('images', '8', 'jpg'))
print(get_text(get_torso('images', '8', 'jpg')))