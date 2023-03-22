from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login

# Create your views here.
# 로그인 행위는 session을 생성
# POST 요청을 보낼 수 있는 페이지 필요 -> GET 요청 우선
# POST 요청
def login(request):
    if request.method == 'POST':
        # AuthenticationForm은 modelform 아니고 form이라서 request를 첫 인자로 받음
        # ctrl + 클릭으로 들어가서 찾고, 첫 인자 뭔지 살펴볼 수 있음
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():    # 유효성 검사
            # Article -> form.save() | DB에 그 Article 생성
            # AuthenticationForm -> ModelForm이 아니라 Model에 대한 정보 없음
            user = form.get_user()
            auth_login(request, user)
            return redirect('articles:index')

    # 인증 절차를 위한 form 태그 
    else:
        form = AuthenticationForm()
        print(form)
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    return redirect('')