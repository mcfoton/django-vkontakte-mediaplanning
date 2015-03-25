from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_see_table_of_communities(self):

        # Llama gets all pumped up and visits the website
        self.browser.get('http://localhost:8000')

        # He looks at the title
        self.assertIn('groups', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('groups', header_text)

        # He looks at the table
        # He looks at all the buttons
        # Selects topics
        # Changes sorting in a table
        # Adds additional filters
        # Presses a button to get data
        # He looks at an updated table with user counts
        # TODO finish the workflow
        self.fail('Finish the test!')
'''
        # He is invited to enter a to-do
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # He types "Eat a mango"
        inputbox.send_keys('Eat a mango')

        # Whe he hits enter, the page updates and now the page lists
        # "1: Eat a mango" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == 'Eat Mango' for row in rows),
            "New to-do item did not appear in table"
        )

        # There's still a text box inviting to add another to-do item.
        # He enters "Meditate"
        self.fail('Finish the text!')

        # When he hits enter the page updates again,
        # and now list shows both items

        # Llama sees that his list has a unique URL

        # He tries that URL directly

        # All works and llama smiles
'''

if __name__ == '__main__':
    unittest.main(warnings='ignore')
