# Tic Tac Toe Game

A classic two-player Tic Tac Toe game built in Python with SQL database integration for tracking game statistics.

## Features

### MVP Features
- ✅ Display a 3×3 grid
- ✅ Two players take turns (X and O)
- ✅ Restart option
- ✅ Win detection and draw detection
- ✅ SQLite database integration for statistics

### Additional Features
- Game statistics tracking (wins, losses, draws)
- Win rate calculations
- Persistent data storage
- User-friendly interface with emojis
- Input validation and error handling

## User Stories

1. **As a user, I should be able to see a 3x3 grid so I can play the game easily.**
   - The game displays a clear 3x3 grid with position numbers for easy reference

2. **As a user, I want to take turns between Player X and Player O so that both players can play fairly.**
   - Players alternate turns automatically, starting with Player X

3. **As a user, I want to see when a player wins or if it's a draw, so I know the outcome of the game.**
   - Clear win/draw messages are displayed when the game ends

4. **As a user, I want a restart button so I can play a new game without refreshing the page or rerunning the program.**
   - After each game, players can choose to play again, view statistics, or quit

## How to Run

1. Make sure you have Python 3.x installed
2. Navigate to the project directory
3. Run the game:
   ```bash
   python tictactoe.py
   ```

## How to Play

1. The game displays a 3x3 grid with position numbers (1-9)
2. Players take turns entering a position number (1-9) to place their mark
3. Player X always goes first
4. The first player to get three marks in a row (horizontally, vertically, or diagonally) wins
5. If all 9 spaces are filled without a winner, the game is a draw
6. After each game, you can:
   - Play again
   - View statistics
   - Quit the game

## Database Schema

The game uses SQLite to store game statistics:

### Games Table
- `id`: Primary key
- `winner`: 'X', 'O', or 'Draw'
- `game_date`: Timestamp of when the game was played
- `moves_count`: Number of moves made in the game

### Players Table (for future expansion)
- `id`: Primary key
- `name`: Player name
- `wins`: Number of wins
- `losses`: Number of losses
- `draws`: Number of draws

## File Structure

```
tictactoe/
├── tictactoe.py          # Main game file
├── requirements.txt      # Project dependencies
├── README.md            # This file
└── tictactoe_stats.db   # SQLite database (created when first run)
```

## Game Controls

- Enter numbers 1-9 to make a move
- Enter 'q' to quit at any time
- Follow the menu prompts after each game

Enjoy playing Tic Tac Toe! 🎮# tictactoe
