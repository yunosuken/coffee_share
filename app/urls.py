from django.urls import path
from .views import index
from .views import sign_in
from .views import sign_up

app_name = 'app'
urlpatterns = [
    # トップ画面
    path('', index.index, name='index'),
    # サインイン画面
    path('sign_in/', sign_in.sign_in, name='sign_in'),
    # サインアップ画面
    path('sign_up/', sign_up.sign_up, name='sign_up'),
    path('user_register/', sign_up.register, name='user_register'),
    # path('book/add/', views.book_edit, name='book_add'),  # 登録
    # path('book/mod/<int:book_id>/', views.book_edit, name='book_mod'),  # 修正
    # path('book/del/<int:book_id>/', views.book_del, name='book_del'),   # 削除
]