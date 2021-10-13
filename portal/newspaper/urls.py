from django.urls import path
from .views import PostList, PostDetail, PostSearch, IndexView

urlpatterns = [
    path('news/', PostList.as_view()),
    path('news/search/', PostSearch.as_view()),
    path('<int:pk>', PostDetail.as_view()),
    path('index/', IndexView.as_view()),
]
