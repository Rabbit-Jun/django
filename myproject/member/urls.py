from django.urls import path
from . import views
urlpatterns =[
    #localhost:8000/member/ 가 기본적으로 있음
    path('',views.index, name='index'),
    path('createMemo/',views.createMemo), #주소에 createMemo/를 입력하면  views.createMemo를 호출

    #수정 페이지 요청
    path('edit/<str:idx>',views.editPage),

    #수정 처리 DB 요청
    path('edit/update/',views.updateMemo),

    #삭제 처리 DB
    path('delete/<str:idx>',views.deleteMemo)
] 