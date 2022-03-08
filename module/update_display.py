# Module to update display info
# MacroControl by Sidpatchy

import terminalio
from adafruit_display_text import bitmap_label as label

# Usage
#   macropad: MacroPad, pass through the macropad variable
#   titlebar: string, name of the current screen
#   line0: string, text of line0
#   line1: string, text of line1
def update_display(macropad, title, line0="", line1="", line2="", line3=""):
    text_lines = macropad.display_text()

    text_lines[0].text = title.center(22)
    text_lines[1].text = line0.center(22)
    text_lines[2].text = line1.center(22)
    text_lines[3].text = line2.center(22)
    text_lines[4].text = line3.center(22)
    

    text_lines.show()
