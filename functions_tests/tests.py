from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from django.test import LiveServerTestCase
import time


# browser = webdriver.Chrome()
# try:
#     # browser.get('http://localhost:8000/login/')
#     browser.get('http://localhost:8003')
#     print(browser.title)
#     assert 'To-Do' in browser.title, 'Browser title was: {}'.\
#         format(browser.title)
#     # 应用邀请她输入一个待办事项
#     # 购买孔雀羽毛)
#     # 她在一个文本框中输入了“ Buy peacock feathers (
#     # 伊迪丝的爱好是使用假蝇做饵钓鱼
#     # 她按回车键后,页面更新了
#     # 待办事项表格中显示了“ 1: Buy peacock feathers ”
#     # 页面中又显示了一个文本框,可以输入其他的待办事项
#     # 使用孔雀羽毛做假蝇)
#     # 她输入了“ Use peacock feathers to make a fly (
#     # 伊迪丝做事很有条理
#     # 页面再次更新,她的清单中显示了这两个待办事项
#     # 伊迪丝想知道这个网站是否会记住她的清单
#     # 她看到网站为她生成了一个唯一的URL
#     # 而且页面中有一些文字解说这个功能
#     # 她访问那个URL,发现她的待办事项列表还在
#     # 她很满意,去睡觉了
# except Exception as e:
#     print(e)
# finally:
#     import time
#     time.sleep(4)
#     browser.close()


# class NewVisitorTest(unittest.TestCase):  # ➊
class NewVisitorTest(LiveServerTestCase):  # ➊

    def setUp(self):  # ➋
        self.browser = webdriver.Chrome()
        # self.browser.implicitly_wait(3)  # 等待三秒

    def tearDown(self):  # ➌
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):  # ➍
        # 伊迪丝听说有一个很酷的在线待办事项应用
        # 她去看了这个应用的首页
        # self.browser.get('http://localhost:8003/')
        self.browser.get(self.live_server_url)

        # 她注意到网页的标题和头部都包含“ To-Do ”这个词
        print(self.browser.title)
        time.sleep(3)
        self.assertIn('To-Do', self.browser.title)  # ➎
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # 应用邀请他输入一个待办事项
        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            input_box.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # 她在一个文本框中输入了"buy peacock feathers"
        # 伊迪斯的爱好是使用是使用家蝇做鱼饵钓鱼
        # 她按回车键, 被带到了一个新的url
        #
        input_box.send_keys('Buy peacock feathers')
        input_box.send_keys(Keys.ENTER)
        edith_list_url = self.browser.current_url

        self.assertRegex(edith_list_url, '/lists/.+')
        # 页面中又显示了一个文本框,可以输入其他的待办事项
        # ” 使用孔雀羽毛做假蝇)
        # 她输入了“ Use peacock feathers to make a fly (
        # 伊迪丝做事很有条理
        # input_box = self.browser.find_element_by_id('id_new_item')
        # input_box.send_keys('Use peacock feathers to make a fly')
        #
        # # 他按回车键后,页面更新了
        # # 待办事项表格中显示了"1, buy peacock feathers"
        # input_box.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table(
            '2: Use peacock feathers to make a fly')

        # 现在一个叫作弗朗西斯的新用户访问了网站
        # 我们使用一个新浏览器会话
        # 确保伊迪丝的信息不会从cookie中泄露出来
        self.browser.quit()
        self.browser = webdriver.Chrome()

        # 弗朗西斯访问首页
        # 页面中看不到伊迪斯的清单
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        print('page_text', page_text)
        self.assertNotIn('Buy peacock feathers', page_text)
        input_box = self.browser.find_element_by_id('id_new_item')
        input_box.send_keys('Buy milk')
        input_box.send_keys(Keys.ENTER)

        # 弗朗西斯获得了他唯一的url
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        # 这个页面没有伊迪斯的清单
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)

        # 两人都很满意, 去睡觉了

        # 页面中有显示了一个文本框, 可以输入其他的待办事项
        # 他输入了"use peacock feathres to make afly"
        # 伊迪斯做事很有条理
        self.fail('Finish the test!')  # ➏


# if __name__ == '__main__':  # ➐
#     unittest.main(warnings='ignore')  # ➑
#     # unittest.main()  # ➑
