"""
Part 6: Homework - Personal To-Do List App
==========================================
See Instruction.md for full requirements.

How to Run:
1. Make sure venv is activated
2. Run: python app.py
3. Open browser: http://localhost:5000
"""
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data - your tasks list
TASKS = [
    {'id': 1, 'title': 'Learn Flask', 'status': 'Completed', 'priority': 'High'},
    {'id': 2, 'title': 'Build To-Do App', 'status': 'In Progress', 'priority': 'Medium'},
    {'id': 3, 'title': 'Push to GitHub', 'status': 'Pending', 'priority': 'Low'},
]

def get_task(task_id):
    """Helper function to find a task by its ID."""
    return next((task for task in TASKS if task['id'] == task_id), None)

@app.route('/')
def index():
    """Home page - display all tasks."""
    return render_template('index.html', tasks=TASKS)

@app.route('/add', methods=['GET', 'POST'])
def add():
    """Page with a form to add a new task."""
    if request.method == 'POST':
        title = request.form.get('title')
        priority = request.form.get('priority')
        status = request.form.get('status') # Get status from form

        # Basic validation
        if title:
            new_task = {
                'id': len(TASKS) + 1,
                'title': title,
                'status': status, # Use status from form
                'priority': priority
            }
            TASKS.append(new_task)
            return redirect(url_for('index'))
    
    return render_template('add.html')

@app.route('/task/<int:id>')
def task(id):
    """View single task details."""
    task_item = get_task(id)
    if task_item:
        return render_template('task.html', task=task_item)
    return "Task not found", 404

@app.route('/task/<int:id>/update_status', methods=['POST'])
def update_status(id):
    """Update a task's status."""
    task_item = get_task(id)
    if task_item:
        task_item['status'] = request.form.get('status')
        return redirect(url_for('index'))
    return "Task not found", 404

@app.route('/delete_completed', methods=['POST'])
def delete_completed():
    """Delete all completed tasks."""
    global TASKS
    TASKS = [task for task in TASKS if task['status'] != 'Completed']
    return redirect(url_for('index'))

@app.route('/about')
def about():
    """About the app page."""
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
