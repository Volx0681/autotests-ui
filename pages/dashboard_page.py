from playwright.sync_api import Page
from pages.base_page import BasePage
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from components.dashboard.dashboard_toolbar_view_component import DashboardToolbarViewComponent
from components.charts.chart_view_component import ChartViewComponent

class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)
        self.toolbar = DashboardToolbarViewComponent(page)
        self.students_chart_view = ChartViewComponent(page, 'students', 'bar')
        self.activities_chart_view = ChartViewComponent(page, 'activities', 'line')
        self.courses_chart_view = ChartViewComponent(page, 'courses', 'pie')
        self.scores_chart_view = ChartViewComponent(page, 'scores', 'scatter')

    def check_visible_dashboard_title(self):
        self.toolbar.check_visible()

    def check_visible_students_chart(self):
        self.students_chart_view.check_visible('Students')

    def check_visible_activities_chart(self):
        self.activities_chart_view.check_visible('Activities')

    def check_visible_courses_chart(self):
        self.courses_chart_view.check_visible('Courses')

    def check_visible_scores_chart(self):
        self.scores_chart_view.check_visible('Scores')