from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import * #현재 디렉토리에 있는 models.py 파일에서 모든 클래스와 함수를 가져오는 의미입니다. 
# Create your views here.
def index(request): #urls.py로 요청이 간 후  view파일의 index 함수를 호출하여 응답
    lists =Memo.objects.all()
    data= {'lists': lists}
    return  render(request,'main.html',data)
    
def createMemo(request):
    # memoContent=request.GET['memoContent']
    memoContent=request.POST['memoContent']

    #DB입력
    article = Memo(memo_text=memoContent)
    article.save()

    # return HttpResponse('CreateMemo='+  memoContent)
    

    #리다이렉트
    # 1.임포트 필요 -from django.http import HttpResponse,HttpResponseRedirect
    # from django.urls import reverse
    #2.redircet() 함수란?
    #   -view페이지 등에서 특정 로직 수행 후 다시 특정 url로 이동시키고자 할 때 사용.
    #3.reverse()함수란?
    #   -URL을 역으로 꼐산하여 path가 변경되어도 URL을 외울 필요 없음
    #   -urls.py에서 만든 urlpattern들의 name을 사용(name의 url을 반환)
    
    return HttpResponseRedirect(reverse('index')) 

def editPage(request, idx):
    # return HttpResponse('수정페이지=' + idx )
    article=Memo.objects.get(id=idx) #.get(id=idx)는 매니저 객체에 대해 호출하는 함수입니다. 이 함수는 주어진 조건(ID 값이 idx인 경우)에 대한 데이터베이스에서 단일 객체(레코드)를 반환합니다.
    data ={'article':article}

    return render(request,'edit.html',data)

def updateMemo(request):
    idx=request.POST['idx'] #post로 넘어오고 있으므로 requst.post로 받아야함
    memoContent=request.POST['memoContent']

    # return HttpResponse(idx +','+memoContent) 잘 되나 확인용
    #실질적인 DB에서의 수정 처
    db_article=Memo.objects.get(id=idx)
    db_article.memo_text=memoContent
    db_article.save()

    return HttpResponseRedirect(reverse('index'))

def deleteMemo(requeset,idx):
    # return HttpResponse(idx)
    
    #DB 삭제 처리
    db_article =Memo.objects.get(id =idx)
    db_article.delete()

    return HttpResponseRedirect(reverse('index'))
