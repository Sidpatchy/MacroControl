# Module to house animations for MacroControl
# MacroControl by Sidpatchy

from time import sleep

# Startup animation:
def startup_animation(macropad, config):
    macropad.pixels[0] = config[0]["colour_unpressed"]
    sleep(0.1)
    macropad.pixels[1] = config[0]["colour_unpressed"]
    macropad.pixels[3] = config[0]["colour_unpressed"]
    sleep(0.1)
    macropad.pixels[2] = config[0]["colour_unpressed"]
    macropad.pixels[4] = config[0]["colour_unpressed"]
    macropad.pixels[6] = config[0]["colour_unpressed"]
    sleep(0.1)
    macropad.pixels[5] = config[0]["colour_unpressed"]
    macropad.pixels[7] = config[0]["colour_unpressed"]
    macropad.pixels[9] = config[0]["colour_unpressed"]
    sleep(0.1)
    macropad.pixels[8] = config[0]["colour_unpressed"]
    macropad.pixels[10] = config[0]["colour_unpressed"]
    sleep(0.1)
    macropad.pixels[11] = config[0]["colour_unpressed"]
    sleep(0.1)
    macropad.pixels.fill((0, 0, 0))
    sleep(0.2)
    macropad.pixels.fill(config[0]["colour_unpressed"])
    sleep(0.2)
    macropad.pixels.fill((0, 0, 0))
    sleep(0.2)
    macropad.pixels.fill(config[0]["colour_unpressed"])