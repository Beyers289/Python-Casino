# 🎰 Python Casino Gaming Platform

A comprehensive command-line casino simulation featuring multiple gambling games with persistent user accounts, secure authentication, and real-time balance tracking.

## 🌟 Features

- **Multi-Game Platform**: Currently includes slots with modular architecture for easy game expansion
- **User Authentication**: Secure login/registration system with password hashing
- **Persistent Data**: SQLite database storing user accounts, balances, and game statistics
- **Realistic Game Mechanics**: Probability-based slot machine with weighted symbols and dynamic payouts
- **Balance Management**: Real-time balance tracking with automatic saving
- **Modular Design**: Clean separation between game logic, database operations, and user interface

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Installation

1. **Clone the repository**
   
   ```bash
   git clone https://github.com/yourusername/python-casino.git
   cd python-casino
   ```
1. **Install required dependencies**
   
   ```bash
   pip install bcrypt
   ```

## 📊 Database Schema

The application uses SQLite with the following table structure:

### Users Table
```sql
CREATE TABLE users (
    ID INT PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);
```
### Gamblers Table
```sql
CREATE TABLE gamblers (
    user_ID INT,
    username TEXT NOT NULL,
    balance REAL
);
```

### Trigger create_gambler_after_user
'''sql
CREATE TRIGGER create_gambler_after_user
AFTER INSERT ON users
FOR EACH ROW
BEGIN
    INSERT INTO gamblers (user_id, username)
    VALUES (NEW.id, NEW.username, 0);
END;
);
```


## 🎮 How to Play

### First Time Setup

1. Run `universal_casino_cli_ui.py`
1. Choose “Create New Account”
1. Enter desired username and password
1. Set your starting balance
1. Start playing!

### Returning Players

1. Run `universal_casino_cli_ui.py`
1. Choose “Login”
1. Enter your credentials
1. Your saved balance and stats will be loaded

### Slots Game

- Place your bet (must not exceed current balance)
- Watch the reels spin with weighted probability outcomes
- Win based on symbol combinations:
  - **Three of a kind**: 5x to 250x bet multiplier
  - **Two of a kind**: 0.10x to 3.50x bet multiplier

## 🛠️ Technical Details

### Game Mechanics

- **Symbol Weights**: 🍒 (40%), 🍉 (25%), 🎄 (18%), 💎 (12%), 🌹 (5%)
- **Payout System**: Dynamic multipliers based on symbol rarity
- **Balance Validation**: Prevents overbetting and tracks wins/losses

### Security Features

- **Password Hashing**: Uses bcrypt for secure password storage
- **Input Validation**: Prevents invalid bets and malicious input
- **Data Persistence**: Automatic saving prevents data loss

### Architecture

- **Object-Oriented Design**: Clean class structure with separation of concerns
- **Modular Components**: Easy to extend with additional casino games
- **Database Abstraction**: Centralized data management

## 🔮 Future Enhancements

- [ ] GUI implementation using PyQt or Tkinter
- [ ] Additional casino games (Blackjack, Poker, Roulette)
- [ ] Advanced player statistics and analytics
- [ ] Sound effects and animations
- [ ] Multiplayer functionality
- [ ] Web-based interface option

## 🤝 Contributing

1. Fork the repository
1. Create a feature branch (`git checkout -b feature/new-game`)
1. Commit your changes (`git commit -am 'Add new casino game'`)
1. Push to the branch (`git push origin feature/new-game`)
1. Create a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🐛 Known Issues

- Currently single-player only
- Text-based interface (GUI planned for future release)
- Limited to local database storage

## 📞 Contact

- GitHub: @Beyers289 (https://github.com/Beyers289)
- Email: natebeyer53@gmail.com

-----

**Enjoy responsibly! This is for educational purposes only.** 🎲