def on_button_pressed_a():
    basic.clear_screen()
    basic.show_number(9)
    basic.pause(1000)
    basic.show_number(8)
    basic.pause(1000)
    basic.show_number(7)
    basic.pause(1000)
    basic.show_number(6)
    basic.pause(1000)
    basic.show_number(5)
    basic.pause(1000)
    basic.show_number(4)
    basic.pause(1000)
    basic.show_number(3)
    basic.pause(1000)
    basic.show_number(2)
    basic.pause(1000)
    basic.show_number(1)
    basic.pause(1000)
    basic.show_number(0)
    basic.pause(1000)
    basic.show_leds("""
        . . # . .
                . # # # .
                . # # # .
                # # # # #
                # . . . #
    """)
    basic.show_leds("""
        . # # # .
                . # # # .
                # # # # #
                # . . . #
                . . . . .
    """)
    basic.show_leds("""
        . # # # .
                # # # # #
                # . . . #
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        # # # # #
                # . . . #
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        # . . . #
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.clear_screen()
    basic.show_string("Abort!!!")
    basic.clear_screen()
    control.reset()
input.on_button_pressed(Button.B, on_button_pressed_b)
