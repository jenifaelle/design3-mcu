import serial
import time

import protocol
from util import *

ser = serial.Serial("/dev/ttySTM32")

# kp, ki, kd
constants = [(0.014279, 0.03122, 0),  # REAR X
             (0.016946, 0.033344, 0),  # FRONT Y
             (0.016877, 0.03873, 0),  # FRONT X
             (0.01679, 0.035129, 0)  # REAR Y
             ]


def set_pid_constants(kp=0.015, ki=0.030, kd=0):
    global motor, cmd
    for motor in protocol.Motors:
        cmd = protocol.generate_set_pid_constant(motor, kp, ki, kd)
        ser.write(cmd)


if __name__ == "__main__":
    ser.read(ser.inWaiting())
    cmd_disable_pid = protocol.generate_set_pid_mode(protocol.PIDStatus.OFF)
    ser.write(cmd_disable_pid)

    set_pid_constants()

    motor = protocol.Motors.FRONT_X
    delta_t = 30  # ms
    current_speed = 5000  # tick/s
    cmd_set_speed = protocol.generate_move_command(220, 0, 0)
    ser.write(cmd_set_speed)
    ser.read(1)

    cmd = protocol.generate_test_pid(motor, delta_t, current_speed)
    ser.read(ser.inWaiting())

    time.sleep(0.050)
    ser.write(cmd)
    ser.read(1)  # dump useless header confirmation
    output = int.from_bytes(ser.read(1), byteorder='big', signed=True)
    print("Resultat pid pour moteur {}, delta_t {}ms et current_speed {}mm/s: {}%".format(motor.value, delta_t, current_speed, output))
    ser.read(1)

    cmd_reset_move = protocol.generate_move_command(0, 0, 0)
    ser.write(cmd_reset_move)

    cmd_enable_pid = protocol.generate_set_pid_mode(protocol.PIDStatus.ON)
    ser.write(cmd_enable_pid)
    exit(0)