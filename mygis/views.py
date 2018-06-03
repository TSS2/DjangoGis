#! -*- coding:utf8 -*- 
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger  # 分页模块
import json
import django.utils.timezone as timezone
from users.models import User
from .models import *
import datetime
import time

# Create your views here.
@login_required
def gis(request):
    if str(request.user) == 'admin':
        logo = '管理员'
        content = '首页'
        return render(request,'mygis/gis.html',context={'logo':logo,'content':content})
    else:
        logo = '信息采集员'
        content = '首页'
        return render(request,'mygis/index.html',context={'logo':logo,'content':content})

@login_required
def message_manage(request):
    if str(request.user) == 'admin':
        logo = '管理员'
    else:
        logo  = '信息采集员'   
    if request.method == 'POST':
        content = request.POST["context"]
        return HttpResponse(json.dumps({'logo':logo,'context':content}))
    elif request.method == 'GET':
        content = "指标查看"
    else:
        content = '首页'

    return render(request,'mygis/message.html',context={'logo':logo,'content':content})

@login_required
def people_manage(request):
    if str(request.user) == 'admin':
        logo = '管理员'
    else:
        logo  = '信息采集员'   
    if request.method == 'POST':
        content = request.POST["context"]
        return HttpResponse(json.dumps({'logo':logo,'context':content}))
    elif request.method == 'GET':
        content = "用户管理"
    else:
        content = '首页'

    return render(request,'mygis/message.html',{'logo':logo,'content':content})

@login_required
def community(request):
 
    if str(request.user) == 'admin':
        logo = '管理员'
    else:
        logo  = '信息采集员'   
    print(request.method)
    if request.method == 'POST':
        content = request.POST["context"]
        print(content)
        return HttpResponse(json.dumps({'logo':logo,'context':content}))
    elif request.method == 'GET':
        content = "社区"
    else:
        content = '首页'
    return render(request,'mygis/community.html',{'logo':logo,'content':content})

# 更新菜市场信息
@login_required
def updateMessage(request):
    if str(request.user) == 'admin':
        logo = '管理员'
    else:
        logo  = '信息采集员'  
    if request.method == 'POST':
        content = request.POST["context"]
        return HttpResponse(json.dumps({'logo':logo,'context':content}))
    elif request.method == 'GET':
        content = "更新菜市场"
    else:
        content = '首页'
    return render(request,'mygis/updatemessage.html',{'logo':logo,'content':content})

# 更新小区信息
@login_required
def updateCommunity(request):
    if str(request.user) == 'admin':
        logo = '管理员'
    else:
        logo  = '信息采集员'  
    if request.method == 'POST':
        content = request.POST["context"]
        return HttpResponse(json.dumps({'logo':logo,'context':content}))
    elif request.method == 'GET':
        content = "小区更新"
    else:
        content = '首页'
    return render(request,'mygis/updatecommunity.html',{'logo':logo,'content':content})

# 更新餐馆信息
@login_required
def updateRest(request):
    if str(request.user) == 'admin':
        logo = '管理员'
    else:
        logo  = '信息采集员'  
    if request.method == 'POST':
        content = request.POST["context"]
        return HttpResponse(json.dumps({'logo':logo,'context':content}))
    elif request.method == 'GET':
        content = "餐馆更新"
    else:
        content = '首页'
    return render(request,'mygis/updaterest.html',{'logo':logo,'content':content})

# 审核信息
@login_required
def verifyMessage(request):
    if str(request.user) == 'admin':
        logo = '管理员'
    else:
        logo  = '信息采集员'  
    if request.method == 'POST':
        content = request.POST["context"]
        return HttpResponse(json.dumps({'logo':logo,'context':content}))
    elif request.method == 'GET':
        content = "信息审核"
    else:
        content = '首页'
    return render(request,'mygis/verifymessage.html',{'logo':logo,'content':content})

# 接受客户端菜市场数据 添加到数据库
@login_required
@csrf_exempt
def addmessage(request):
    if str(request.user) == 'admin':
        logo = '管理员'
    else:
        logo  = '信息采集员'  

    if request.method == 'POST':
        market_name = request.POST.get('market_name',False)
        province = request.POST.get('province',False)
        city = request.POST.get('city',False)
        district = request.POST.get('district',False)
        eX = request.POST.get('eX',False)
        eY = request.POST.get('eY',False)
        market_phone = request.POST.get('market_phone',False)
        
        address = '_'.join([str(province),str(city),str(district)])
        if eX:
            create_misite_market(market_name,address,eX,eY,market_phone)
        return HttpResponseRedirect('/mygis/updatemessage')
    return render(request,'mygis/updatemessage.html')

# 添加小区
@login_required
@csrf_exempt
def addcommunity(request):
    if str(request.user) == 'admin':
        logo = '管理员'
    else:
        logo  = '信息采集员'  
    if request.method == 'POST':
        community_name = request.POST.get('community_name',False)
        province = request.POST.get('province',False)
        city = request.POST.get('city',False)
        district = request.POST.get('district',False)
        eX = request.POST.get('eX',False)
        eY = request.POST.get('eY',False)
        community_phone = request.POST.get('community_phone',False)
        address = '_'.join([str(province),str(city),str(district)])
        print(address)
        if eX:
            create_misite_community(community_name,address,eX,eY,community_phone)
        return HttpResponseRedirect('/mygis/updatecommunity')
    return render(request,'mygis/updatecommunity.html')

# 添加餐馆
@login_required
@csrf_exempt
def addrest(request):
    if str(request.user) == 'admin':
        logo = '管理员'
    else:
        logo  = '信息采集员'  
    if request.method == 'POST':
        rest_name = request.POST.get('rest_name',False)
        province = request.POST.get('province',False)
        city = request.POST.get('city',False)
        district = request.POST.get('district',False)
        eX = request.POST.get('eX',False)
        eY = request.POST.get('eY',False)
        rest_phone = request.POST.get('rest_phone',False)
        address = '_'.join([str(province),str(city),str(district)])
        print(address)
        if eX:
            create_misite_restaurant(rest_name,address,eX,eY,rest_phone)
        return HttpResponseRedirect('/mygis/updaterest')
    return render(request,'mygis/updaterest.html')

@login_required
@csrf_exempt
def querymessage(request):
    if request.method == 'POST':
        district = request.POST.get('district',False)
        province = request.POST.get('province',False)
        city = request.POST.get('city',False)
        address = '_'.join([str(province),str(city),str(district)])
        query = query_misite_market(address,None)
        print(query)
        response_data = {}
        for q in query:
            response_data[q['market_name']] = [q['market_long'],q['market_dimen']]  
        print(response_data)
    return HttpResponse(json.dumps(response_data),content_type="application/json")

# 弹出层 显示菜市场信息
@login_required
@csrf_exempt
def marketmessage(request):
    name = request.GET.get('name',None)
    if request.method == 'POST':
        pass
    # 菜市场问卷调查 
    query_target = query_misite_targetlast(None,name)
    date_time = None
    for query in query_target:
        lrzw = query['lrzw']
        lrzw_s = lrzw.split('_')
        lrzw_fen = lrzw_s[0]
        lrzw_t =lrzw_s[1]
        twzj = query['twzj']
        twzj_s = twzj.split('_')
        twzj_fen = twzj_s[0]
        twzj_t =twzj_s[1]
        cyryywzj = query['cyryywzj']
        cyryywzj_s = cyryywzj.split('_')
        cyryywzj_fen = cyryywzj_s[0]
        cyryywzj_t =cyryywzj_s[1]
        csws = query['csws']
        csws_s = csws.split('_')
        csws_fen = csws_s[0]
        csws_t =csws_s[1]
        cpxxcd = query['cpxxcd']
        cpxxcd_s = cpxxcd.split('_')
        cpxxcd_fen = cpxxcd_s[0]
        cpxxcd_t =cpxxcd_s[1]
        pingfen = query['pingfen']
        
        times = query['data_time']
        
        year = times.year
        month = times.month
        day = times.day
        date_time = str(year)+'-'+str(month)+'-'+str(day)
    # print(date_time)
    if request.method == 'GET':
        return render(request,'mygis/querymessage.html',locals())
    return render(request,'mygis/querymessage.html',locals())

# 信息采集员 显示菜市场信息
@login_required
@csrf_exempt
def marketmessage_user(request):
    if str(request.user) == 'admin':
        
        logo = '管理员'
    else:
        logo = '信息采集员'
    content = '菜市场'
    query = query_misite_market()
    paginator = Paginator(query,3) # 每页三条数据
    page = request.GET.get('page',1)  # 接受网页中的page值
    try:
        customer = paginator.page(page)
    except PageNotAnInteger:
        customer = paginator.page(1)
    except EmptyPage:
        customer = paginator.page(paginator.num_pages)
    cus_list = customer.object_list
    return render(request,'mygis/marketmessage_user.html',locals())

# 信息采集员 显示小区信息
@login_required
@csrf_exempt
def querycommunitymessage(request):
    if str(request.user) == 'admin':
        logo = '管理员'
        if request.method == 'POST':
            id = request.POST.get('task_id')
            task_id = str(id).split('_')[1]
            update_mysite_people(task_id)
    else:
        logo  = '信息采集员'
        
    content = '小区'
    query = query_misite_community()
    community_id = []
    for q in query:
        community_id.append(q['community_id'])    # 小区ID
    # 根据小区ID查询小区人口数
    people_message = []
    for id in community_id:
        query_people = query_misite_people(id,None)
        query_community = query_misite_community(None,None,id)
        item = {}
        for query_p in query_people:
            item['people_num'] = query_p['num_people']
            item['check'] = query_p['check']
            item['task_id'] = query_p['task_id']
        for query_c in query_community:
            item['community'] = query_c['community_name']
            item['address'] = query_c['community_address']
            item['c_id'] = query_c['community_id']
            people_message.append(item)
    paginator = Paginator(people_message,3) # 每页三条数据
    page = request.GET.get('page',1)  # 接受网页中的page值
    try:
        customer = paginator.page(page)
    except PageNotAnInteger:
        customer = paginator.page(1)
    except EmptyPage:
        customer = paginator.page(paginator.num_pages)
    cus_list = customer.object_list
    return render(request,'mygis/communitymessage.html',locals())

# 进入价格采集页面
@login_required
@csrf_exempt
def marketdetail(request):
    if str(request.user) == 'admin':
        logo = '管理员'
    else:
        logo = '信息采集员'
    content = '菜市场'
    market_name = request.GET.get('market_name',None)
    print(market_name)
    update_mysite_market(None,market_name)
    page = request.GET.get('page',1)
    foodadd = '菜品管理'
    people_tanwei = '流量与摊位'
    message = '问卷调查'
    market_id = 0
    # 菜市场信息
    query = query_misite_market(None,market_name)
    for q in query:
        market_id = q['market_id']
    if str(request.user) == 'admin':
        if request.method == 'POST':
            id = request.POST.get('task_id')
            task_id = str(id).split('_')[1]
            update_mysite_price(task_id)
    # 价格采集任务表
    query_price = query_misite_price(market_id,market_name)
    messages = []
    if query_price:
        for q in query_price:
            food = q['food_id_id']
            price = q['price']
            datatime = q['data_time']
            market_id_id = q['market_id_id']
            check = q['check']
            task_id = q['task_id']
            # 菜品信息
            query_food = query_misite_food('',food)
            for q in query_food:
                item = {}
                item['mfood'] = q['food_name']
                item['mprice'] = price
                item['mdatatime'] = datatime
                item['check'] = check
                item['task_id'] = task_id
                messages.append(item)
    paginator = Paginator(messages,5) # 每页三条数据
    page = request.GET.get('page',1)  # 接受网页中的page值
    try:
        customer = paginator.page(page)
    except PageNotAnInteger:
        customer = paginator.page(1)
    except EmptyPage:
        customer = paginator.page(paginator.num_pages)
    cus_list = customer.object_list
    return render(request,'mygis/marketdetails.html',locals())

# 进入流量与摊位采集页面
@login_required
@csrf_exempt
def marketmessages(request):
    logo = '信息采集员'
    content = '菜市场'
    market_name = request.GET.get('market_name')
    page = request.GET.get('page',1)
    foodadd = '菜品管理'
    people_tanwei = '流量与摊位'
    message = '问卷调查'
    # 菜市场信息
    query = query_misite_market(None,market_name)
    for q in query:
        market_id = q['market_id']
    if str(request.user) == 'admin':
        if request.method == 'POST':
            id = request.POST.get('task_id')
            task_id = str(id).split('_')[1]
            update_mysite_message(task_id)
    # 流量摊位采集任务表
    query_message = query_misite_message(market_id,market_name)
    messages = []
    if query_message:
        for q in query_message:
            message_id = q['message_id']
            people_flow = q['people_flow']
            datatime = q['data_time']
            market_id = q['market_id']
            tanwei_num = q['tanwei_num']
            tanwei_use_num = q['tanwei_use_num']
            check = q['check']
            item = {}
            item['message_id'] = message_id
            item['datatime'] = datatime
            item['people_flow'] = people_flow
            item['tanwei_num'] = tanwei_num
            item['tanwei_use_num'] = tanwei_use_num
            item['check'] = check
            messages.append(item)
    paginator = Paginator(messages,3) # 每页三条数据
    page = request.GET.get('page',1)  # 接受网页中的page值
    try:
        customer = paginator.page(page)
    except PageNotAnInteger:
        customer = paginator.page(1)
    except EmptyPage:
        customer = paginator.page(paginator.num_pages)
    cus_list = customer.object_list
    return render(request,'mygis/people_tanwei.html',locals())

# 进入评价采集页面
@login_required
@csrf_exempt
def marketdetailasses(request):
    content = '菜市场'
    market_name = request.GET.get('market_name')
    people_tanwei = '流量与摊位'
    page = request.GET.get('page',1)
    foodadd = '菜品管理'
    message = '问卷调查'
    if str(request.user) == 'admin':
        logo = '管理员'
        print(request.method)
        print(market_name)
        query_target = query_misite_target(None,market_name)
        message_t = []
        for query_t in query_target:
            target_id = query_t['target_id']
            lrzw = query_t['lrzw']
            twzj = query_t['twzj']
            cyryywzj = query_t['cyryywzj']
            csws = query_t['csws']
            cpxxcd = query_t['cpxxcd']
            pingfen = query_t['pingfen']
            data_time = query_t['data_time']
            check = query_t['check']
            item = {}
            item['target_id'] = target_id
            item['lrzw'] = lrzw
            item['twzj'] = twzj
            item['cyryywzj'] = cyryywzj
            item['csws'] = csws
            item['cpxxcd'] = cpxxcd
            item['pingfen'] = pingfen
            item['data_time'] = data_time
            item['check'] = check
            message_t.append(item)
        paginator = Paginator(message_t,3) # 每页三条数据
        page = request.GET.get('page',1)
        pages = request.GET.get('pages',1)  # 接受网页中的page值
        print(page)
        try:
            customer = paginator.page(pages)
        except PageNotAnInteger:
            customer = paginator.page(1)
        except EmptyPage:
            customer = paginator.page(paginator.num_pages)
        cus_list = customer.object_list
        if request.method == 'POST':
            id = request.POST.get('task_id')
            task_id = str(id).split('_')[1]
            update_mysite_target(task_id)
        return render(request,'mygis/markettarget.html',locals())
    else:
        logo  = '信息采集员'
    query = query_misite_market(None,market_name)
    for q in query:
        market_id = q['market_id']
        market_address = q['market_address']
        market_phone = q['market_phone']
        data_time = q['data_time']
        status = q['status']
        if status == '0':
            update_mysite_market(None,market_name)
    # 添加问卷信息
    if request.method == 'POST':
        market = request.POST.get('market_id')
        lrzw = request.POST.get('start2')
        twzj = request.POST.get('start3')
        cyryywzj = request.POST.get('start4')
        csws = request.POST.get('start5')
        cpxxcd = request.POST.get('start1')
        user = User.objects.filter(username=request.user).values()
        for query in user:
            u_id = query['id']
        lrzws = str(lrzw).split('_')[0]
        twzjs = str(twzj).split('_')[0]
        cyryywzjs = str(cyryywzj).split('_')[0]
        cswss = str(csws).split('_')[0]
        cpxxcds = str(cpxxcd).split('_')[0]
        pingfen = int(lrzws) + int(twzjs) + int(cyryywzjs) + int(cswss) + int(cpxxcds)
        # 添加评分
        print(market,u_id,lrzw,twzj,cyryywzj,csws,cpxxcd,pingfen)
        create_misite_target(market,u_id,lrzw,twzj,cyryywzj,csws,cpxxcd,str(pingfen))
    return render(request,'mygis/marketdetailasses.html',locals())

# # 进入小区信息采集页面
# @login_required
# @csrf_exempt
# def addcommunitymessage(request):
#     logo = '信息采集员'
#     content = '小区'
#     community_name = request.GET.get('community_name')
#     page = request.GET.get('page',1)
#     peopleadd = '人口管理'
#     # 小区信息
#     query = query_misite_community(community_name)
#     for q in query:
#         community_id = q['community_id']
#     # 人口采集任务表
#     query_people = query_misite_price(community_id,community_name)
#     messages = []
#     if query_people:
#         for q in query_people:
#             people_id = q['task_id']
#             peopel_num = q['num_people']
#             datatime = q['data_time']
#             community_id_id = q['community_id_id']
#             message_person_id_id = q['message_person_id_id']
#             item = {}
#             item['mpeople_num'] = q['peopel_num']
#             item['mdatatime'] = datatime
#             messages.append(item)
#     paginator = Paginator(messages,3) # 每页三条数据
#     page = request.GET.get('page',1)  # 接受网页中的page值
#     try:
#         customer = paginator.page(page)
#     except PageNotAnInteger:
#         customer = paginator.page(1)
#     except EmptyPage:
#         customer = paginator.page(paginator.num_pages)
#     cus_list = customer.object_list
#     return render(request,'mygis/marketdetails.html',locals())

# 信息采集员菜市场价格编辑
@login_required
@csrf_exempt
def marketdetailedit(request):
    logo = '信息采集员'
    content = '菜市场'
    market_name = request.GET.get('market_name')
    page = request.GET.get('page',1)
    foodadd = '菜品管理'
    message = '问卷调查'
    query = query_misite_market(market_name)
    for q in query:
        market_id = q['market_id']
        market_address = q['market_address']
        market_phone = q['market_phone']
        data_time = q['data_time']
        status = q['status']
        if status == '0':
            update_mysite_market(None,market_name)
    return render(request,'mygis/marketdetails.html',locals())
# 未使用
# 信息采集员发布菜品  
@login_required
@csrf_exempt
def marketfoodedit(request):
    logo = '管理员'
    content = '菜品发布'
    query = query_misite_market()
    paginator = Paginator(query,3) # 每页三条数据
    page = request.GET.get('page',1)  # 接受网页中的page值
    try:
        customer = paginator.page(page)
    except PageNotAnInteger:
        customer = paginator.page(1)
    except EmptyPage:
        customer = paginator.page(paginator.num_pages)
    cus_list = customer.object_list
    return render(request,'mygis/marketfoodedit.html',locals())

# 信息采集员添加菜品
@login_required
@csrf_exempt
def marketfoodadd(request):
    id = request.GET.get('id')
    ma_id = str(id).split('_')
    market_id = ma_id[1]
    query_user = User.objects.filter(username=request.user).values()
    if request.method == 'POST':
        food = request.POST.get('food',None)
        price = request.POST.get('price',0.0)
        # 添加菜品
        create_misite_food(food)
        query_food = query_misite_food(food,None)
        for query in query_food:
            food_id = query['food_id']
        for query in query_user:
            user_id = query['id']
        create_misite_price(price,user_id,food_id,market_id)
        # return HttpResponseRedirect('mygis/marketdetail')
    return render(request,'mygis/marketfoodadd.html',locals())

# 信息采集员添加小区人数
@login_required
@csrf_exempt
def marketpeopleadd(request):
    com_id=None
    if request.method == 'GET':
        id = request.GET.get('id')
        c_id = str(id).split('_')
        com_id = c_id[1]
    query_user = User.objects.filter(username=request.user).values()
    print(request.method)
    if request.method == 'POST':
        id = request.POST.get('id',None)
        people_num = request.POST.get('people_num',None)
        #添加人数
        for query in query_user:
            u_id = query['id']
        print('添加人口')
        create_misite_people(people_num,u_id,id)
    return render(request,'mygis/communitypeopleadd.html',locals())

# 信息采集员添加流量及摊位
@login_required
@csrf_exempt
def markettanweiadd(request):
    id = request.GET.get('id')
    m_id = str(id).split('_')
    mar_id = m_id[1]
    query_user = User.objects.filter(username=request.user).values()
    if request.method == 'POST':
        people_flow = request.POST.get('people_flow',None)
        tanwei_num = request.POST.get('tanwei_num',None)
        tanwei_use_num = request.POST.get('tanwei_use_num',None)
        
        #添加人数
        for query in query_user:
            u_id = query['id']
        print(people_flow,tanwei_num,tanwei_use_num,m_id,u_id)
        create_misite_message(people_flow,tanwei_num,tanwei_use_num,mar_id,u_id)
        return render(request,'mygis/people_tanwei.html',locals())
    return render(request,'mygis/marketpeopleadd.html',locals())

# 管理员查看菜品
@login_required
@csrf_exempt
def marketfoodshow(request):
    id = request.GET.get('id',None)
    print(id)
    id = User.objects.filter(id=id).values()
    for i in id:
        print(i['id'])
    return render(request,'mygis/marketfoodshow.html',locals())

# 管机员菜品价格查询
@login_required
@csrf_exempt
def marketfoodsearch(request):
    logo = '管理员'
    content = '价格查询'
    market_name = request.GET.get('market_name',None)
    page = request.GET.get('page',1)
    message = '价格查询'
    time = timezone.now()
    query = query_misite_market(market_name)
    for q in query:
        market_id = q['market_id']
        market_address = q['market_address']
        market_phone = q['market_phone']
        data_time = q['data_time']
        status = q['status']
        if status == '0':
            update_mysite_market(None,market_name)
    return render(request,'mygis/marketfoodsearch.html',locals())

# # 高德地图
# @login_required
# @csrf_exempt
# def js_page_map(request):
#     return render(request,'mygis/JS_Page_Map.html',locals())

# 管理员信息审核
@login_required
@csrf_exempt
def checkmessage(request):
    logo = '管理员'
    content = '信息审核'
    return render(request,'mygis/checkmessage.html',locals())

# 菜市场信息审核
@login_required
@csrf_exempt
def checkmarketfood(request):
    logo = '管理员'
    content = '菜市场审核'
    message = '信息审核'
    query = query_misite_market()
    paginator = Paginator(query,3) # 每页三条数据
    page = request.GET.get('page',1)  # 接受网页中的page值
    try:
        customer = paginator.page(page)
    except PageNotAnInteger:
        customer = paginator.page(1)
    except EmptyPage:
        customer = paginator.page(paginator.num_pages)
    cus_list = customer.object_list
    return render(request,'mygis/marketmessage_user.html',locals())


# 小区人数审核  
@login_required
@csrf_exempt
def checkcommunity(request):
    logo = '管理员'
    content = '菜市场审核'
    message = '信息审核'
    query = query_misite_market()
    paginator = Paginator(query,3) # 每页三条数据
    page = request.GET.get('page',1)  # 接受网页中的page值
    try:
        customer = paginator.page(page)
    except PageNotAnInteger:
        customer = paginator.page(1)
    except EmptyPage:
        customer = paginator.page(paginator.num_pages)
    cus_list = customer.object_list
    return render(request,'mygis/communitymessage.html',locals())


# 管理员信息管理之 菜品菜价搜索
@login_required
@csrf_exempt
def marketsearchbyfood(request):
    content = '菜品查看'
    logo = '管理员'
    food = query_misite_food()
    food_set = []
    for f in food:
        food_set.append(f['food_name'])
    food_set = set(food_set)
    food_set = list(food_set)
    if request.method == 'POST':
        pass
    if request.method == 'GET':
        search = request.GET.get('search',None)
        market_name = []
        # 未搜索菜品时 返回值为空 即查询结果为空
        if search:
            query_price = None
            food = query_misite_food(search,None)
            if food:
                search = search
            else:
                search = None
            for f in food:
                f_id = f['food_id']
                
                query_price = query_misite_price_by_foodid(f_id)
                # print(query_price)
                for query in query_price:
                    price = query['price']
                    market_id = query['market_id_id']
                    date_time = query['data_time']
                    market = query_misite_marketbyid(market_id)
                    name = None
                    for m in market:
                        name = m['market_name']
                        if name not in market_name:
                            
                            market_name.append(name)
            paginator = Paginator(market_name,2) # 每页三条数据
            page = request.GET.get('page',1)  # 接受网页中的page值
            try:
                customer = paginator.page(page)
            except PageNotAnInteger:
                customer = paginator.page(1)
            except EmptyPage:
                customer = paginator.page(paginator.num_pages)
            cus_list = customer.object_list
    return render(request,'mygis/marketsearchbyfood.html',locals())

# 管理员信息管理之 菜品菜价搜索结果展示
@login_required
@csrf_exempt
def marketsearchshow(request):
    content = '菜品查看'
    logo = '管理员'
    if request.method == 'POST':
        return HttpResponse('hee')
    if request.method == 'GET':
        search = request.GET.get('search',None)
        market_name = request.GET.get('market_name',None)
        page = request.GET.get('page',None)
        start_time = request.GET.get('start_time',None)
        end_time = request.GET.get('end_time',None)
        # start_split = str(start_time).split('/')
        # end_split = str(end_time).split('/')
        # smonth = str(int(start_split[0]))
        # emonth = str(int(end_split[0]))
        # start = int(start_split[2]+smonth+start_split[1])
        # end = int(end_split[2]+emonth+end_split[1])
        timess = []
        market_id = None
        food_id = []
        price = []
        times = []
        timesss = []
        result_time = []
        start = 0
        end = 0
        if market_name:
            market = query_misite_market(None,market_name)
            for i in market:
                market_id = i['market_id']
        if search:
            food = query_misite_food(search,None)
            for i in food:
                food_id.append(i['food_id'])
        for id in food_id:
            query = query_price(market_id,id)
            print(query)
            if len(query)>0:
                for q in query:
                    date_time = q['data_time']
                    date_year = date_time.year
                    date_month = date_time.month
                    date_day = date_time.day
                    date_times = str(date_year)+"/"+str(date_month)+"/"+str(date_day)
                    date_times_01 = str(date_year)+str(date_month)+str(date_day)
                    item = {}
                    item['price'] = q['price']
                    item['time'] = date_times
                    times.append(date_times)
                    timess.append(date_times_01)
                    price.append(item)
        if start_time:
            start_split = str(start_time).split('/')
            end_split = str(end_time).split('/')
            smonth = str(int(start_split[0]))
            emonth = str(int(end_split[0]))
            start = int(start_split[2]+smonth+start_split[1])
            end = int(end_split[2]+emonth+end_split[1])
            for t in sorted(times):
                date = t.split('/')
                year = date[0]
                month = int(date[1])
                day = date[2]
                ts = str(year)+str(month)+str(day)
                if int(ts)>=int(start) and int(ts)<=int(end):
                    result_time.append(t)
        else:
            result_time = sorted(times)[-7:]
        sort_times = sorted(times)[-7:]
        for t in sorted(timess):
            if int(t)>=int(start) and int(t)<=int(end):
                timesss.append(t)
     
        result_price = []
        print(price)
        for time in result_time:
            for p in price:
                if str(time) == str(p['time']):
                    result_price.append(p['price'])
                    print(p['price'],p['time'])
        print(result_price,result_time)
        
    return render(request,'mygis/marketsearchshow.html',locals())


@login_required
def marketsearchbycom(request):
    if str(request.user) == 'admin':
        logo = '管理员'
    else:
        logo  = '信息采集员'   
    if request.method == 'POST':
        content = request.POST["context"]
        addr = request.POST.get('addr',None)
        # print(addr)
        return HttpResponse(json.dumps({'logo':logo,'context':content}))
    elif request.method == 'GET':
        content = "指标查看"
        province = request.GET.get('p',None)
        city = request.GET.get('c',None)
        district = request.GET.get('d',None)
        # 查询餐馆
        query_result = query_misite_restaurant()
        result = {}
        for query in query_result:
          
            result[query['restaurant_name']] = [query['restaurant_long'],query['restaurant_dimen']]
            
        print('---------------',json.dumps(result))
        json_result = json.dumps(result)
        
    else:
        content = '首页'

    return render(request,'mygis/marketsearchbycom.html',locals())
@csrf_exempt
@login_required
def marketsearchbycan(request):
    if str(request.user) == 'admin':
        logo = '管理员'
    else:
        logo  = '信息采集员'   
    if request.method == 'POST':
        content = request.POST["context"]
        addr = request.POST.get('addr',None)
        # print(addr)
        return HttpResponse(json.dumps({'logo':logo,'context':content}))
    elif request.method == 'GET':
        content = "指标查看"
        province = request.GET.get('p',None)
        city = request.GET.get('c',None)
        district = request.GET.get('d',None)
        # 查询小区人数
        print(province)
        query_result = query_people_all()
        result = {}
        for query in query_result:
            com_id = query['community_id_id']
            num = query['num_people']
            com_query = query_misite_community(None,None,com_id)
            for c_query in com_query:
                result[num] = [c_query['community_long'],c_query['community_dimen']] 
            
        print('---------------',json.dumps(result))
        json_result = json.dumps(result)
        
    else:
        content = '首页'
    return render(request,'mygis/marketsearchbycan.html',locals())
