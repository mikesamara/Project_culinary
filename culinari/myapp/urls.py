from . import views
from django.urls import path, include
from django.contrib.auth import views as auth_views


urlpatterns = [

    path('', views.home, name='home'),
    path('all_recipe/', views.all_recipe, name='all_recipe'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('recipe_full/<int:category_id>/', views.recipe_full, name='recipe_full'),
    path('recept_text/<int:id_recipe>/', views.recept_text, name='recept_text'),
    path('users/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('user_login/<int:author_id>/', views.user_login, name='user'),
    path('logout/', views.user_logout, name='logout'),
    path('create_recipe/<int:id_recipe>', views.create_recipe, name='create_recipe'),
    path('delete_recipe/<int:id_recipe>', views.delete_recipe, name='delete_recipe'),
    path('delete_user/<int:id_user>', views.delete_user, name='delete_user'),



]
