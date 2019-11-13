from model.project import Project
from fixture.application import Application
from model.project import Project
import pytest

def test_add_project(app):
        app.session.login("administrator", "root")
        app.project.open_manage()
        #app.project.authenticate()
        app.project.open_manage_projects()
        old_project = app.project.count()
        app.project.create_project(Project(name="name", status="release", description="description"))
        new_project = app.project.count()
        app.project.return_to_view_page()
        app.project.logout()
        # app.session.logout()
        assert old_project + 1 == new_project