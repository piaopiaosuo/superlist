from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
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


class NewVisitorTest(unittest.TestCase):  # ➊

    def setUp(self):  # ➋
        self.browser = webdriver.Chrome()
        # self.browser.implicitly_wait(3)  # 等待三秒

    def tearDown(self):  # ➌
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):  # ➍
        # 伊迪丝听说有一个很酷的在线待办事项应用
        # 她去看了这个应用的首页
        self.browser.get('http://localhost:8003/')

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
        input_box.send_keys('Buy peacock feathers')

        # 他按回车键后,页面更新了
        # 待办事项表格中显示了"1, buy peacock feathers"
        input_box.send_keys(Keys.ENTER)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        # print([row.text for row in rows])
        # time.sleep(3)
        self.assertIn('1: Buy peacock feathers', [row.text for row in rows],
                      'this is a test'
                      )
        # self.assertTrue(
        #     any(row.text == '1: Buy peacock feathers' for row in rows),
        #     "New to-do item did not appear in table -- its text was:\n %s" % (
        #         table.text
        #     )
        # )

        # 页面中有显示了一个文本框, 可以输入其他的待办事项
        # 他输入了"use peacock feathres to make afly"
        # 伊迪斯做事很有条理
        self.fail('Finish the test!')  # ➏


if __name__ == '__main__':  # ➐
    unittest.main(warnings='ignore')  # ➑
    # unittest.main()  # ➑
