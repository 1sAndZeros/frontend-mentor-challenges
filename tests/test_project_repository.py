from lib.project_repository import ProjectRepository
from lib.project import Project

"""
When we call ProjectRepository#all
We get a list of Project objects reflecting the seed data.
"""


def test_get_all_records(db_connection):
    db_connection.seed("seeds/projects.sql")
    repository = ProjectRepository(db_connection)
    projects = repository.all()
    assert projects == [
        Project(1, 'rikie@makers.com', 'rikie123', 'mypassword1', True)
    ]


"""
When we call ProjectRepository#find
We get a single Project object reflecting the seed data.
"""


def test_get_single_record(db_connection):
    db_connection.seed("seeds/projects.sql")
    repository = ProjectRepository(db_connection)
    project = repository.find_by_id(3)
    assert project == Project(3)


"""
When we call ProjectRepository#create
We get a new record in the database.
"""


def test_create_record(db_connection):
    db_connection.seed("seeds/projects.sql")
    repository = ProjectRepository(db_connection)

    repository.create(
        Project(None, 'yasien@makers.com', 'yas44', 'p4$$W0rD!'))
    projects = repository.all()
    assert projects == [
        Project(1, 'rikie@makers.com', 'rikie123', 'mypassword1', True),
        Project(2, 'denise@makers.com', 'denise321', 'thisismypassword'),
        Project(3, 'alex@makers.com', 'alex5', 'iwillnotrememberthis!'),
        Project(4, 'yasien@makers.com', 'yas44', 'p4$$W0rD!')
    ]


"""
When we call ProjectRepository#delete
We remove a record from the database.
"""


def test_delete_record(db_connection):
    db_connection.seed("seeds/projects.sql")
    repository = ProjectRepository(db_connection)
    repository.delete(2)
    projects = repository.all()
    assert projects == [
        Project(1, 'rikie@makers.com', 'rikie123', 'mypassword1', True),
        Project(3, 'alex@makers.com', 'alex5', 'iwillnotrememberthis!')
    ]
