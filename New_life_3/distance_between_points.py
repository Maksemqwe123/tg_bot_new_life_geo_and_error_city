import h3
from geolocation import loc_geo
import re
metrix_1 = []

# Point one
lat1 = 52.473507
lon1 = 31.02713
points_1 = (lat1, lon1)

# Point two
# lat2 = 52.4321132
# lon2 = 31.02713
# points_2 = (lat2, lon2)

for i in loc_geo:
    ab = loc_geo[:]
    ab.append(points_1)
    ab.sort()
    ab_index = ab.index(points_1) - 1 if ab.index(points_1) > 0 else 0

    distance = h3.point_dist(points_1, i, unit='m')  # to get distance in meters
    # print(i, round(distance))
    metrix = (round(distance))
    print(f'Дистанция между точка {metrix} m')
    metrix_1.append(metrix)
print(min(metrix_1))



# # What you were looking for
# dist = mpu.haversine_distance((lat1, lon1), (lat2, lon2))
# print(dist)  # gives 278.45817507541943.
# x = hs.haversine(points_1, points_2)
# print(f'The distance is {x} km')


