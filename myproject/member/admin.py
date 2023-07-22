from django.contrib import admin
from member.models import Memo #member의 modles에 작성한 Memo를 불러옴
# Register your models here.

admin.site.register(Memo) #admin site에 Memo 등록

