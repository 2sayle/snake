import curses
import random
import locale

locale.setlocale(locale.LC_ALL, '')

def main(stdscr):
    # Initial setup
    curses.curs_set(0)
    sh, sw = stdscr.getmaxyx()
    w = curses.newwin(sh, sw, 0, 0)
    w.keypad(1)
    w.timeout(100)

    # Initial snake position
    snk_x = sw // 4
    snk_y = sh // 2
    snake = [
        [snk_y, snk_x],
        [snk_y, snk_x - 1],
        [snk_y, snk_x - 2]
    ]

    # Initial food position
    food = [sh // 2, sw // 2]
    w.addch(food[0], food[1], '@')

    # Initial direction
    key = curses.KEY_RIGHT

    while True:
        next_key = w.getch()
        
        # Prevent reversing direction
        if next_key != -1:
            if (key == curses.KEY_DOWN and next_key != curses.KEY_UP) or \
               (key == curses.KEY_UP and next_key != curses.KEY_DOWN) or \
               (key == curses.KEY_LEFT and next_key != curses.KEY_RIGHT) or \
               (key == curses.KEY_RIGHT and next_key != curses.KEY_LEFT):
                key = next_key

        # Check if the player has lost
        if (snake[0][0] in [0, sh-1] or
            snake[0][1] in [0, sw-1] or
            snake[0] in snake[1:]):
            curses.endwin()
            quit()

        # Determine the new head of the snake
        new_head = [snake[0][0], snake[0][1]]

        if key == curses.KEY_DOWN:
            new_head[0] += 1
        if key == curses.KEY_UP:
            new_head[0] -= 1
        if key == curses.KEY_LEFT:
            new_head[1] -= 1
        if key == curses.KEY_RIGHT:
            new_head[1] += 1

        snake.insert(0, new_head)

        # Check if the snake has eaten the food
        if snake[0] == food:
            food = None
            while food is None:
                nf = [
                    random.randint(1, sh-2),
                    random.randint(1, sw-2)
                ]
                food = nf if nf not in snake else None
            w.addch(food[0], food[1], '@')
        else:
            tail = snake.pop()
            w.addch(tail[0], tail[1], ' ')

        # Redraw the snake
        for i, segment in enumerate(snake):
            if i == 0:
                w.addch(segment[0], segment[1], 'O')
            else:
                w.addch(segment[0], segment[1], 'o')

        # Redraw the food to ensure it's always visible
        w.addch(food[0], food[1], '@')

        w.refresh()

curses.wrapper(main)