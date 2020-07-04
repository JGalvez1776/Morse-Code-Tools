import time
try:
    import winsound
except ImportError:
    print('At the moment the program only works on Windows :/')

def output_morse(data, duration):
    for char in data:
        if char == '.':
            short(duration)
        elif char == '-':
            long(duration)
        elif char == ' ':
            space(duration)

def short(duration):
    winsound.Beep(2500, duration)

def long(duration):
    winsound.Beep(2500, duration * 3)

def space(duration):
    time.sleep(duration / 1000) # sleep() uses seconds and duration is in milisecondss