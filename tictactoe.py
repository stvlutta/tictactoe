import sqlite3
import os
from datetime import datetime

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
        self.game_over = False
        self.winner = None
        self.db_file = 'tictactoe_stats.db'
        self.init_database()
    
    def init_database(self):
        """Initialize SQLite database for game statistics"""
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS games (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                winner TEXT,
                game_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                moves_count INTEGER
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS players (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE,
                wins INTEGER DEFAULT 0,
                losses INTEGER DEFAULT 0,
                draws INTEGER DEFAULT 0
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def display_board(self):
        """Display the current game board"""
        print("\n" + "="*30)
        print("    TIC TAC TOE GAME")
        print("="*30)
        print(f"\nCurrent Player: {self.current_player}")
        print("\nBoard positions (1-9):")
        print(" 1 | 2 | 3 ")
        print("---|---|---")
        print(" 4 | 5 | 6 ")
        print("---|---|---")
        print(" 7 | 8 | 9 ")
        print("\nCurrent board:")
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print("---|---|---")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]} ")
        print("---|---|---")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]} ")
        print()
    
    def make_move(self, position):
        """Make a move at the specified position"""
        if self.board[position] == ' ' and not self.game_over:
            self.board[position] = self.current_player
            return True
        return False
    
    def check_winner(self):
        """Check if there's a winner or if the game is a draw"""
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        
        for combo in winning_combinations:
            if (self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' '):
                self.winner = self.board[combo[0]]
                self.game_over = True
                return True
        
        if ' ' not in self.board:
            self.game_over = True
            self.winner = 'Draw'
            return True
        
        return False
    
    def switch_player(self):
        """Switch to the other player"""
        self.current_player = 'O' if self.current_player == 'X' else 'X'
    
    def save_game_result(self):
        """Save game result to database"""
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        
        moves_count = sum(1 for cell in self.board if cell != ' ')
        
        cursor.execute('''
            INSERT INTO games (winner, moves_count)
            VALUES (?, ?)
        ''', (self.winner, moves_count))
        
        conn.commit()
        conn.close()
    
    def get_statistics(self):
        """Get game statistics from database"""
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT 
                COUNT(*) as total_games,
                SUM(CASE WHEN winner = 'X' THEN 1 ELSE 0 END) as x_wins,
                SUM(CASE WHEN winner = 'O' THEN 1 ELSE 0 END) as o_wins,
                SUM(CASE WHEN winner = 'Draw' THEN 1 ELSE 0 END) as draws
            FROM games
        ''')
        
        stats = cursor.fetchone()
        conn.close()
        
        return {
            'total_games': stats[0] if stats[0] else 0,
            'x_wins': stats[1] if stats[1] else 0,
            'o_wins': stats[2] if stats[2] else 0,
            'draws': stats[3] if stats[3] else 0
        }
    
    def display_statistics(self):
        """Display game statistics"""
        stats = self.get_statistics()
        print("\n" + "="*30)
        print("    GAME STATISTICS")
        print("="*30)
        print(f"Total Games Played: {stats['total_games']}")
        print(f"Player X Wins: {stats['x_wins']}")
        print(f"Player O Wins: {stats['o_wins']}")
        print(f"Draws: {stats['draws']}")
        
        if stats['total_games'] > 0:
            x_win_rate = (stats['x_wins'] / stats['total_games']) * 100
            o_win_rate = (stats['o_wins'] / stats['total_games']) * 100
            draw_rate = (stats['draws'] / stats['total_games']) * 100
            
            print(f"\nWin Rates:")
            print(f"Player X: {x_win_rate:.1f}%")
            print(f"Player O: {o_win_rate:.1f}%")
            print(f"Draws: {draw_rate:.1f}%")
        print("="*30)
    
    def reset_game(self):
        """Reset the game to initial state"""
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
        self.game_over = False
        self.winner = None
    
    def play(self):
        """Main game loop"""
        print("Welcome to Tic Tac Toe!")
        
        while True:
            self.display_board()
            
            if self.game_over:
                if self.winner == 'Draw':
                    print("🤝 It's a draw!")
                else:
                    print(f"🎉 Player {self.winner} wins!")
                
                self.save_game_result()
                
                while True:
                    choice = input("\nWhat would you like to do?\n1. Play again\n2. View statistics\n3. Quit\nEnter choice (1-3): ").strip()
                    
                    if choice == '1':
                        self.reset_game()
                        break
                    elif choice == '2':
                        self.display_statistics()
                        input("\nPress Enter to continue...")
                    elif choice == '3':
                        print("Thanks for playing! Goodbye! 👋")
                        return
                    else:
                        print("Invalid choice. Please enter 1, 2, or 3.")
                
                continue
            
            try:
                position = input(f"Player {self.current_player}, enter position (1-9) or 'q' to quit: ").strip().lower()
                
                if position == 'q':
                    print("Thanks for playing! Goodbye! 👋")
                    break
                
                position = int(position) - 1
                
                if position < 0 or position > 8:
                    print("❌ Invalid position! Please enter a number between 1 and 9.")
                    continue
                
                if self.make_move(position):
                    if self.check_winner():
                        continue
                    self.switch_player()
                else:
                    print("❌ That position is already taken! Choose another position.")
                    
            except ValueError:
                print("❌ Invalid input! Please enter a number between 1 and 9.")
            except KeyboardInterrupt:
                print("\n\nGame interrupted. Goodbye! 👋")
                break

def main():
    game = TicTacToe()
    game.play()

if __name__ == "__main__":
    main()