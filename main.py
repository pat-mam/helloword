def on_button_pressed_a():
    basic.show_icon(IconNames.YES)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_logo_pressed():
    basic.show_icon(IconNames.HAPPY)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def on_button_pressed_ab():
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_icon(IconNames.NO)
input.on_button_pressed(Button.B, on_button_pressed_b)


def on_forever():
    basic.show_leds("""
        # . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.pause(100)
    basic.show_leds("""
        # # . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.pause(100)
    basic.show_leds("""
        # # # . .
        . . . . .
        . # . . .
        . . . . .
        # . . . .
        """)
    basic.pause(100)
    basic.show_leds("""
        # # # # .
        . . . . .
        # . # . .
        . . . . .
        # # . . .
        """)
    basic.pause(100)
    basic.show_leds("""
        # # # # #
        . . . . .
        . # . # .
        . . . . .
        . # # # .
        """)
    basic.pause(100)
    for index in range(4):
        basic.show_leds("""
            # # # # #
            . . . . .
            . . # . #
            . . . . .
            . # # # .
            """)
        basic.pause(100)
        basic.show_leds("""
            # # # # #
            . . . . .
            # . # . .
            . . . . .
            . # # # .
            """)
        basic.pause(100)
        basic.show_leds("""
            # # # # #
            . . . . .
            . # . # .
            . . . . .
            . # # # .
            """)
        basic.pause(500)
        basic.show_leds("""
            # # # # #
            . # . # .
            . . . . .
            . . . . .
            . # # # .
            """)
        basic.pause(100)
        basic.show_leds("""
            # # # # #
            . . . . .
            . . . . .
            . # . # .
            . # # # .
            """)
        basic.pause(100)
        basic.show_leds("""
            # # # # #
            . . . . .
            . # . # .
            . . . . .
            . # # # .
            """)
        basic.pause(500)
    basic.show_leds("""
        # # # # #
        . . . . .
        . # . # .
        . . . . .
        . # # # .
        """)
    basic.pause(100)
    basic.show_leds("""
        . # # # #
        . . . . .
        . . # . #
        . . . . .
        . . # # #
        """)
    basic.pause(100)
    basic.show_leds("""
        . . # # #
        . . . . .
        . . . # .
        . . . . .
        . . . # #
        """)
    basic.pause(100)
    basic.show_leds("""
        . . . # #
        . . . . .
        . . . . #
        . . . . .
        . . . . #
        """)
    basic.pause(100)
    basic.show_leds("""
        . . . . #
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.show_string(" ")
    basic.show_string("BYE!")

basic.forever(on_forever)
