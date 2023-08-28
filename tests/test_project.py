from lib.project import Project


def test_project_constructs():
    project = Project(1, "Password Generator", "Generates a password with different characters, symbols etc. of a given length",
                      "https://unsplash.com/photos/FnA5pAzqhMM")
    assert project.id == 1
    assert project.name == "Password Generator"
    assert project.description == "Generates a password with different characters, symbols etc. of a given length"
    assert project.image_url == "https://unsplash.com/photos/FnA5pAzqhMM"


def test_projects_format_nicely():
    project = Project(1, "Password Generator", "Generates a password with different characters, symbols etc. of a given length",
                      "https://unsplash.com/photos/FnA5pAzqhMM")
    assert str(project) == "Project 1 - Password Generator"
    # Try commenting out the `__repr__` method in lib/project.py
    # And see what happens when you run this test again.


def test_projects_are_equal():
    project1 = Project(1, "Password Generator", "Generates a password with different characters, symbols etc. of a given length",
                       "https://unsplash.com/photos/FnA5pAzqhMM")
    project2 = Project(1, "Password Generator", "Generates a password with different characters, symbols etc. of a given length",
                       "https://unsplash.com/photos/FnA5pAzqhMM")
    assert project1 == project2
