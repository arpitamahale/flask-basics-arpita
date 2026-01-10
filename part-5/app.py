"""
Part 5: Mini Project - Personal Website with Flask
===================================================
A complete personal website using everything learned in Parts 1-4.

How to Run:
1. Make sure venv is activated
2. Run: python app.py
3. Open browser: http://localhost:5000
"""

from flask import Flask, render_template

app = Flask(__name__)

# =============================================================================
# YOUR DATA - Customize this section with your own information!
# =============================================================================

PERSONAL_INFO = {
    'name': 'Arpita',
    'title': 'Software Engineer',
    'bio': 'A software engineer with a passion for building web applications.',
    'email': 'arpita@example.com',
    'github': 'https://github.com/arpita',
    'linkedin': 'https://linkedin.com/in/arpita',
}

SKILLS = [
    {'name': 'Python', 'level': 90},
    {'name': 'HTML/CSS', 'level': 85},
    {'name': 'Flask', 'level': 80},
    {'name': 'JavaScript', 'level': 70},
    {'name': 'SQL', 'level': 75},
    {'name': 'React', 'level': 65},
    {'name': 'Git', 'level': 80},
]

PROJECTS = [
    {'id': 1, 'name': 'Personal Website', 'description': 'A Flask-powered personal portfolio website.', 'tech': ['Python', 'Flask', 'HTML', 'CSS'], 'status': 'Completed'},
    {'id': 2, 'name': 'Todo App', 'description': 'A simple task management application.', 'tech': ['Python', 'Flask', 'SQLite'], 'status': 'In Progress'},
    {'id': 3, 'name': 'Weather Dashboard', 'description': 'Display weather data from an API.', 'tech': ['Python', 'Flask', 'API'], 'status': 'Planned'},
    {'id': 4, 'name': 'E-commerce API', 'description': 'A RESTful API for an e-commerce platform.', 'tech': ['Python', 'Flask', 'SQL'], 'status': 'Completed'},
    {'id': 5, 'name': 'Blog Platform', 'description': 'A multi-user blog platform.', 'tech': ['Python', 'Flask', 'React'], 'status': 'In Progress'},
]

BLOG_POSTS = [
    {'id': 1, 'title': 'My First Blog Post', 'content': 'This is the content of my first blog post.'},
    {'id': 2, 'title': 'Flask is Fun', 'content': 'I am learning so much about web development with Flask.'},
]


# =============================================================================
# ROUTES
# =============================================================================

@app.route('/')
def home():
    return render_template('index.html', info=PERSONAL_INFO)


@app.route('/about')
def about():
    return render_template('about.html', info=PERSONAL_INFO, skills=SKILLS)


@app.route('/projects')
def projects():
    return render_template('projects.html', info=PERSONAL_INFO, projects=PROJECTS)


@app.route('/project/<int:project_id>')  # Dynamic route for individual project
def project_detail(project_id):
    project = None
    for p in PROJECTS:
        if p['id'] == project_id:
            project = p
            break
    return render_template('project_detail.html', info=PERSONAL_INFO, project=project, project_id=project_id)


@app.route('/contact')
def contact():
    return render_template('contact.html', info=PERSONAL_INFO)


@app.route('/blog')
def blog():
    return render_template('blog.html', info=PERSONAL_INFO, posts=BLOG_POSTS)


@app.route('/skill/<skill_name>')
def skill_projects(skill_name):
    projects_with_skill = [p for p in PROJECTS if skill_name in p['tech']]
    return render_template('skill.html', info=PERSONAL_INFO, skill=skill_name, projects=projects_with_skill)


if __name__ == '__main__':
    app.run(debug=True)


# =============================================================================
# PROJECT STRUCTURE:
# =============================================================================
#
# part-5/
# ├── app.py              <- You are here
# ├── static/
# │   └── style.css       <- CSS styles
# └── templates/
#     ├── base.html       <- Base template (inherited by all pages)
#     ├── index.html      <- Home page
#     ├── about.html      <- About page
#     ├── projects.html   <- Projects list
#     ├── project_detail.html <- Single project view
#     └── contact.html    <- Contact page
#
# =============================================================================

# =============================================================================
# EXERCISES:
# =============================================================================
#
# Exercise 5.1: Personalize your website
#   - Update PERSONAL_INFO with your real information
#   - Add your actual skills and projects
#   - Completed
#
# Exercise 5.2: Add a new page
#   - Create a /blog route
#   - Add blog posts data structure
#   - Create blog.html template
#   - Completed
#
# Exercise 5.3: Enhance the styling
#   - Modify static/style.css
#   - Add your own color scheme
#   - Make it responsive for mobile
#   - Completed
#
# Exercise 5.4: Add more dynamic features
#   - Create a /skill/<skill_name> route
#   - Show projects that use that skill
#   - Completed
#
# =============================================================================
