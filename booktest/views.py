import json

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
        req_dict = json.loads(request.body)
        hname = req_dict.get('hname')
        hgender = req_dict.get('hgender')
        hcomment = req_dict.get('hcomment')
        hbook_id = req_dict.get('hbook_id')
        # 参数完整性
        if not all([hname, hcomment, hbook_id]):
            return JsonResponse({'code': 400,
                                 'message': '缺少必传参数!'})
        if hgender is None:
            return JsonResponse({'code': 400,
                                 'message': '缺少必传参数!'})

        try:
            book = BookInfo.objects.get(id=hbook_id)
        except BookInfo.DoesNotExist:
            return JsonResponse({'code': 400,
                                 'message': '图书数据不存在'})
        try:
            hero = HeroInfo.objects.create(hname=hname,
                                           hgender=hgender,
                                           hcomment=hcomment,
                                           hbook_id=hbook_id, )
        except Exception as e:
            print(e)
            return JsonResponse({'code': 400,
                                 'message': '添加数据出错!'})
        data = {
            'id': hero.id,
            'hname': hero.hname,
            'hgender': hero.hgender,
            'hcomment': hero.hcomment,
            'hbook': hero.hbook.btitle,
            'hbook_id': hero.hbook_id,
        }
        return JsonResponse({'code': 0,
                             'message': 'OK',
                             'hero': data})


class HeroDetailView(View):
    """ 获取 修改 删除 指定的英雄人物数据"""

    def get(self, request, id):
        """ 获取指定的英雄人物数据(根据英雄ID) """
        try:
            hero = HeroInfo.objects.get(id=id)
        except HeroInfo.DoesNotExist:
            return JsonResponse({'code': 400,
                                 'message': '请求英雄数据不存在'})
        data = {
            'id': hero.id,
            'hname': hero.hname,
            'hgender': hero.hgender,
            'hcomment': hero.hcomment,
            'hbook': hero.hbook.btitle,
            'hbook_id': hero.hbook_id,
        }
        return JsonResponse({'code': 0,
                             'message': 'OK',
                             'hero': data})

    def put(self, request, id):
        """ 修改指定的英雄人物数据(根据英雄ID) """
        try:
            hero = HeroInfo.objects.get(id=id)
        except HeroInfo.DoesNotExist:
            return JsonResponse({'code': 400,
                                 'message': '请求英雄数据不存在!'})
        req_dict = json.loads(request.body)
        hname = req_dict.get('hname')
        hgender = req_dict.get('hgender')
        hcomment = req_dict.get('hcomment')
        hbook_id = req_dict.get('hbook_id')

        if not all([hname, hcomment, hbook_id]):
            return JsonResponse({'code': 400,
                                 'message': '缺少必传参数!'})
        if hgender is None:
            return JsonResponse({'code': 40,
                                 'message': '缺少必传参数!'})
        try:
            book = BookInfo.objects.get(id=hbook_id)
        except BookInfo.DoesNotExist:
            return JsonResponse({'code': 400,
                                 'message': '图书数据不存在!'})
        try:
            hero.hname = hname
            hero.hgender = hgender
            hero.hcomment = hcomment
            hero.hbook_id = hbook_id
            hero.save()
        except Exception as e:
            print(e)
            return JsonResponse({'code': 400,
                                 'message': '更新数据出错!'})
        data = {
            'id': hero.id,
            'hname': hero.hname,
            'hgender': hero.hgender,
            'hcomment': hero.hcomment,
            'hbook': hero.hbook.btitle,
            'hbook_id': hero.hbook_id,
        }
        return JsonResponse({'code': 0,
                             'message': 'OK',
                             'hero': data})

    def delete(self, request, id):
        """ 删除指定的英雄人物数据(根据英雄ID) """
        try:
            hero = HeroInfo.objects.get(id=id)
        except HeroInfo.DoesNotExist:
            return JsonResponse({'code': 400,
                                 'message': '英雄数据不存在!'})
        try:
            hero.delete()
        except Exception as e:
            print(e)
            return JsonResponse({'code': 400,
                                 'message': '删除数据出错!'})

        return JsonResponse({"code": 0,
                             'message': 'OK'})
