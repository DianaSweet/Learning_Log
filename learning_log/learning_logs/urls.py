'''定义 learning_logs的url模式'''

from django.urls import re_path

from . import views

urlpatterns = [
    #主页
    re_path(r'^$', views.index, name='index'),

    #显示所有的主题
    re_path(r'^topics/$', views.topics, name='topics'),

    #显示特定的主题
    re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),

    #用于添加新主题的网页
    re_path(r'^new_topic/$', views.new_topic, name='new_topic'),

    #用于添加新条目的页面
    re_path(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),

    #用于编辑条目的页面
    re_path(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]