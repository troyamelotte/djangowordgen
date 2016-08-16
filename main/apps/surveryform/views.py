from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'surveyform/index.html')
def submit(request):
    if request.method == 'POST':
        request.session['first']=request.POST['first']
        request.session['dojo']=request.POST['dojo']
        request.session['lang']=request.POST['lang']
        request.session['comment']=request.POST['comment']
        return redirect('/result')
    else:
        return redirect('/')
def result(request):

    return render(request, 'surveyform/result.html')
