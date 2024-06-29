# Terminal Snake Game 🐍

## Description

This is a simple implementation of the classic Snake game, designed to run in a terminal environment. The game is written in Python and uses the `curses` library for terminal manipulation and keyboard input handling.

## Features

- Classic Snake gameplay
- Terminal-based interface
- Keyboard arrow key controls
- Randomly generated food
- Game over when the snake hits the wall or itself

## Requirements

- Python 3.x
- `curses` library (usually pre-installed on Unix-based systems)

## Installation

1. Ensure you have Python 3.x installed on your system.
2. Clone this repository or download the `snake.py` file.

```bash
git clone https://github.com/yourusername/terminal-snake.git
cd terminal-snake
```

## How To Play
1. Open a terminal and navigate to the directory containing snake.py.
2. Run the game using Python:
```
python snake.py
```
3. Use the arrow keys to control the snake:
  * ↑ (Up Arrow): Move up
  * ↓ (Down Arrow): Move down
  * ← (Left Arrow): Move left
  * → (Right Arrow): Move right
4. Eat the food (π symbol) to grow the snake.
5. Avoid hitting the walls or the snake's own body.
6. The game ends when the snake collides with the wall or itself.

## Customisation
You can modify the game's speed by changing the `w.timeout(100)` value in the code. A lower value will make the game faster.

## Note for Windows Users
The curses library is not natively available on Windows. If you're using Windows, you may need to install a compatible version of curses, such as `windows-curses`:
```
pip install windows-curses
```

## Contributing
Feel free to fork this project and submit pull requests with improvements or bug fixes.

## License
This project is open source and available under the MIT License.

## Author
[@2sayle]

Enjoy the game!😁 





