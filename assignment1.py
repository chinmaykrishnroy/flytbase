import time
from flyt_python import api

# Connect to FlytSIM
flyt = api.navigation(timeout=120000)  # 2 minutes timeout

# Wait for 3 seconds for initialization
time.sleep(3)

# Take off at 5m altitude
flyt.take_off(altitude=5.0)

# Move in a square trajectory
side_length = 6.5
for _ in range(4):
    flyt.move_distance(x=side_length, y=0, z=0)
    flyt.move_distance(x=0, y=side_length, z=0)
    flyt.move_distance(x=-side_length, y=0, z=0)
    flyt.move_distance(x=0, y=-side_length, z=0)

# Land the drone
flyt.land(async=False)
