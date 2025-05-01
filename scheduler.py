from datetime import datetime
import sqlite3

def check_reminders():
    now = datetime.now().strftime('%H:%M')
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    reminders = conn.execute('SELECT * FROM reminders WHERE time = ?', (now,)).fetchall()

    # Delete non-repeating
    for r in reminders:
        if r['repeat'] == 'none':
            conn.execute('DELETE FROM reminders WHERE id = ?', (r['id'],))
    conn.commit()
    conn.close()

    return [dict(r) for r in reminders]
