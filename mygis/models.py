from django.db import models
from django.db.models import Q
import django.utils.timezone as timezone
import datetime
from users.models import User


#菜市场
class Mysite_Market(models.Model,models.Manager):
    market_id = models.AutoField(primary_key=True)
    market_name = models.CharField(max_length = 100)
    market_address = models.CharField(max_length = 100)
    market_long = models.CharField(max_length = 100)
    market_dimen = models.CharField(max_length = 100)
    market_phone = models.CharField(max_length = 50)
    data_time = models.DateTimeField(default = timezone.now)
    status = models.CharField(max_length=10,default=0)
    
    people_flow = models.CharField(max_length=30,default=0)     # 日流量
    tanwei_num = models.CharField(max_length=30,default=0)      # 摊位数
    tanwei_use_num = models.CharField(max_length=30,default=0)  # 使用摊位数


def create_misite_market(*argv):
    market = Mysite_Market()
    market.market_name = argv[0]
    market.market_address = argv[1]
    market.market_long = argv[2]
    market.market_dimen = argv[3]
    market.market_phone = argv[4]
    market.save()

def query_misite_market(*argv):
    if argv:
        query = Mysite_Market.objects.filter(Q(market_address = argv[0])|Q(market_name = argv[1])).values()
    else:
        query = Mysite_Market.objects.all().values()
    return query

def query_misite_marketbyid(*argv):
    if argv:
        query = Mysite_Market.objects.filter(market_id = argv[0]).values()
    else:
        query = Mysite_Market.objects.all().values()
    return query
    
def update_mysite_market(*argv):
    Mysite_Market.objects.filter(Q(market_address = argv[0])|Q(market_name = argv[1])).update(status=1)

# 菜市场人流量及摊位
class Mysite_Market_Message(models.Model,models.Manager):
    message_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_mysite_market_message',default='')
    market = models.ForeignKey(Mysite_Market,on_delete=models.CASCADE,related_name='mysite_market_mysite_market_message',default='')
    people_flow = models.CharField(max_length=30,default=0)     # 日流量
    tanwei_num = models.CharField(max_length=30,default=0)      # 摊位数
    tanwei_use_num = models.CharField(max_length=30,default=0)  # 使用摊位数
    check = models.CharField(max_length=10,default=0)
    data_time = models.DateTimeField(default = timezone.now)

def create_misite_message(*argv):
    market = Mysite_Market_Message(people_flow=argv[0],tanwei_num=argv[1],tanwei_use_num=argv[2],market_id=argv[3],user_id_id=argv[4])
    market.save()

def query_misite_message(*argv):
    market = Mysite_Market.objects.get(Q(market_id = argv[0])|Q(market_name = argv[0]))
    message = market.mysite_market_mysite_market_message.all().values()
    return message

def update_mysite_message(*argv):
    Mysite_Market_Message.objects.filter(message_id = argv[0]).update(check=1)
#菜品
class Mysite_Food(models.Model,models.Manager):
    food_id = models.AutoField(primary_key=True)
    food_name = models.CharField(max_length = 100)
    # food_kind = models.CharField(max_length = 100)
    # market = models.ManyToManyField('Mysite_Market')      # 菜品 菜市场 多对多关系
# 添加菜品
def create_misite_food(*argv):
    food = Mysite_Food()
    food.food_name = argv[0]
    # food.food_kind = argv[1]
    food.save()


# 菜品查询
def query_misite_food(*argv):
    if argv:
        query = Mysite_Food.objects.filter(Q(food_name = argv[0])|Q(food_id = argv[1])).values()
    else:
        query = Mysite_Food.objects.all().values()
    return query

#评价
class Mysite_Asses(models.Model,models.Manager):
    asses_id = models.AutoField(primary_key=True)
    asses_comment = models.CharField(max_length = 100)
    market_id = models.ForeignKey(Mysite_Market,on_delete=models.CASCADE,related_name='mysite_market_mysite_asses')
    message_person_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_mysite_asses')

#日期
class Mysite_DataTime(models.Model,models.Manager):
    data_time_id = models.AutoField(primary_key=True)
    data_time = models.DateTimeField(default = timezone.now)

#价格采集任务
class Mysite_PriceTask(models.Model,models.Manager):
    task_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_mysite_pricetask')
    food_id = models.ForeignKey(Mysite_Food,on_delete=models.CASCADE,related_name='mysite_food_mysite_pricetask')
    market_id = models.ForeignKey(Mysite_Market,on_delete=models.CASCADE,related_name='mysite_market_mysite_pricetask')
    data_time = models.DateTimeField(default = timezone.now)
    check = models.CharField(max_length=10,default=0)
    price = models.CharField(max_length = 50)

def create_misite_price(*argv):
    market = Mysite_PriceTask(price=argv[0],user_id_id=argv[1],food_id_id=argv[2],market_id_id=argv[3])
    market.save()

def query_misite_price(*argv):
    # 根据菜市场查询菜价
    market = Mysite_Market.objects.get(Q(market_id = argv[0])|Q(market_name = argv[1]))
    price = market.mysite_market_mysite_pricetask.all().values()
    return price

def query_price(*argv):
    price = Mysite_PriceTask.objects.filter(Q(market_id_id = argv[0])&Q(food_id_id = argv[1])).order_by('data_time').values()
    return price
def query_misite_price_by_foodid(*argv):
    # 根据菜品查询菜价
    food = Mysite_Food.objects.get(food_id=argv[0])
    price = food.mysite_food_mysite_pricetask.all().values()
    return price

def update_mysite_price(*argv):
    Mysite_PriceTask.objects.filter(task_id = argv[0]).update(check=1)

# 问卷
class Mysite_Target(models.Model,models.Manager):
    target_id = models.AutoField(primary_key=True)
    market = models.ForeignKey(Mysite_Market,on_delete=models.CASCADE,related_name='mysite_market_mysite_target',default='')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_mysite_target',default='')
    lrzw = models.CharField(max_length = 100) # 乱认杂物 评分
    twzj = models.CharField(max_length = 100) # 摊位整洁 评分
    cyryywzj = models.CharField(max_length = 100) # 从业人员工作衣帽洁净 评分
    csws = models.CharField(max_length = 100) # 厕所卫生 评分
    # xfws = models.CharField(max_length = 100)
    cpxxcd = models.CharField(max_length = 100) # 菜品新鲜程度 评分
    pingfen = models.CharField(max_length = 30,default='') # 总评分
    check = models.CharField(max_length=10,default=0)
    data_time = models.DateTimeField(default = timezone.now)

def create_misite_target(*argv):
    target = Mysite_Target(market_id=argv[0],user_id=argv[1],lrzw=argv[2],twzj=argv[3],cyryywzj=argv[4],csws=argv[5],cpxxcd=argv[6],pingfen=argv[7])
    target.save()

def query_misite_target(*argv):
    # 根据菜市场查询问卷评分
    market = Mysite_Market.objects.get(Q(market_id = argv[0])|Q(market_name = argv[1]))
    target = market.mysite_market_mysite_target.all().values()
    return target

def query_misite_targetlast(*argv):
    # 根据菜市场查询问卷评分
    market = Mysite_Market.objects.get(Q(market_id = argv[0])|Q(market_name = argv[1]))
    target = market.mysite_market_mysite_target.all().order_by('-data_time')[0:1].values() # 时间降序排列
    return target
def update_mysite_target(*argv):
    Mysite_Target.objects.filter(target_id = argv[0]).update(check=1)
#社区
class Mysite_Community(models.Model,models.Manager):
    community_id = models.AutoField(primary_key=True)
    community_name = models.CharField(max_length = 100)
    community_address = models.CharField(max_length = 100)
    community_long = models.CharField(max_length = 100)
    community_dimen = models.CharField(max_length = 100)
    community_wyphone = models.CharField(max_length = 100)
    status = models.CharField(max_length=10,default=0)

def create_misite_community(*argv):
    community = Mysite_Community()
    community.community_name = argv[0]
    community.community_address = argv[1]
    community.community_long = argv[2]
    community.community_dimen = argv[3]
    community.community_wyphone = argv[4]
    community.save()

def query_misite_community(*argv):
    if argv:
        query = Mysite_Community.objects.filter(Q(community_address = argv[0])|Q(community_name = argv[1])|Q(community_id=argv[2])).values()
    else:
        query = Mysite_Community.objects.all().values()
    return query

def update_mysite_community(*argv):
    Mysite_Community.objects.filter(Q(community_address = argv[0])|Q(community_name = argv[0])).update(status=1)

#人口采集任务
class Mysite_PeopleTask(models.Model,models.Manager):
    task_id = models.AutoField(primary_key=True)
    num_people = models.IntegerField()
    message_person_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_mysite_peopletask')
    community_id = models.ForeignKey(Mysite_Community,on_delete=models.CASCADE,related_name='Mysite_Community_mysite_peopletask')
    check = models.CharField(max_length=10,default=0)
    data_time = models.DateTimeField(default = timezone.now)

def create_misite_people(*argv):
    people = Mysite_PeopleTask(num_people=argv[0],message_person_id_id=argv[1],community_id_id=argv[2])
    people.save()

def query_misite_people(*argv):
    # 根据小区查询人口
    community = Mysite_Community.objects.get(Q(community_id = argv[0])|Q(community_name = argv[1]))
    people = community.Mysite_Community_mysite_peopletask.all().values()
    return people
def query_people_all():
    query = Mysite_PeopleTask.objects.all().values()
    return query
def update_mysite_people(*argv):
    Mysite_PeopleTask.objects.filter(task_id = argv[0]).update(check=1)
#零售店
class Mysite_Store(models.Model):
    store_id = models.AutoField(primary_key=True)
    store_name = models.CharField(max_length = 100)
    store_address = models.CharField(max_length = 100)
    store_long = models.CharField(max_length = 100)
    store_dimen = models.CharField(max_length = 100)
    store_wyphone = models.CharField(max_length = 100)

#餐馆
class Mysite_Restaurant(models.Model,models.Manager):
    restaurant_id = models.AutoField(primary_key=True)
    restaurant_name = models.CharField(max_length = 100)
    restaurant_address = models.CharField(max_length = 100)
    restaurant_long = models.CharField(max_length = 100)
    restaurant_dimen = models.CharField(max_length = 100)
    restaurant_wyphone = models.CharField(max_length = 100)
    status = models.CharField(max_length=10,default=0)

def create_misite_restaurant(*argv):
    restaurant = Mysite_Restaurant()
    restaurant.restaurant_name = argv[0]
    restaurant.restaurant_address = argv[1]
    restaurant.restaurant_long = argv[2]
    restaurant.restaurant_dimen = argv[3]
    restaurant.restaurant_wyphone = argv[4]
    restaurant.save()

def query_misite_restaurant(*argv):
    if argv:
        query = Mysite_Restaurant.objects.filter(Q(restaurant_address = argv[0])|Q(restaurant_name = argv[0])).values()
    else:
        query = Mysite_Restaurant.objects.all().values()
    return query

def update_mysite_restaurant(*argv):
    Mysite_Restaurant.objects.filter(Q(restaurant_address = argv[0])|Q(restaurant_name = argv[0])).update(status=1)