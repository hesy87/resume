
from django.urls import path,include
from resume.views import index_view
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index_view,name='index'),
]
