from exif import Image


import re

def dms2dec(dms):

    degree = dms[0]
    minute = dms[1]
    second = dms[2]

    return int(degree) + float(minute) / 60 + float(second) / 3600
 
with open("sample.jpg", "rb") as f:
    img = Image(f)
    # print(img)
 
print(img.has_exif)
print(img.gps_altitude_ref, img.model, img.datetime)
 
print(img.gps_latitude, img.gps_longitude)
print(type(img.gps_latitude), type(img.gps_longitude))

print(dms2dec(img.gps_latitude))
print(dms2dec(img.gps_longitude))

