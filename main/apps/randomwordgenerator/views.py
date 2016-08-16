from django.shortcuts import render, redirect
import random
import string
# Create your views here.
def index(request):
    if not 'attempt' in request.session:
        request.session['attempt']=0
    request.session['attempt']+=1
    request.session['word']=''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])
    return render(request, 'randomwordgenerator/index.html')
def generate(request):
    return redirect('/')
