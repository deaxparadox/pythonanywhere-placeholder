import json


from django.core import serializers
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse, Http404

from .models import UserInfo


# def index(request):
#     qs = UserInfo.objects.all()
#     qs_json = serializers.serialize('json', qs)
#     return HttpResponse(qs_json, content_type='application/json')

def index(request):
    qs = UserInfo.objects.all()
    return render(request, "placeholder/index.html", {
        "userinfo": qs,
    })

def get_user(request, id):
    qs = get_object_or_404(UserInfo, id=id)
    return JsonResponse(
        qs.to_dict(), status=200
    )

