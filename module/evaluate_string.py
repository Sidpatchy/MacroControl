# Module to evaluate macro text optionally including escape sequences
# MacroControl by Sidpatchy

from time import sleep

def evaluate_string(macropad, string, evaluate_escape_sequences):

    if string.startswith("{launch}"):
        string = string.replace("{launch}", "")

        macropad.keyboard.press(macropad.Keycode.WINDOWS)
        macropad.keyboard.release_all()
        sleep(0.3)
        macropad.keyboard_layout.write(str(string + "\n"))
    
    else:
        macropad.keyboard_layout.write(str(string + "\n"))