from django.urls import path
from . import views

app_name = 'ringisyo'
urlpatterns = [
    # path(表示されるurl, views.処理を行う関数名)
    # pathの引数nameは、html等でurlを指定する際に,' app_name : 設定したname 'とすることで、
    # html等のurlの記述を変えずともurls.pyのメンテナンスを行うことが出来る
    path('', views.top_page, name='top'),
    path('question/', views.question, name='question'),
    path('result/', views.result, name='result'),
    path('dep/', views.dep_input, name='dep'),
    path('depresult/', views.dep_result, name='dep_result')
]
