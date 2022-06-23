from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView
from django.views.generic import ListView, DetailView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import CreateView, DeleteView
from .forms import CommentForm
from .models import Form


# ================COMMENT
# Create your views here.

class PostListView(ListView):  # POSTLARNI BOSH SAHIFALARDA KO'RSATADI
    model = Form
    template_name = 'home.html'
    paginate_by = 13
    # context_object_name = 'posts'


class PostDisplay(DetailView):  # POSTLARNI KO'RISH UCHUN KIRADI
    model = Form
    template_name = 'form_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context


class PostComment(SingleObjectMixin, FormView):  # COMMENTLAR YARATADI
    model = Form
    form_class = CommentForm
    template_name = 'form_detail.html'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(PostComment, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = self.object
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        post = self.get_object()
        return reverse('post_detail', kwargs={'pk': post.pk}) + '#comments'


class PostDetailView(View):  # POSTLARNI KO'RSATISH VA COMMENTLAR BILAN ISHLAYDI

    def get(self, request, *args, **kwargs):
        view = PostDisplay.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = PostComment.as_view()
        return view(request, *args, **kwargs)


# ==============================CEATE FORM=======================================
class FormDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):  # FORMANI O'CHIRISH
    model = Form
    template_name = 'form_delete.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class FormCreateView(LoginRequiredMixin, CreateView):  # FORMANI YARATISH
    model = Form
    template_name = 'form_new.html'
    fields = ('kitob_nomi',
              'kitob_muqovasi',
              'kitob_fayli',
              'muallif',
              'bolim',
              'ishlab_chiqaruvchi',
              'til',
              'seriya',
              'yil',
              'bet',
              'kitob_haqida',
              'isbn',
              'kitob_shakli',)

    def form_valid(self, form):  # new
        form.instance.author = self.request.user
        return super().form_valid(form)

# ==========SEARCH FORM ======================

class BlogSearchView(ListView):
    model = Form 
    template_name = 'home.html'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        return Form.objects.filter(kitob_nomi__icontains=query).order_by('-created')