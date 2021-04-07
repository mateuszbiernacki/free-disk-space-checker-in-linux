import os
import sys
import _smtp as smtp

if sys.platform == 'linux':
    result = os.statvfs("/")
    free_space_percent = float(result.f_bavail / result.f_blocks * 100)
    free_space_gigabytes = (result.f_bavail * result.f_bsize) / 1024 / 1024 / 1024
    print(100-free_space_percent)
    print(free_space_gigabytes)
    smtp.send_email('mateusz.biernacki@banachoutsourcing.pl', 'Available space', 'Available space: %sGB (its %s of entire disk).' % (free_space_gigabytes, free_space_percent))


else:
    print('It\'s not a linux system.')
