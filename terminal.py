class Terminal:
    def move_cursor(self, x, y):
        print(f"\033[{y};{x}H", end="")

    def clear_screen(self):
        print("\033[2J", end="")

    def clear_line(self):
        print("\033[2K", end="")