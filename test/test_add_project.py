from data.project import testdata
from model.project import Project
import pytest

@pytest.mark.parametrize("project",testdata, ids=[repr(x) for x in testdata])
def test_add_project(app, project):
        app.session.login("administrator", "root")
        app.project.open_project_page()
        old_project_list = app.project.get_project_list()
        app.project.create_project(project)
        new_project_list = app.project.get_project_list()
        assert len(old_project_list) + 1 == len(new_project_list)
        old_project_list.append(project)
        assert sorted(old_project_list, key=Project.id_or_max) == sorted(new_project_list,key=Project.id_or_max)


"""def test_add_project(app, project):
        app.session.login("administrator", "root")
        app.project.open_project_page()
        # app.project.authenticate()
        old_project = app.project.count()
        app.project.create_project(project)
        new_project = app.project.count()
        app.project.return_to_view_page()
        app.project.logout()
        #app.session.logout()
        assert old_project == new_project

        #old_project.append(project)
        # app.project.create_project(Project(name="name", status="release", description="description"))
        #assert sorted(old_project, key=Project.id_or_max) == sorted( new_project, key=Project.id_or_max)"""
