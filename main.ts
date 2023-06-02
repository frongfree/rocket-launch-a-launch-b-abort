input.onButtonPressed(Button.A, function () {
    basic.clearScreen()
    basic.showNumber(9)
    basic.pause(1000)
    basic.showNumber(8)
    basic.pause(1000)
    basic.showNumber(7)
    basic.pause(1000)
    basic.showNumber(6)
    basic.pause(1000)
    basic.showNumber(5)
    basic.pause(1000)
    basic.showNumber(4)
    basic.pause(1000)
    basic.showNumber(3)
    basic.pause(1000)
    basic.showNumber(2)
    basic.pause(1000)
    basic.showNumber(1)
    basic.pause(1000)
    basic.showNumber(0)
    basic.pause(1000)
    basic.showLeds(`
        . . # . .
        . # # # .
        . # # # .
        # # # # #
        # . . . #
        `)
    basic.showLeds(`
        . # # # .
        . # # # .
        # # # # #
        # . . . #
        . . . . .
        `)
    basic.showLeds(`
        . # # # .
        # # # # #
        # . . . #
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        # # # # #
        # . . . #
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        # . . . #
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
})
input.onButtonPressed(Button.B, function () {
    basic.clearScreen()
    basic.showString("Abort!!!")
    basic.clearScreen()
    control.reset()
})
