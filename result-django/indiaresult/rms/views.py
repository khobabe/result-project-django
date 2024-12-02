from django.shortcuts import render,redirect
from .forms import InsertResultForm

# Create your views here.
def home(req):
    return render(req,"index.html")

def insertFunction(request):
    data = {}
    form = InsertResultForm(request.POST or None)
    
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(home)
    data['insertForm'] = form
        
    return render(request, "insert.html", data)