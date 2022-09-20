from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils.translation import gettext as _

from .models import BlogPost
from .forms import PostForm


class PostListView(generic.ListView):
    template_name = 'blog/blog_list_temp.html'
    context_object_name = 'posts_list'
    paginate_by = 9

    def get_queryset(self):
        return BlogPost.objects.filter(status='p').order_by('-datetime_modified')


class PostDetailView(generic.DetailView):
    model = BlogPost
    template_name = 'blog/blog_detail_temp.html'
    context_object_name = 'blog'


class PostCreateView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    form_class = PostForm
    template_name = 'blog/blog_create_temp.html'
    success_message = _('your Blog post is now submitted')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, generic.UpdateView):
    model = BlogPost
    form_class = PostForm
    template_name = 'blog/blog_update_temp.html'
    success_message = _('your Blog Post Successfully updated')

    def test_func(self):
        return self.get_object().author == self.request.user


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, generic.DeleteView):
    model = BlogPost
    template_name = 'blog/blog_delete_temp.html'
    context_object_name = 'blog'
    success_url = reverse_lazy('blog_list')
    success_message = _('your Blog Post successfully deleted')

    def test_func(self):
        return self.get_object().author == self.request.user
