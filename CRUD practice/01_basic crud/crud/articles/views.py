from django.shortcuts import render, redirect

# models.py에서 가져올 모델
from .models import Article

# 만든 form import 해오기
from .forms import ArticleForm


def index(request):
    articles = Article.objects.all()
    context = {
        'articles':articles
    }
    return render(request, 'articles/index.html', context)


# request랑 pk가 같이 들어온다
def detail(request, pk):

    #들어온 pk를 가진 Article 객체를 디비에서 불러옴
    article = Article.objects.get(pk=pk)    
    context = {
        'article':article
    }
    return render(request, 'articles/detail.html', context)


# 글 작성용 form만 가져오는 new함수는 create랑 합쳐졌음~!
# def new(request):
#     form = ArticleForm()
#     context = {
#         'form':form
#     }
#     return render(request, 'articles/new.html', context)


def create(request):

    # POST일 때 == 글 작성한거 디비에 저장시키기!!
    if request.method == 'POST':
        # ArticleForm에 포함된 데이터를 form 변수에 담는다
        form = ArticleForm(request.POST)

        # 만약 이 form이 valid하면 디비에 저장하고 상세페이지로 넘어간다
        if form.is_valid():
            article = form.save()
            # save된 article에서 pk값을 가지고 상세페이지로 보냄
            return redirect('articles:detail', article.pk)
    
    # GET일 때 == 글 작성할 FORM 불러오기!!
    else:
        form = ArticleForm()
    
    context = {
        'form':form
    }
    return render(request, 'articles/new.html', context)


def delete(request, pk):
    # request랑 같이 들어온 pk를 디비에서 찾아냄
    article = Article.objects.get(pk=pk)

    # 아무나 링크로 삭제 못하게 POST인지 확인먼저
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')

    # GET 요청은 그냥 삭제 안하고 다시 상세페이지로
    else:
        return redirect('aritlces:detail', article.pk)


def update(request, pk):
    # 우선 바꾸고 싶은 article 객체 찾기
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        # instance = find an existing model instance from database
        # if target instance is found from the database, save() will update that instance
        # else, save() will create a new instance of the specified model
        form = ArticleForm(request.POST, instance=article)

        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)

    else:
        form = ArticleForm(instance=article)
    context = {
        'form':form,
        'article':article
    }
    return render(request, 'articles/update.html', context)