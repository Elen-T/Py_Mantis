from random import randrange
import pytest
from model.project import Project

def test_del_project(app):
    app.session.login("administrator", "root")
    # app.project.authenticate()
    app.project.open_project_page()
    old_project_list = app.project.get_project_list()
    index = randrange(len(old_project_list))
    app.project.del_project_by_index(index)
    new_project_list = app.project.get_project_list()
    assert len(old_project_list) - 1 == len(new_project_list)
    del old_project_list[index]
    assert sorted(old_project_list, key=Project.id_or_max) == sorted(new_project_list, key=Project.id_or_max)
    # app.session.logout()


"""def test_del_project(app):
        app.session.login("administrator", "root")
        #app.project.authenticate()
        app.project.open_project_page()
        old_project = app.project.count()
        index = randrange(1, old_project)
        app.project.del_project_by_index(index)
        new_project = app.project.count()
        app.project.return_to_view_page()
        assert old_project == new_project
        app.project.logout()
        #app.session.logout()"""


