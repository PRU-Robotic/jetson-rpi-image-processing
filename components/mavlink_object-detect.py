# with object detection
from pymavlink import mavutil

# Create the connection
master = mavutil.mavlink_connection('udpin:0.0.0.0:14550')
# Wait a heartbeat before sending commands
master.wait_heartbeat()

# Arm
# master.arducopter_arm() or:
master.mav.command_long_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
    0,
    1, 0, 0, 0, 0, 0, 0)

# wait until arming confirmed (can manually check with master.motors_armed())
print("Waiting for the vehicle to arm")
master.motors_armed_wait()
print('Armed!')

# Start object detection loop
while True:
    # Perform object detection
    confidence = perform_object_detection()
    if confidence > 0.5:
        # Object detected, stop the vehicle
        master.mav.set_mode_send(
            master.target_system,
            mavutil.mavlink.MAV_MODE_FLAG_CUSTOM_MODE_ENABLED,
            mavutil.mavlink.MAV_MODE_AUTO_DISARMED)
        print("Object detected, vehicle stopped.")
    else:
        # No object detected, start the vehicle
        master.mav.set_mode_send(
            master.target_system,
            mavutil.mavlink.MAV_MODE_FLAG_CUSTOM_MODE_ENABLED,
            mavutil.mavlink.MAV_MODE_AUTO_ARMED)
        print("No object detected, vehicle started.")

    # Disarm
    # master.arducopter_disarm() or:
    master.mav.command_long_send(
        master.target_system,
        master.target_component,
        mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
        0,
        0, 0, 0, 0, 0, 0, 0)

    # wait until disarming confirmed
    master.motors_disarmed_wait()