from unittest import TestCase
from typing import List
from google.easy.crawler_log_folder_1598 import CrawlerLogFolder

class TestCrawlerLogFolder(TestCase):

    def setUp(self) -> None:
        self.c = CrawlerLogFolder()
    
    def test_crawler(self):
        logs: List[str] = ["d1/","d2/","../","d21/","./"]
        res = self.c.minOperations(logs=logs)
        self.assertEqual(res, 2)