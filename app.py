import os
from dotenv import load_dotenv
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.project_repository import ProjectRepository
from lib.project import Project

# Create a new Flask app
app = Flask(__name__)

load_dotenv()

# == Your Routes Here ==


@app.route('/')
def get_root():
    return render_template('index.html')


# @app.route('/projects/<id>')
# def get_message_by_user_id(id):
#     connection = get_flask_database_connection(app)
#     project_repository = ProjectRepository(connection)
#     projects = project_repository.find_by_id(id)
#     return render_template('project.html', projects=projects)

@app.route('/profile-card')
def get_profile_card():
    # We use `render_template` to send the user the file `emoji.html`
    # But first, it gets processed to look for placeholders like {{ emoji }}
    # These placeholders are replaced with the values we pass in as arguments
    return render_template('profile-card.html')


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    print(os.environ['PORT'])
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
