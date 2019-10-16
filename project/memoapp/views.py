from django.shortcuts import render, redirect, get_object_or_404
from .forms import DayCreateForm
from .models import Day
# Create your views here.


def index(request):
    context = {
        'day_list': Day.objects.all(),
    }
    return render(request, 'memoapp/day_list.html', context)


def add(request):
    # context = {
    #     'form': DayCreateForm()
    # }
    # return render(request, 'memoapp/day_form.html', context)

    # 送信内容をもとにフォームを作る。POSTじゃなければ空のフォーム
    form = DayCreateForm(request.POST or None)

    # method=POST,つまり送信ボタンを押した時、入力内容に問題が無ければ
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('memoapp:index')

    # 通常時にページアクセスや、入力内容に誤りがあればまたページを表示
    context = {
        'form': form
    }
    return render(request, 'memoapp/day_form.html', context)


def update(request, pk):
    # urlのpkをもとに、Dayを取得
    day = get_object_or_404(Day, pk=pk)

    # フォームに取得したDayを紐付ける
    form = DayCreateForm(request.POST or None, instance=day)

    # method=POST,つまり送信ボタンを押した時、入力内容に問題が無ければ
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('memoapp:index')

    # 通常時のページアクセスや、入力内容に誤りがあればまたページを表示
    context = {
        'form': form
    }
    return render(request, 'memoapp/day_form.html', context)


def delete(request, pk):
    day = get_object_or_404(Day, pk=pk)

    if request.method == 'POST':
        day.delete()
        return redirect('memoapp:index')


    context = {
        'day': day,
    }
    return render(request, 'memoapp/day_confirm_delete.html', context)


def detail(request, pk):
    day = get_object_or_404(Day, pk=pk)

    context = {
        'day': day,
    }
    return render(request, 'memoapp/day_detail.html', context)
