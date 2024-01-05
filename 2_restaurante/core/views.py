from django.shortcuts import render
from categos.models import Category

# Create your views here.
def inicial (request):
    categorys = Category.objects.all()
    return render(request,"core\inicial.html", {'categorys':categorys})
    

def platoXCate (request, category_id):
    platoXCate = Category.objects.get(id=category_id)
    return render(request,"core\platoXCate.html",  {'platoXCate':platoXCate})
    