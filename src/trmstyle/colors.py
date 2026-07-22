class Color:
    ESC = "\033["
    RESET = ESC + "0m"

    # REGULAR COLORS
    FORE_RED = ESC + "31m"
    FORE_GREEN = ESC + "32m"
    FORE_BLUE = ESC + "34m"
    FORE_BLACK = ESC + "30m"
    FORE_YELLOW = ESC + "33m"
    FORE_PURPLE = ESC + "35m"
    FORE_CYAN = ESC + "36m"
    FORE_WHITE = ESC + "37m"

    # BACKGROUND COLORS
    BACK_BLACK = ESC + "40m"
    BACK_RED = ESC + "41m"
    BACK_GREEN = ESC + "42m"
    BACK_YELLOW = ESC + "43m"
    BACK_BLUE = ESC + "44m"
    BACK_PURPLE = ESC + "45m"
    BACK_CYAN = ESC + "46m"
    BACK_WHITE = ESC + "47m"
    
    # MISC
    RAINBOW = [
            FORE_RED,
            FORE_GREEN,
            FORE_BLUE,
            FORE_YELLOW,
            FORE_PURPLE
    ]
