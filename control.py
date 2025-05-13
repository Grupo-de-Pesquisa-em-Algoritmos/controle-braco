import RPi.GPIO as gpio
import time
import threading


MOTOR_PINS = {
    0: 17,  # fservo 
    1: 27,  # sservo 
    2: 22,  # tservo 
    3: 5,   # foservo
    4: 6,   # fifservo 
    5: 19,  # sxservo (pulso)
}

gpio.setmode(gpio.BCM)
pwm_channels = {}

for motor_id, pin in MOTOR_PINS.items():
    gpio.setup(pin, gpio.OUT)
    pwm = gpio.PWM(pin, 50)
    pwm.start(0)
    pwm_channels[motor_id] = pwm


def angle_to_duty_cycle(angle): # magica
    return (angle / 180) * 10 + 2


def move_servo(motor_id, current_angle, target_angle, step=2):
    pwm = pwm_channels[motor_id]

    total_distance = abs(target_angle - current_angle)

    if total_distance == 0:
        return target_angle

    delay = 0.005

    if current_angle < target_angle:
        angle_range = range(current_angle, target_angle + 1, step)
    else:
        angle_range = range(current_angle, target_angle - 1, -step)

    # a idea eh criar um range de angulos para a transicao ser fluida

    for angle in angle_range:
        duty_cycle = angle_to_duty_cycle(angle)
        pwm.ChangeDutyCycle(duty_cycle)
        time.sleep(delay)

    # pwm.ChangeDutyCycle(angle_to_duty_cycle(target_angle))
    # time.sleep(delay)
    pwm.ChangeDutyCycle(0)

    return target_angle


current_angles = {i: 0 for i in MOTOR_PINS}
motor_locks = {motor_id: threading.Lock() for motor_id in MOTOR_PINS}


def get_angle_and_move(motor_id, angle):
    with motor_locks[motor_id]:
        current = current_angles.get(motor_id, 0)

        new_angle = move_servo(motor_id, current, angle)

        current_angles[motor_id] = new_angle


def start_thread_move(motor_id, angle):
    thread = threading.Thread(target=get_angle_and_move, args=(motor_id, angle))
    thread.start()
    return thread


def run_movement(motor_id, angle, mov_all_bitset=0):
    angle = int(angle)
    angle = max(0, min(180, angle))

    if motor_id != 6:
        # start_thread_move(motor_id, angle)
        # talvez seja lento criar nova thread pra esse movimento
        get_angle_and_move(motor_id, angle) 
        return
    for i in range(6):
        if mov_all_bitset & (1 << i):
            start_thread_move(i, angle)
