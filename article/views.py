from django.http import HttpResponse

from django.template.loader import get_template

from django.shortcuts import render_to_response

from django.template import Context

from django.shortcuts import render

from django.views.generic.base import TemplateView

from article.models import Article

#from forms import ArticleForm

from django.http import HttpResponseRedirect

from django.core.context_processors import csrf

def articles(request):
	return render_to_response('articles.html',
		{'articles': Article.objects.all() })

def article(request, article_id=1):
	return render_to_response('article.html',
					{'article': Article.objects.get(id=article_id) })

def home(request):
	return render(request,"home.html")
	#return render(request,'home.html')


"""
def create(request):
	if request.POST:
		form = ArticleForm(request.POST)
		if form.is_valid():
			form.save()

			return HttpResposeRedirect('/articles/all')
			
		else:
			form = ArticleForm()

		args = {}
		args.update(csrf(request))

		args['form']= form

		return render_to_response('create_article.html', args)
"""


