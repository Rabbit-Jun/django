from django.db import models

# 데이터 모델.
#idx ( idx ==pk ,기본키는 장고에서 자동으로 만들어 줌)
#memo_txt
#published_date

# Memo라는 이름으로 테이블이 생성된다
class Memo(models.Model): #models.Model은 기본 틀,Model이 사용하는 method
    memo_text = models.CharField(max_length=200) #문자제한을 두고 싶을 때 사용, TextField를 사용하면 제한 없이 입력 가능
    published_date= models.DateTimeField(auto_now_add=True) #날짜 시간을 자동으로 추가 auto_now_add=True

    def __str__(self): #이 메서드는 객체를 문자열 형식으로 나타내기 위한 목적으로 사용된다 
        return self.memo_text 


#작성 후 Admin사이트에 반영하기 위해 admin.py를 열고 추가 작성을 해줘야한다.
