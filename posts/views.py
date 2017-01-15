from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from posts.models import Post
from posts.forms import PostCreateForm, SettingForm
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import FormView, CreateView
from django.views.generic.detail import DetailView
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.http import HttpResponse

# Create your views here.
class Index(TemplateView):
	template_name = "posts/index.html"

	def get_context_data(self, **kwargs):
		context = super(Index, self).get_context_data(**kwargs)
		context['count'] = Post.objects.count()
		return context

class PostCreate(CreateView):
	template_name = 'posts/create.html'
	form_class = PostCreateForm
	success_url = '/posts/list'

	def form_valid(self, form):
		return super(PostCreate, self).form_valid(form)

class PostList(ListView):
	model = Post
	template_name = 'posts/posts.html'

	def get_context_data(self, **kwargs):
		context = super(PostList, self).get_context_data(**kwargs)
		context['now'] = timezone.now()
		return context

class PostDetail(DetailView):
	model = Post
	template_name = 'posts/detail.html'

	def get_context_data(self, **kwargs):
		context = super(PostDetail, self).get_context_data(**kwargs)
		context['now'] = timezone.now()
		return context

class Setting(TemplateView):
	template_name = "posts/setting.html"
	form_class = SettingForm
	success_url = '/posts/index'

	def form_valid(self, form):
		return super(Setting, self).form_valid(form)

def UpdatePost(request, pk):
	post = Post.objects.filter(pk=pk).first()
	form = PostCreateForm(request.POST or None,
						request.FILES or None, instance=post)
	if request.method == 'POST':
		if form.is_valid():
		   form.save()
		   return HttpResponseRedirect("/posts/list")
	return render(request, 'posts/update.html', {'form': form})

def DeletePost(request, pk):
	post = Post.objects.filter(pk=pk).first()
	post.delete()
	return HttpResponseRedirect("/posts/list")
