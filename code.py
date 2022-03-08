# ----------------------------------------------
# |            MacroControl v1.0.0             |
# |                by Sidpatchy                |
# |                                            |
# |           Configuration Section            |
# ----------------------------------------------
# For instructions on how to edit the config, please see:
# *link*

evaluate_escape_sequences = True

config = [
    # Page 0
    {
        "page_title"  : "NumPad",
        "page_hint_0" : "Functions like a",
        "page_hint_1" : "regular numpad",
        "page_hint_2" : "(much more minimal)",

        "colour_unpressed" : (50, 50, 50),
        "colour_pressed"   : (255, 255, 255),

        "button0"  : 7,
        "button1"  : 8,
        "button2"  : 9,
        
        "button3"  : 4,
        "button4"  : 5,
        "button5"  : 6,
        
        "button6"  : 1,
        "button7"  : 2,
        "button8"  : 3,
        
        "button9"  : 0,
        "button10" : 0,
        "button11" : "."
    },

    # Page 1
    {
        "page_title" : "Letters Demo",
        "page_hint_0" : "",
        "page_hint_1" : "Letters a through l",
        "page_hint_2" : "",
        
        "colour_unpressed" : (50, 0, 0),
        "colour_pressed"   : (255, 0, 0),

        "button0"  : "a",
        "button1"  : "b",
        "button2"  : "c",
        
        "button3"  : "d",
        "button4"  : "e",
        "button5"  : "f",
        
        "button6"  : "g",
        "button7"  : "h",
        "button8"  : "i",
        
        "button9"  : "j",
        "button10" : "k",
        "button11" : "l"
    }
]


# ----------------------------------------------
# |                 *the code*                 |
# ----------------------------------------------
import displayio
import terminalio
from time import sleep
from adafruit_display_text import bitmap_label as label
from adafruit_displayio_layout.layouts.grid_layout import GridLayout
from adafruit_macropad import MacroPad

# Import modules
from module.update_display import update_display
from module.animations import startup_animation

macropad = MacroPad()

update_display(macropad, "MacroControl v1.0.0", "by Sidpatchy", "", "Loading...")
startup_animation(macropad, config)

page_number = 0
last_position = None # previous encoder position
prev_page = 0
page = config[0]

while True:

    # Page manager
    encoder_pos = macropad.encoder
    if last_position == None or encoder_pos != last_position:
        
        # Ensure no errors on initial run + avoid running this non stop while at pos 0
        if last_position == None:
            last_position = 0

        # Determine which direction the encoder moved.
        if last_position > encoder_pos:
            page_number = prev_page + 1
        elif last_position < encoder_pos:
            page_number = prev_page - 1

        # Make sure the position is in bounds. Wrap around if not.
        if page_number > (len(config) - 1):
            page_number = 0
        elif page_number < 0:
            page_number = len(config) - 1

        page = config[page_number]
        macropad.pixels.fill(page["colour_unpressed"])
        update_display(
            macropad, 
            page["page_title"],
            page["page_hint_0"],
            page["page_hint_1"],
            page["page_hint_2"]
        )

        last_position = encoder_pos
        prev_page = page_number
        

    # Keypress handler
    key_press_event = macropad.keys.events.get()
    if key_press_event:
        key_number = key_press_event.key_number

        if key_press_event.pressed:
            macropad.pixels[key_number] = page["colour_pressed"]
            macropad.keyboard_layout.write(str(page[f"button{key_number}"]))

        else:
            macropad.pixels[key_number] = page["colour_unpressed"]
