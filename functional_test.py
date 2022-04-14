import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):
    
    def setUp(self) -> None:
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith聽說有個很酷的代辦事項清單網頁
        # 她去查看首頁
        self.browser.get('http://localhost:8000')

        # 她發現網頁標頭(title)與標題(h1)顯示"代辦事項清單"
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # 她馬上受邀輸入一個代辦事項
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # 她在文字方塊輸入"購買孔雀羽毛"
        # (Edith的興趣是綁蒼蠅魚餌)
        inputbox.send_keys('Buy peacock feathers')

        # 當她按下enter，網頁會更新，現在網頁列出
        # "1.購買孔雀羽毛"，一個待辦事項
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )

        # 此時仍然有一個文字方塊，讓她可以加入其他項目
        # 她輸入"使用孔雀羽毛製作一隻蒼蠅"(Edith非常有條理)
        self.fail('Finish the test!')

        # 網頁再次更新，現在她的清單有兩個項目

        # Edith 不知道網站能否記得她的清單
        # 接著她看到網站產生一個唯一的URL給她
        # 網頁有一些文字說明其用途

        # 她前往那個URL－她的待辦清單仍在那裏

        # 她滿意地上床睡覺


if __name__ == '__main__':
    unittest.main(warnings='ignore')