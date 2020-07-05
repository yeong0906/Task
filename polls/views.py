from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from polls.models import Shoe, Accessories

def index(request):
    shoe = Shoe.objects.all()
    context = {'shoe': shoe}
    return  render(request, 'templates/polls/shoes.html',context)
    str = ''
    for shoe in shoe:
        str += "<p>{}".format(shoe.name,shoe,product_detail())+"</p>"

def index(request):
    accessories = Accessories.objects.all()
    context = {'accessories': accessories}
    return  render(request, 'templates/polls/shoes.html',context)
    str = ''
    for shoe in shoe:
        str += "<p>{}".format(accessories.name,accessories,product_detail())+"</p>"

def main(request):
    return render(request,'main.html')

def shoe(request):
    return render(request,'shoe.html')

def product_detail(request, id, product_slug=None) :
    return  render(request,'templates/shoe.html',{'product':product})

def shoe(request):
    shoe = Shoe.objects.all()
    contexr = {'shoe':shoe}
    return render(request,'templates/main.html')

# Create your views here.

