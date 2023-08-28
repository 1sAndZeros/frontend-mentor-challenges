from lib.project import Project


class ProjectRepository:
    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all projects
    def all(self):
        rows = self._connection.execute('SELECT * from projects')
        projects = []
        for row in rows:
            item = Project(row["id"], row["name"],
                           row["description"], row["image_url"])
            projects.append(item)
        return projects

    # Find a single project by its id
    def find_by_id(self, project_id):
        rows = self._connection.execute(
            'SELECT * from projects WHERE id = %s', [project_id])
        row = rows[0]
        return Project(row["id"], row["name"],
                       row["description"], row["image_url"])

    # Create a new project
    def create(self, project):
        rows = self._connection.execute('INSERT INTO projects (name, description, image_url) VALUES (%s, %s, %s) RETURNING id', [
            project.name, project.description, project.image_url])
        row = rows[0]
        project.id = row["id"]
        return project

    # Delete a project by its id
    def delete(self, project_id):
        self._connection.execute(
            'DELETE FROM projects WHERE id = %s', [project_id])
        return None
