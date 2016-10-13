# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from django.template.context import RequestContext

# 表单
@csrf_exempt
def login_form(request):
	return render_to_response('login.html')

# 接收请求的登录数据
@csrf_exempt
def login(request):
	request.encoding='utf-8'
        username = request.POST['username'].encode("utf-8")
        password = request.POST['password'].encode("utf-8")
        c = {'username': username, 'password': password}
	return render_to_response( "index.html", c)