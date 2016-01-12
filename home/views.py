from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_GET

from home.models import Member


@require_GET
def index(request):
    return render(request, 'home/index.html')


@require_GET
def member(request):
    return render(request, 'home/member.html')


@require_GET
def group(request):
    return render(request, 'home/group.html')


@require_GET
def get_members(request):
    ret_list = []
    for member in Member.objects.all():
        ret_list.append(member.as_json())
    # print ret_list
    return JsonResponse(ret_list, safe=False)




