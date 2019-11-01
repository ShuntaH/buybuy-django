from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from .forms import DayCreateForm
from .models import Day


# Create your views here.


class IndexView(LoginRequiredMixin, generic.ListView):
    model = Day
    paginate_by = 8
    login_url = '/buybuy/signin/'

    def get_queryset(self):
        return Day.objects.filter(user=self.request.user)


class AddView(LoginRequiredMixin, generic.CreateView):
    model = Day
    form_class = DayCreateForm
    # fields = '__all__'
    login_url = '/buybuy/signin/'

    # 単純なフォームだったらform_classはいらなくてこれでok
    # fields = '__all__'

    # redirect()はhttp response objectを返す関数
    # reverse_lazy()は文字列を返す関数
    success_url = reverse_lazy('memoapp:index')

    def form_valid(self, form):
        messages.success(self.request, 'Your  desire was added successfully')
        form.instance.user = self.request.user
        response = super().form_valid(form)
        return response


class UpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Day
    form_class = DayCreateForm
    login_url = '/buybuy/signin/'
    success_url = reverse_lazy('memoapp:index')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Your desire is updated')
        return response


class DeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Day
    login_url = '/buybuy/signin/'
    success_url = reverse_lazy('memoapp:index')

    def delete(self, request, *args, **kwargs):
        response = super().delete(self)
        messages.success(self.request, 'Deleted successfully')
        return response


class DetailView(LoginRequiredMixin, generic.DetailView):
    model = Day
    login_url = '/buybuy/signin/'


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('memoapp:signin')
    template_name = 'memoapp/signup.html'

    def post(self, request, *args, **kwargs):
        response = super().post(self)
        messages.success(self.request, 'Your account was created successfully')
        return response


# class ProfileView(generic.TemplateView):
#     model = User
#     template_name = 'memoapp/base.html'


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
