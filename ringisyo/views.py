from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import DepartmentForm
from .models import Department


def top_page(request):
    title, name = 'タイトルです', '有原'
    # top.htmlに渡す変数を、辞書型で渡す ネストしているなら、key.ネスト側のkeyでアクセスできる
    context = {'title': title, 'name': name}
    return render(request, 'ringisyo/top.html', context)


def question(request):
    context = {'title': 'クエスチョンフォーム'}
    return render(request, 'ringisyo/question.html', context)


def result(request):
    context = {'text': request.POST['text']}
    return render(request, 'ringisyo/result.html', context)


def dep_input(request):
    param = {'message': '', 'form': None}
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/ringisyo/depresult')
        else:
            param['messages'] = '再入力してください'
            param['form'] = form
    else:
        param['form'] = DepartmentForm()
    return render(request, 'ringisyo/depInput.html', param)


def dep_result(request):
    data = Department.objects.all()
    param = {'部署名': data}
    return render(request, 'ringisyo/depResult.html', param)
