import os
import sys
import _smtp as smtp

if sys.platform == 'linux':
    result = os.statvfs("/")
    free_space_percent = float(result.f_bavail / result.f_blocks * 100)
    free_space_gigabytes = (result.f_bavail * result.f_bsize) / 1024 / 1024 / 1024
    if free_space_percent > 90:
        smtp.send_email('mateusz.biernacki@banachoutsourcing.pl',
                        'Available space',
                        'Available space: %sGB (its %s of entire disk).' %
                        (round(free_space_gigabytes, 4), round(free_space_percent, 4)))


else:
    print('It\'s not a linux system.')
