from django.forms import ModelForm
from posts.models import Post

# Create your tests here.

class PostCreateForm(ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'content')

class SettingForm(ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'content')