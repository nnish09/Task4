from django.shortcuts import render,reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from client.models import Client
from .forms import ClientForm,UpdateProfile
from django.views.generic import TemplateView, ListView

from django.db.models import Q
# Create your views here.


def base(request):
    return render(request, 'base.html')



def client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():        
            form.save()            
            return HttpResponseRedirect(reverse('get_clients'))
        
    else:
        form = ClientForm()
    return render(request, 'client_form.html', {
        'form': form
    })



# class SearchResultsView(ListView):
#     model = Client
#     template_name = 'search_results.html'

#     def get_queryset(self): # new
#         query = self.request.GET.get('q')
#         object_list = Client.objects.filter(
#             Q(client_name__icontains=query) | Q(email__icontains=query)| Q(phone_no__icontains=query)| Q(suburb__icontains=query)
#         )
#         return object_list




def search(request):        
    if request.method == 'GET':      
        query =  request.GET.get('q')      
        object_list = Client.objects.filter(Q(client_name__icontains=query) | Q(email__icontains=query)| Q(phone_no__icontains=query)| Q(suburb__icontains=query)) 
        return render(request,"get_clients.html",{"object_list":object_list})
   

# def get_clients(request):
#     object_list = Client.objects.all().order_by('client_name','email','phone_no','suburb')
#     return render(request, 'get_clients.html', {"object_list":object_list})
  

# def get_clients(request):
#     if request.method == 'POST':      
#         query =  request.POST.get('q')      
#         clients = Client.objects.filter(Q(client_name__icontains=query) | Q(email__icontains=query)| Q(phone_no__icontains=query)| Q(suburb__icontains=query)) 
        
#     else:
#         clients = Client.objects.all().order_by('client_name','email','phone_no','suburb')
#     return render(request, 'get_clients.html', {"clients":clients})
  


    
def get_client_profile(request,id):
    prof = Client.objects.get(id=id)
    return render(request, 'client_profile.html', {"prof":prof})



def update_client(request,id):
    if request.method == 'POST':
        client_form = UpdateProfile(request.POST, instance=Client.objects.get(id=id))
        
        if client_form.is_valid():          
            client_form.save()                      
            return HttpResponseRedirect(reverse('get_client_profile',args=(id,)))
        
    else:
        client_form = UpdateProfile(instance=Client.objects.get(id=id))
    return render(request, 'update_client.html', {'client_form': client_form })
    



def get_clients(request):
    orderBy = request.GET.get('order_by')
    direction='asc'
    if request.GET.get('direction'): 
        direction = request.GET.get('direction')        
        if direction == 'desc':
            orderBy = "-" + orderBy   
            direction = 'asc'
            print(direction)
        elif direction == 'asc':
            orderBy = orderBy   
            direction = 'desc'
            print(direction)
        
    if orderBy is None:
        object_list=Client.objects.all().order_by('client_name')
        return render(request, 'get_clients.html', {"object_list":object_list})

    else:
        object_list=Client.objects.all().order_by(orderBy)
        return render(request, 'get_clients.html', {"object_list":object_list,"direction": direction})




