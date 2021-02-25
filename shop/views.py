from django.shortcuts import render
from django.http import HttpResponse
from .models import Product ,Contact,Orders ,OrderUpdate
from math import ceil
import json
from django.views.decorators.csrf import csrf_exempt 
from shop.paytm import checksum
MERCHANT_KEY = 'i%O8#ZVI#LqjaZjq'
# Create your views here.
def home(request):
    #products=Product.objects.all()
    #print(products)
    #n=len(products)
    #nSlides=n//4 + ceil((n/4)-(n//4))
    allProds=[]
    catprods=Product.objects.values('category','id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n=len(prod)
        nSlides=n//4 + ceil((n/4)-(n//4))
        allProds.append([prod ,range(1,nSlides) ,nSlides])
    #params={'no_of_slides': nSlides ,'range' : range(1,nSlides) ,'product': products}
    #allProds=[[products ,range(1,nSlides) ,nSlides] ,
    #          [products ,range(1,nSlides) ,nSlides]]
    params={'allProds': allProds}          
    return render(request,'shop/index.html',params)


def about(request):
    return render(request,'shop/about.html')


def contact(request):
    thank=False
    if request.method=="POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('desc','')
        #print(name,email,phone,desc)
        contact=Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
        thank=True
        return render(request,'shop/contact.html',{'thank':thank})
    return render(request,'shop/contact.html')


def search(request):
    return render(request,'shop/search.html')   


def productView(request ,myid):
    # fetch the product using id
    product=Product.objects.filter(id=myid)
    return render(request,'shop/product.html',{'product': product[0]})


def tracker(request):
    if request.method=="POST":
        orderid=request.POST.get('orderid','')
        email=request.POST.get('email','')
        #return HttpResponse(f"{orderid} and {email}")
        try:
            order=Orders.objects.filter(order_id=orderid ,email=email)
            if len(order)>0:
                update=OrderUpdate.objects.filter(order_id=orderid)
                updates=[]
                for item in update:
                    updates.append({'text':item.update_desc ,'time':item.timestamp})
                    response=json.dumps([updates ,order[0].order_json] ,default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')    
        
            
    return render(request,'shop/tracker.html')


def checkout(request):
    if request.method=="POST":
        order_json=request.POST.get('itemsJson','')
        name=request.POST.get('name','')
        amount=request.POST.get('amount','')
        email=request.POST.get('email','')
        address=request.POST.get('address1','') + " " + request.POST.get('address2','')
        city=request.POST.get('city','')
        state=request.POST.get('state','')
        zip_code=request.POST.get('zip_code','')
        phone=request.POST.get('phone','')
        #print(name,email,phone,desc)
        print(amount)
        order=Orders(order_json=order_json ,name=name,email=email ,address=address ,city=city ,state=state ,zip_code=zip_code ,phone=phone ,amount=amount)
        order.save()
        update=OrderUpdate(order_id=order.order_id ,update_desc="The order has been placed")
        update.save()
        thank=True
        id=order.order_id
        #return render(request,'shop/checkout.html',{'thank':thank,'id':id})
        # request paytm to transfer the amount to your account payment by user
        param_dict={
            'MID':'OuNTMn30623681544705',
            'ORDER_ID':str(order.order_id),
            'TXN_AMOUNT':str(amount),
            'CUST_ID':'email',
            'INDUSTRY_TYPE_ID':'Retail',
            'WEBSITE':'WEBSTAGING',
            'CHANNEL_ID':'WEB',
	        'CALLBACK_URL':'http://127.0.0.1:8000/shop/handlerequest/',
        }
        param_dict['CHECKSUMHASH']=checksum.generate_checksum(param_dict ,MERCHANT_KEY)
        return render(request,'shop/paytm.html' ,{'param_dict':param_dict})  

    return render(request,'shop/checkout.html')   

@csrf_exempt
def handlerequest(request):
    # paytm will send you post request here
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum1 = form[i]

    verify = checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum1)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
    return render(request, 'shop/paymentstatus.html', {'response': response_dict})

