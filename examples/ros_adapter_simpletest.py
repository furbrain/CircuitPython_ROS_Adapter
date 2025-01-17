# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2025 Phil Underwood for Underwood Underground
#
# SPDX-License-Identifier: Unlicense
import sys
sys.path.insert(0,'..')
import board
import icm
import time
import digitalio
import busio
from ros_adapter import ROS_Adapter


en_pin = digitalio.DigitalInOut(board.D4)
en_pin.switch_to_output(False)
i2c_bus = busio.I2C(board.SCL, board.SDA, frequency=400_000)
device = icm.ICM20948(i2c_bus)
print("created device")
ros = ROS_Adapter.create_from_sensor(device, frame_id="map")
print(ros.msgs)
ros.run()
print("exiting")
