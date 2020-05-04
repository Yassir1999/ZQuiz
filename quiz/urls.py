from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name="index"),
    path('home/', views.index, name="index"),
    path('home', views.index, name="index"),
    path('new/', views.new, name="new"),
    path('new', views.new, name="new"),
    path('new/<int:pageNumber>', views.newbypagenumber, name="newbypagenumber"),
    path('popular/', views.popular, name="popular"),
    path('popular', views.popular, name="popular"),
    path('popular/<int:pageNumber>', views.popularbypagenumber, name="popularbypagenumber"),
    path('categories/', views.categories, name="categories"),
    path('categories', views.categories, name="categories"),
    path('categories/<int:Category_id>', views.searchbyCategory, name="searchbycategory"),
    path('categories/<int:Category_id>/page<int:pageNumber>', views.searchbycategorybypagenumber, name="searchbycategorybypagenumber"),
    path('results', views.search, name="search"),
    path('results/', views.search, name="search"),
    path('quizzes', views.quizzes, name="quizzes"),
    path('quizzes/', views.quizzes, name="quizzes"),
    path('quizzes/page<int:pageNumber>', views.allbypagenumber, name="allbypagenumber"),
    path('quizzes/<int:Quiz_id>', views.startQuiz, name="startQuiz"),
]
