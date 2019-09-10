from article import Article

class TestArticle():
    def test_init_of_Article(self):
        article = Article()
        assert article.placeholder_method() == 'hello word'