from model.project import Project
from selenium.webdriver.support.select import Select


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_project_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def authenticate(self):
        wd = self.app.wd
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys("root")
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Password'])[1]/following::input[2]").click()


    def create_project(self, project):
        wd = self.app.wd
        wd.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Manage Configuration'])[1]/following::input[2]").click()
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(project.name)
        wd.find_element_by_name("status").click()
        Select(wd.find_element_by_name("status")).select_by_visible_text("release")
        wd.find_element_by_name("status").click()
        wd.find_element_by_name("description").click()
        wd.find_element_by_name("description").clear()
        wd.find_element_by_name("description").send_keys(project.description)
        wd.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Description'])[1]/following::input[1]").click()
        wd.implicitly_wait(10)


    def return_to_view_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='administrator'])[1]/preceding::img[1]").click()


    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()

    def count(self):
        wd = self.app.wd
        #return len(wd.find_elements_by_xpath("//body//tr[]"))
        return len(wd.find_elements_by_xpath("//div[@class='widget-box widget-color-blue2']/div[2]/div[1]/div[2]/table/tbody/tr"))

    def delete(self):
        wd = self.app.wd

    def open_project_by_index(self, index):
        wd = self.app.wd
        self. open_project_page()
        row = wd.find_elements_by_xpath("//div[@class='table-responsive']/table/tbody/tr")[index]
        cell = row.find_elements_by_tag_name("td")[0]
        cell.find_element_by_tag_name("a").click()

    def del_project_by_index(self, index):
        wd = self.app.wd
        self.open_project_page()
        wd.find_elements_by_css_selector("td > a[href*='manage_proj_edit_page.php?project_id']")[index].click()
        wd.find_element_by_css_selector("input[value='Delete Project']").click()
        wd.find_element_by_css_selector("input[value='Delete Project']").click()

    """def get_project_list(self):
        wd = self.app.wd
        self.open_project_page()
        self.project_list = []
        for element in wd.find_elements_by_xpath("//div[@class='table-responsive']/table/tr"):
            cells = element.find_elements_by_tag_name("td")
            name = cells[1]
            description = cells[5]
            self.project_list.append(Project(name=name, description=description))
        return list(self.project_list)"""

    def get_project_list(self):
        wd = self.app.wd
        self.open_project_page()
        project_list = []
        for el in wd.find_elements_by_css_selector("td > a[href*='manage_proj_edit_page.php?project_id']"):
            id = el.get_attribute('search')[12:]
            name = el.text
            project_list.append(Project(name=name, id=id))
        return project_list