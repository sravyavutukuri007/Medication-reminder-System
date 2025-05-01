# Medication Reminder System

This is a Medication Reminder System web application designed to help users manage and schedule their medications efficiently. The system includes features such as adding and editing medications, smart reminders, and user-friendly interfaces.

## 🗂 Project Structure

```
csp/
├── app.py                  # Main application entry point (Flask server)
├── init_db.py              # Script to initialize the SQLite database
├── scheduler.py            # Schedules reminders (possibly with APScheduler or similar)
├── database.db             # SQLite database storing user and medication data
├── static/
│   └── style.css           # CSS styles for the web interface
├── templates/
│   ├── index.html          # Homepage or dashboard
│   └── edit.html           # Page to edit medication details
└── __pycache__/            # Compiled Python bytecode (ignored in most cases)
```

## 💡 Features

- Add, update, and delete medication schedules
- Smart reminders using scheduling logic
- Simple and clean UI with Flask and HTML/CSS
- SQLite database for local storage

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- `pip` package manager

### Installation

1. Clone the repository or extract the ZIP.
2. Navigate to the `csp` directory:
   ```bash
   cd csp
   ```
3. Install dependencies (if any):
   ```bash
   pip install flask apscheduler
   ```
4. Initialize the database:
   ```bash
   python init_db.py
   ```
5. Run the application:
   ```bash
   python app.py
   ```
6. Open your browser and navigate to `http://127.0.0.1:5000`.

## 🛠 Technologies Used

- **Python** (Flask for web framework)
- **SQLite** (for local database)
- **HTML/CSS** (for frontend)
- **APScheduler** or similar (for scheduling)

## 📁 Notes

- Do not modify `__pycache__` or `database.db` manually.
- Customize styles in `static/style.css`.
- Add more templates as needed under `templates/`.
