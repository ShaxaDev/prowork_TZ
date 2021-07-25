from django.shortcuts import render
from operator import attrgetter
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .forms import FilterForm
from blog.views import get_blog_queryset
from blog.models import BlogPost, Category
from account.models import Territory
from django.db.models import Q
BLOG_POSTS_PER_PAGE = 2

def home_screen_view(request, *args, **kwargs):
	blog_posts=BlogPost.objects.all()
	context = {}
	if request.method=='POST':
		territory=None
		category=None
		if request.POST['categories']!='':
			category=Category.objects.get(pk=request.POST.get('categories',' '))
		elif request.POST['territories']!='':
			territory=Territory.objects.get(pk=request.POST.get('territories',' '))
		if category and territory is None:
			blogs=BlogPost.objects.filter(category=category)
		elif territory and category is None:
			blogs=BlogPost.objects.filter(territory=territory)
		else:
			blogs=BlogPost.objects.filter(Q(category=category) | Q(territory=territory))

		print(blogs)
		blog_posts=blogs
	# Search
	query = ""
	if request.GET:
		query = request.GET.get('q', '')
		context['query'] = str(query)

		blog_posts = sorted(get_blog_queryset(query), key=attrgetter('date_updated'), reverse=True)
	


	# Pagination
	page = request.GET.get('page', 1)
	blog_posts_paginator = Paginator(blog_posts, BLOG_POSTS_PER_PAGE)
	try:
		blog_posts = blog_posts_paginator.page(page)
	except PageNotAnInteger:
		blog_posts = blog_posts_paginator.page(BLOG_POSTS_PER_PAGE)
	except EmptyPage:
		blog_posts = blog_posts_paginator.page(blog_posts_paginator.num_pages)

	context['blog_posts'] = blog_posts
	context['form']=FilterForm
	return render(request, "personal/home.html", context)



