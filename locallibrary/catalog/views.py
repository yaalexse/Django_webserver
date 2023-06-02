from django.shortcuts import render
from .models import Codes, new_Authors
from django.views import generic
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .forms import edit_new_code
from django.contrib.auth.decorators import login_required, permission_required
from . import code_checker as c_d
from django.http import JsonResponse
from django.views.generic.edit import FormView
from djangocodemirror.settings import *
from djangocodemirror.helper import codemirror_settings_update
from .forms import SignUpForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth import get_user_model
import re
User = get_user_model()

CODEMIRROR_SETTINGS = codemirror_settings_update(CODEMIRROR_SETTINGS, {
    'lineNumber': False,
    'indent': 6
})

def index(request):
	"""View function for home page of site."""
	
	num_authors = new_Authors.objects.all().count()
	num_codes = Codes.objects.all().count()
	
	context = {
		'num_authors': num_authors,
		'num_codes' : num_codes,
	}
	 
	return render(request, 'index.html',context=context)

#def ino_codes(request):
#	ino_code_l = Codes.objects.filter(language__icontains='ino')
#	ino_test = "c'est de la merde"
#	template = 'List_Codes.html'
#	context={
#		'ino_codes' : ino_code_l,
#	}
#	return render(request, template_name=template, context=context)

class ino(generic.ListView):
	model = Codes
	context_object_name = 'ino_codes'
	queryset = model.objects.all()
	template_name = 'List_Codes.html'
	#def get_queryset(self):
	#	return Codes.objects.filter(language__icontains='ino')
	#def get_context_data(self, **kwargs):
	#	object_list = Codes.objects.filter(title__icontains='shuffle')
	#	context = super(ino, self).get_context_data(object_list=object_list, **kwargs)
	#	return context

class new_auth(generic.ListView):
	model = new_Authors
	context_object_name = 'authors'
	queryset = model.objects.all()
	template_name = 'List_auth.html'


""""
class list_c_codes(generic.ListView):
	model = Codes
	context_name_object = 'list_c_codes'
	queryset = Codes.objects.filter(language__icontains='c')
	template_name = 'List_Codes.html'
"""
class code__detail(generic.DetailView):
	model = Codes
	template_name = 'code_detail.html'
"""
def code__detail(request):
	detail = Codes.objects.values()
	template = 'code_detailhtml'
	context = {
		'detail' : detail,
	}
	return render(request, template_name=template, context = context)
"""
"""
#@login_required
#@permission_required('catalog.can_mark_returned', raise_exception=True)
def edit_new_code_(request):
	username = request.user.username
	if request.method == 'POST':
		print('the code has been here')
		print(request.method)
		form = edit_new_code(request.POST)
		if form.is_valid():
			code=Codes.objects.create()
			code.description = form.cleaned_data['code_description']
			code.content = form.cleaned_data['code_content']
			code.title = form.cleaned_data['code_title']
			code.language = form.cleaned_data['code_language']
			code.save()
	#return HttpResponseRedirect(reverse('Ino'))
	context = {
		'form':form,
		'code':code,
	}
	return render(request, 'code_editing.html',context)

def new_date(request):
	if request.method == 'POST':
		form = test_form(request.POST)
		if form.is_valid():
			code = Codes.objects.create(
				content='this things is horrible',
				description = form.cleaned_data['description']
			)
		context ={
		'form':form,
		'code':code,
		}
	else:
		form = test_form(initial={'description':'this is just some bullshit'})
	context ={
		'form':form,
	}
	return render(request,'code_editing.html',context)
"""

def get_compilator_check(code,text_to_compil):
    result = c_d.cc(code.cleaned_data['code_language'],text_to_compil)
    return result

def edit_new_code_(request):
	if request.method == 'POST':
		form = edit_new_code(request.POST)
		if form.is_valid():
			my_user = User.objects.get(username = request.user)
			print(my_user.id)
			print(form.cleaned_data['code_content'])
			code=Codes.objects.create(
			description = form.cleaned_data['code_description'],
			content = form.cleaned_data['code_content'],
			title = form.cleaned_data['code_title'],
			language = form.cleaned_data['code_language'],
			author_id  = new_Authors.objects.get(name = my_user))
			code.save()
			is_submitted = 'the code has been submitted you can return on the main page'
			#result = get_compilator_check(form)
			#return HttpResponse(result)
			context ={
			'form':form,
			'code':code,
			'is_submitted':is_submitted
			}
	else:
		form = edit_new_code()
		result='this should be the result of the compilation'
		is_submitted = 'not submitted yet'
		context={
			'form':form,
			'result':result,
			'is_submitted':is_submitted
		}
	return render(request,'code_editing.html',context)

def compil_this_fcking_code(request):
	print(request.method)
	text = "the compilation output should be here"
	if request.method =='POST':
		form = edit_new_code(request.POST)
		print(form.is_valid())
		if form.is_valid():
			text_to_compil = form.cleaned_data['code_content']
			text_to_compil = re.sub("__LINEBREAK__", " ", text_to_compil, flags=re.IGNORECASE)
			print(text_to_compil)
			result_ = get_compilator_check(form,text_to_compil)
			if result_.returncode == 0:
				text = "The code has successfully compiled:    "+ result_.stdout
			else:
				text = "The compilation has failed" + result_.stderr
		else:
			text = form.errors
		return HttpResponse(text)

def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			user.refresh_from_db()
			user.save()
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=user.username,password=raw_password)
			login(request,user)
			author = new_Authors.objects.create(name = user)
			return redirect('index')
	else:
		form = SignUpForm()
	return render(request, 'signup.html', {'form':form})

