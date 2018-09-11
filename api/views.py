from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status

from .models import *
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class AnimalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Animal
        fields = ('name', 'age')

class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

router = routers.DefaultRouter()
router.register(r'animals', AnimalViewSet)

@csrf_exempt
def run_job(request):
    # 判断请求头是否为json
    if request.content_type != 'application/json':  
        # 如果不是的话，返回405
        return HttpResponse('only support json data', status=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)
    # 判断是否为post 请求
    if request.method == 'POST':
        try:
            # 解析请求的json格式入参
            data = JSONParser().parse(request)
        except Exception as why:
            print(why.args)
        else:
            content = {'msg': 'SUCCESS'}
            print(data)
            # 返回自定义请求内容content,200状态码
            return JsonResponse(data=content, status=status.HTTP_200_OK)
    # 如果不是post 请求返回不支持的请求方法
    return HttpResponseNotAllowed(permitted_methods=['POST'])



# @csrf_exempt
# def get_animals(request):
#     animals = Animal.objects.all()
#     data = serializers.serialize("json", animals)
#     return HttpResponse(data)


#todo 直接使用sql https://www.cnblogs.com/lijintian/p/6100097.html