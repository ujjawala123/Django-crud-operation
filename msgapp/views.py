from django.shortcuts import render,HttpResponse,redirect
from django.views import View
from msgapp.models import Message

# 1) Function Base  views here.
def about(request):
    return HttpResponse("This is from About Page")


# 2) Class Base Views  --pascal datatype
# derived from view class
#Types of vies =classbase,functionbase

class ContactForm(View):
    def get(self,request,eid):
        #return HttpResponse("This is from Class Base view")
        return HttpResponse("Emplyoee id is:"+eid)
    
#render fun:parameters= request,html file with exe,dict------using for website html pages 
def hello(request):
    return render(request,'hello.html')

def hello (request):
    #x='Itvedant'
    d={}
    d['x']='Itvedant'
    d['y']='cghnb'
    d['z']='It'
    d['a']=10
    d['b']=20
    d['c']=30
    lst=[{'id':1, 'name':'hardik', 'city':'pune',},{'id':2, 'name':'ujjawala', 'city':'pune',},{'id':3, 'name':'pooja', 'city':'pune',}]
    d['data']=lst


    return render(request,'hello.html',d)
def main(request):
    return render(request,'main.html')
def product(request):
    return render(request,'product.html')
def cart(request):
    return render(request,'cart.html')
def form(request):
    if request.method== 'GET':
        return render(request,'form.html')
    else:
        n=request.POST['name']
        e=request.POST['email']
        mob=request.POST['mob']
        msg=request.POST['msg']
        # print(n) check for get method
        # print(n,e,m,msg)
        m=Message.objects.create(name=n,email=e,mob=mob,msg=msg)
        # return HttpResponse("Data Fetched")
        return render(request,'display.html')

def display(request):
    m=Message.objects.all()
    context={}
    context['data']=m
    # print(m)
    # return HttpResponse("Data fetched from database")
    return render(request,'display.html',context)

def delete(request,eid):
    m=Message.objects.filter(id=eid)
    # print(m)
    m.delete()
    # return HttpResponse("Emplyoee id is:"+eid)
    return redirect('/display')

def edit(request,eid):
  
    if request.method== 'GET': #check if the method is get
        m=Message.objects.filter(id=eid)  # filter recordes     
        context={}
        context['data']=m
        return render(request,'edit.html',context)
   
    else:
        n=request.POST['name']
        e=request.POST['email']
        mob=request.POST['mob']
        msg=request.POST['msg']
            # print(n,e,mob,msg)
        m=Message.objects.filter(id=eid) 
        m.update(name=n,email=e,mob=mob,msg=msg) 
        return redirect('/display')