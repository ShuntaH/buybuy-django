from django.urls import reverse_lazy
from django.views import generic

from .forms import DayCreateForm
from .models import Day

# Create your views here.


'''function
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

'''


class IndexView(generic.ListView):
    model = Day
    paginate_by = 3


class AddView(generic.CreateView):
    model = Day
    form_class = DayCreateForm

    # 単純なフォームだったらform_classはいらなくてこれでok
    # fields = '__all__'

    # redirect()はhttp response objectを返す関数
    # reverse_lazy()は文字列を返す関数
    success_url = reverse_lazy('memoapp:index')


class UpdateView(generic.UpdateView):
    model = Day
    form_class = DayCreateForm
    success_url = reverse_lazy('memoapp:index')



class DeleteView(generic.DeleteView):
    model = Day
    success_url = reverse_lazy('memoapp:index')


class DetailView(generic.DetailView):
    model = Day
