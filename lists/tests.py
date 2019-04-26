from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.views import home_page
from lists.models import Item


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

    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = "POST"
        request.POST['item_text'] = 'A new list item'

        response = home_page(request)

        self.assertEqual(Item.objects.count(), 1)

        self.assertIn('A new list item', response.content.decode())
        expected_html = render_to_string(
            'home.html', {"new_item_text": 'A new list item'}
        )
        self.assertEqual(response.content.decode(), expected_html)


class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'the first list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'the second list item'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        import time
        time.sleep(3)
        self.assertEqual(first_saved_item.text, 'the first list item')
        self.assertEqual(second_saved_item.text, 'the second list item')
