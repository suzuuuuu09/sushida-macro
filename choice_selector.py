from msvcrt import getch

class ChoiceSelector:
    def __init__(self, menu_options, menu_start_row, menu_selected_index=0):
        self.menu_options = menu_options
        self.menu_selected_index = menu_selected_index
        self.menu_start_row = menu_start_row

    def display_menu(self):
        print("\033[2J")  # Clear the screen
        for i, option in enumerate(self.menu_options):
            if i == self.menu_selected_index:
                print(f"\033[{self.menu_start_row};{i*10 + 5}H\033[33m> {option}\033[0m", end='', flush=True)
            else:
                print(f"\033[{self.menu_start_row};{i*10 + 5}H  {option}", end='', flush=True)

    def run(self):
        self.display_menu()
        while True:
            key = ord(getch())
            if key == 75:  # Left arrow key
                if self.menu_selected_index > 0:
                    self.menu_selected_index -= 1
                    self.display_menu()
            elif key == 77:  # Right arrow key
                if self.menu_selected_index < len(self.menu_options) - 1:
                    self.menu_selected_index += 1
                    self.display_menu()
            elif key == 13:  # Enter key
                break
        print("\n")
        return self.menu_options[self.menu_selected_index]