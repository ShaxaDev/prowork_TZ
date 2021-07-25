from django import forms

from blog.models import BlogPost ,Category
from account.models import Territory


class CreateBlogPostForm(forms.ModelForm):
	title=forms.CharField(label="<b>Maqola nomi</b>",max_length=100,widget=forms.TextInput(attrs={'placeholder':'Maqola nomini yozing'}))
	category=forms.ModelChoiceField(label="<b>Kategoriya</b>",empty_label='Kategoriya tanlang',queryset=Category.objects.all())
	category=forms.ModelChoiceField(label="<b>Xudud</b>",empty_label='Kategoriya tanlang',queryset=Territory.objects.all())
	
	body=forms.CharField(label='<b>Maqola matni</b>',widget=forms.Textarea())
	image=forms.ImageField(label='<b>Maqola uchun rasm</b>')
	class Meta:
		model = BlogPost
		fields = ['title', 'category','territory','body', 'image']


class UpdateBlogPostForm(forms.ModelForm):

	class Meta:
		model = BlogPost
		fields = ['title', 'body', 'image']

	def save(self, commit=True):
		blog_post = self.instance
		blog_post.title = self.cleaned_data['title']
		blog_post.body = self.cleaned_data['body']

		if self.cleaned_data['image']:
			blog_post.image = self.cleaned_data['image']

		if commit:
			blog_post.save()
		return blog_post

