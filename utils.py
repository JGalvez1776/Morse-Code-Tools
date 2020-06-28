import winsound
import time

def output_morse(data, duration):
    for char in data:
        if char == '.':
            short(1, duration)
        elif char == '-':
            long(1, duration)
        elif char == ' ':
            space(1, duration)

# So far I am not utilizing the count parameter much. Maybe remove it doesn't get used by the end
def short(count, duration):
    if count == 0:
        return
    short(count - 1, duration)
    winsound.Beep(2500, duration)

def long(count, duration):
    if count == 0:
        return
    long(count - 1, duration)
    winsound.Beep(2500, duration * 3)

def space(count, duration):
    if count == 0:
        return
    space(count - 1, duration)
    time.sleep(duration / 1000) # Sleep is in seconds duration is in miliseconds
