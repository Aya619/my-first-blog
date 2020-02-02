from django.shortcuts import render
from .models import Prop
# Create your views here.
def prop(request):
	props = Prop.objects.filter()
	return render(request, 'mysite/prop.html', {'props':props})
