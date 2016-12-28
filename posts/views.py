from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from posts.models import Post
from posts.forms import PostCreateForm
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import FormView, CreateView
from django.views.generic.detail import DetailView
from django.utils import timezone


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
	success_url = '/posts/'

	def form_valid(self, form):
		return super(PostCreate, self).form_valid(form)

class PostList(ListView):
	model = Post
	context_object_name = 'all_posts'
	template_name = 'posts/posts.html'

class PostDetail(DetailView):
	model = Post
	template_name = 'detail.html'

	def get_context_data(self, **kwargs):
		context = super(PostDetail, self).get_context_data(**kwargs)
		context['now'] = timezone.now()
		return context

def post_detail(request):
	instance=get_object_or_404(Post, title="Сообщение 1")
	context={
		"title":instance.title,
		"instance":instance,
	}
	return render(request, "posts/post_detail.html", context)

def index(request):
	context={
		"title":"Index"
	}
	return render(request, "posts/index.html", context)

def post_create(request):
	context={
		"title":"Create"
	}
	return render(request, "posts/index.html", context)	

def post_update(request):
	return HttpResponse("<h1>Hello</h1>")

def DeletePost(request, pk):
	post = Post.objects.filter(pk=pk).first()
	post.delete()
	return HttpResponseRedirect('/')

def post_list(request):
	if request.user.is_authenticated():
			context={
			"title":"My User List"
			}
	else:
		context={
			"title":"List"
		}
	return render(request, "posts/index.html", context)
