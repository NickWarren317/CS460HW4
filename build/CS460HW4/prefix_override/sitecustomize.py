import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/nickwarren/Misc/CS460HW4/install/CS460HW4'
