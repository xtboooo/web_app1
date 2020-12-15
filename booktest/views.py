from django.http import JsonResponse
from django.views import View

from booktest.models import BookInfo, HeroInfo


class HeroListView(View):
    """ 获取全部英雄 修改指定英雄数据 视图 """

    def get(self, request):
        """ 获取所有的英雄人物数据 """
        heros = HeroInfo.objects.all()
        hero_list = []

        try:
            for hero in heros:
                data = {
                    'id': hero.id,
                    'hname': hero.hname,
                    'hgender': hero.hgender,
                    'hcomment': hero.hcomment,
                    'hbook': hero.hbook.btitle,
                    'hbook_id': hero.hbook_id
                }
                hero_list.append(data)
        except Exception as e:
            # print(e)
            return JsonResponse({'code': 400,
                                 'message': '获取数据错误'})

        return JsonResponse({'code': 0,
                             'message': 'OK',
                             'heros': hero_list})

    def post(self, request):
        """ 新增一个英雄人物数据 """
        pass


class HeroDetailView(View):
    """ 获取 修改 删除 指定的英雄人物数据"""

    def get(self, request):
        """ 获取指定的英雄人物数据(根据英雄ID) """
        pass

    def put(self, request):
        """ 修改指定的英雄人物数据(根据英雄ID) """
        pass

    def delete(self, request):
        """ 删除指定的英雄人物数据(根据英雄ID) """
        pass
