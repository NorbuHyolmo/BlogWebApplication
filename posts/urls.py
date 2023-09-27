from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name="index"),
    path('post/<str:id>', views.post, name="post"),
    # path('add_blog', views.add_blog, name="add_blog"),
    path('add', views.add, name="add"),
    path('post/delete/<int:id>', views.delete, name="delete"),
    path('update/<int:id>', views.update, name="update")
]