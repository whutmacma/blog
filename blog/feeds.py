from django.contrib.syndication.views import Feed

from .models import Article


class AllArticlesRssFeed(Feed):
    # 显示在聚合阅读器上的标题
    title = "Blog & Mac"

    # 通过聚合阅读器跳转到网站的地址
    link = "http://127.0.0.1:8020/welcome/"

    # 显示在聚合阅读器上的描述信息
    description = "Django 博客教程演示项目测试文章"

    # 需要显示的内容条目
    def items(self):
        return Article.objects.all()

    # 聚合器中显示的内容条目的标题
    def item_title(self, item):
        return '[%s] %s' % (item.category, item.title)

    # 聚合器中显示的内容条目的描述
    def item_description(self, item):
        return item.body
