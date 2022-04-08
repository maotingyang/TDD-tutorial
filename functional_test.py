import unittest

from selenium import webdriver


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

        # 她發現網頁標頭(title)顯示"代辦事項清單"
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # 她馬上受邀輸入一個代辦事項

        # 她在文字方塊輸入"購買孔雀羽毛"
        # (Edith的興趣是綁蒼蠅魚餌)

        # 當她按下enter，網頁會更新，現在網頁列出
        # "1.購買孔雀羽毛"，一個待辦事項

        # 此時仍然有一個文字方塊，讓她可以加入其他項目
        # 她輸入"使用孔雀羽毛製作一隻蒼蠅"(Edith非常有條理)

        # 網頁再次更新，現在她的清單有兩個項目

        # Edith 不知道網站能否記得她的清單
        # 接著她看到網站產生一個唯一的URL給她
        # 網頁有一些文字說明其用途

        # 她前往那個URL－她的待辦清單仍在那裏

        # 她滿意地上床睡覺


if __name__ == '__main__':
    unittest.main(warnings='ignore')