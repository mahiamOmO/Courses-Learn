from django.shortcuts import render
from .models import ChaiVarity
from django.shortcuts import get_object_or_404
from .forms import ChaiVarityForm

# Create your views here.
def all_chai(request):
    chais = ChaiVarity.objects.all()
    return render(request,'all_chai.html',{'chais': chais})

def chai_detail(request, chai_id):
    chai = get_object_or_404(ChaiVarity, id=id)
    return render(request, 'chai_detail.html', {'chai': chai})

def chai_stores_view(request):
    store = None
    if request.method == 'POST':
    form = ChaiVarityForm(request.POST)
    if form.is_valid():
       chai_varity =  form.cleaned_data['chai_varity']
       stores =  Store.objects.filter(chai_varieties= chai_varity)

    else:
        form = ChaiVarityForm()
    return render(request,'chai_stores.html',
    {'stores' : stores,'form': form})