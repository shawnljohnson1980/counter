from django.shortcuts import render,redirect



def index(request):
    if "count" not in request.session:
        request.session['count']=0
    request.session['count']+=1
    context={
        'count':request.session['count']
    }
    return render(request, 'index.html', context)

def refresh(request):
    request.session.flush()
    return redirect('/')

        
