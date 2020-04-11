from django.shortcuts import render
from .models import Prop,Prop_cal,Prop_liner,Prop_mine

# Create your views here.
def index(request):
	return render(request, 'mysite/index.html')
def cal(request):
	props = Prop_cal.objects.filter()
	return render(request, 'mysite/cal.html', {'props':props})

def prop(request):
	props = Prop.objects.filter()
	return render(request, 'mysite/prop.html', {'props':props})
def liner(request):
	props = Prop_liner.objects.filter()
	return render(request, 'mysite/liner.html', {'props':props})
def mine(request):
	props = Prop_mine.objects.filter()
	return render(request, 'mysite/mine.html', {'props':props})
	
