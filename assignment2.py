import time
from flyt_python import api

# Connect to FlytSIM
flyt = api.navigation(timeout=120000)  # 2 minutes timeout

# Wait for 3 seconds for initialization
time.sleep(3)

# Take off at 10m altitude
flyt.take_off(altitude=10.0)

# Move in a triangle trajectory
side_length = 10.0
height = 10.0
flyt.move_distance(x=side_length, y=0, z=0)
flyt.move_distance(x=-side_length/2, y=side_length*(3**0.5)/2, z=0)
flyt.move_distance(x=-side_length/2, y=-side_length*(3**0.5)/2, z=0)

# Land the drone
flyt.land(async=False)
