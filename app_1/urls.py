from django.urls import path

from app_1 import views


urlpatterns = [
    path('', views.job_list, name="jobs_home"),
    path('hello/',views.hello, name="hello"),
    path('job/<int:id>',views.job_detail_page, name="jobs_detail"),
]