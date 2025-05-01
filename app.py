from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3
from datetime import datetime
from scheduler import check_reminders

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    reminders = conn.execute('SELECT * FROM reminders').fetchall()
    conn.close()
    return render_template('index.html', reminders=reminders)

@app.route('/add', methods=['POST'])
def add_reminder():
    name = request.form['name']
    time = request.form['time']
    repeat = request.form.get('repeat', 'none')

    conn = get_db_connection()
    conn.execute('INSERT INTO reminders (name, time, repeat) VALUES (?, ?, ?)',
                 (name, time, repeat))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_reminder(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM reminders WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_reminder(id):
    conn = get_db_connection()
    if request.method == 'POST':
        name = request.form['name']
        time = request.form['time']
        repeat = request.form['repeat']
        conn.execute('UPDATE reminders SET name = ?, time = ?, repeat = ? WHERE id = ?',
                     (name, time, repeat, id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    reminder = conn.execute('SELECT * FROM reminders WHERE id = ?', (id,)).fetchone()
    conn.close()
    return render_template('edit.html', reminder=reminder)

@app.route('/check_reminders')
def check_reminders():
    now = datetime.now().strftime('%H:%M')
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # Get all reminders that match current time
    c.execute("SELECT id, name, repeat FROM reminders WHERE time = ?", (now,))
    due_reminders = c.fetchall()

    # Remove 'once' reminders
    for r in due_reminders:
        if r[2] == 'none':
            c.execute("DELETE FROM reminders WHERE id = ?", (r[0],))

    conn.commit()
    conn.close()

    return jsonify([{'name': r[1]} for r in due_reminders])

if __name__ == '__main__':
    app.run(debug=True)
