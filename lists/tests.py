from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.views import home_page


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        print('1123', found)
        self.assertEqual(found.func, home_page)  # 检查是否使用了正确的函数

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        # print(request.body)
        response = home_page(request)
        print(456, response.content)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>To-Do lists</title>', response.content)
        self.assertTrue(response.content.strip().endswith(
            b'</html>'))

    def test_home_page_returns_correct_string(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertTrue(response.content, expected_html)  # 检查是否渲染了正确的模板
