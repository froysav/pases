from django.urls import path
from django.urls import path
from apps import views
from django.urls import path
from .views import Blog,a_blog,w_comment_blog


app_name = 'shop'


urlpatterns = [
    path('', Blog, name='Blog'),
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('add_comment_blog/<int:pk>', w_comment_blog, name='w_comment_blog'),
    path('add_blog', a_blog, name='a_blog'),

]



