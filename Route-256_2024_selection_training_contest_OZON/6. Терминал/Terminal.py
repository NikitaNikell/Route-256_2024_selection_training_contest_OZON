class Terminal:
    def __init__(self):
        self.lines = ['']
        self.cursor_x = 0
        self.cursor_y = 0

    def execute_command(self, command):
        for char in command:
            if char == 'L':
                self.move_left()
            elif char == 'R':
                self.move_right()
            elif char == 'U':
                self.move_up()
            elif char == 'D':
                self.move_down()
            elif char == 'B':
                self.move_home()
            elif char == 'E':
                self.move_end()
            elif char == 'N':
                self.insert_newline()
            else:
                self.insert_char(char)

    def move_left(self):
        if self.cursor_x > 0:
            self.cursor_x -= 1

    def move_right(self):
        if self.cursor_x < len(self.lines[self.cursor_y]):
            self.cursor_x += 1

    def move_up(self):
        if self.cursor_y > 0:
            self.cursor_y -= 1
            if self.cursor_x > len(self.lines[self.cursor_y]):
                self.cursor_x = len(self.lines[self.cursor_y])

    def move_down(self):
        if self.cursor_y < len(self.lines) - 1:
            self.cursor_y += 1
            if self.cursor_x > len(self.lines[self.cursor_y]):
                self.cursor_x = len(self.lines[self.cursor_y])

    def move_home(self):
        self.cursor_x = 0

    def move_end(self):
        self.cursor_x = len(self.lines[self.cursor_y])

    def insert_newline(self):
        first_half = self.lines[self.cursor_y][:self.cursor_x]
        second_half = self.lines[self.cursor_y][self.cursor_x:]
        self.lines[self.cursor_y] = first_half
        self.lines.insert(self.cursor_y + 1, second_half)
        self.cursor_x = 0
        self.cursor_y += 1

    def insert_char(self, char):
        self.lines[self.cursor_y] = self.lines[self.cursor_y][:self.cursor_x] + char + self.lines[self.cursor_y][self.cursor_x:]
        self.cursor_x += 1

    def display_text(self):
        print('\n'.join(self.lines))


n = int(input())    # Количество наборов входных данных:
for i in range(n):
    terminal = Terminal()
    terminal.execute_command(input())   # Введите последовательность символов для обработки:
    terminal.display_text()
    print('-')


# terminal = Terminal()
# terminal.execute_command('otLLLrRuEe256LLLN')
# terminal.execute_command('LRLUUDE')
# terminal.execute_command('itisatest')
# terminal.execute_command('abNcdLLLeUfNxNx')
# terminal.display_text()
