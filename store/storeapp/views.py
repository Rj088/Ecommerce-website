
from django.shortcuts import render,HttpResponse,redirect
from storeapp.models import Product,Cart,Orders
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
import random
import razorpay
# Create your views here.

def contact(request):
    return HttpResponse("hello from our first program")



def edit(request,id):

    p=Product.objects.filter(id=id) # fetching a specific record, sql= select * from storeapp_product where id=id
    if(request.method=='GET'):
        context={}
        context['data']=p
        return render(request,'editproduct.html',context)
    else:
        uname=request.POST['pname']
        uprice=request.POST['price']
        uqty=request.POST['qty']
        # print(uname,uprice,uqty)
        # return HttpResponse('updated')
        p.update(name=uname,price=uprice,qty=uqty)
        return redirect('/Hello')
    

def delete(request,id):
    p=Product.objects.filter(id=id).delete()
    print(p)
    return redirect('/Hello')

def addproject(request):
    print(request.method)
    if request.method=="GET":
        print("if in part")
        return render(request,'addproject.html')
    else:
        print("in else part")
        product_name=request.POST['pname']
        price=request.POST['price']
        q=request.POST['qty']
        

        p=Product.objects.create(name=product_name,price=price,qty=q)
        print(p)
        p.save()

        return redirect('/Hello')
def Hello(request):
    p=Product.objects.all()
    print(p)

    context={}

    context['user']="itvedantthane"
    context['x']=3000
    context['y']=40
    context['l']=[1,2,3,4,5]
    context['d']={'id':1,'name':'machine','price':200,'qty':50}
    context['data']=[
        {'id':1,'name':'machine','price':200,'qty':50},
        {'id':2,'name':'sunny','price':55,'qty':3},
        {'id':3,'name':'raj','price':300,'qty':20}
    ]

    context['products']=p
    
    


    return render(request,'hello.html',context) 

def greet(request):
    return render(request,'base.html')

def about(request):
    return render(request,'about.html')

def index(request):
    uid=request.user.id
    print("user id",uid)
    print(request.user.is_authenticated)
    print(request.user.username)
    p=Product.objects.filter(is_active=True)
    print(p)
    context={}
    context['products']=p
   
    return render(request,'index.html',context)


def cart(request):
    return render(request,'cart.html')

def contact(request):
    return render(request,'contact.html')

def details(request,id):
    p=Product.objects.filter(id=id)
    print(p)
    context={}
    context['products']=p
   
    return render(request,'details.html',context)

def user_login(request):
    context={}
    if request.method== "GET":
        return render(request,'login.html')
    else:
         uname=request.POST['uname']
         upass=request.POST['upass']
         #print(uname)
         #print(upass)
         u=authenticate(username=uname,password=upass)
         #print(u)
         #print(u.password)
         if u is not None:
             login(request,u)
             return redirect("/index")
         else:
             
             context['errmsg']="invalid password"
             return render(request,'login.html',context)
         
def user_logout(request):
    logout(request)
    return redirect('/index')



def order(request):
    return render(request,'order.html')

def payment(request):
    return render(request,'payment.html')

def place_order(request):
    if User.is_authenticated:
        c=Cart.objects.filter(uid=request.user.id)
        oid=random.randrange(1000,9999)
        context={}
        s=0
        for x in c:
            o=Orders.objects.create(order_id=oid,uid=x.uid,pid=x.pid,qty=x.qty)
            o.save()
            x.delete()
        o=Orders.objects.filter(uid=request.user.id)
        i=len(o)
        for y in o:
            s=s+(y.qty*y.pid.price)
        context['product']=Orders.objects.filter(uid=request.user.id)
        context['total']=s
        context['items']=i
        return render(request,'placeorder.html',context)
    else:
        return redirect('/login')

def register(request):
    context={}
    if request.method=="GET":

      return render(request,'register.html')
    else:
        user=request.POST['uname']
        p=request.POST['upass']
        cp=request.POST['ucpass']

        if user=='' or p=='' or cp=='':
            context['errmsg']="fileds cannot be empty"
            return render(request,'register.html',context)
        elif p!=cp:
            context['errmsg']="password and confirm password didn't match"
            return render(request,'register.html',context)
         

        else:
            
            try:
             
            
        
             u=User.objects.create(username = user)
             u.set_password(p)
             u.save()
             context['success']="user create succefully"
             return render(request,'register.html',context)
            except Exception:
                 context['success']="user create succefully"
                 return render(request,'register.html',context)

        


def catfilter(request,cv):
    q1=Q(cat=cv)
    q2=Q(is_active=1)
    p=Product.objects.filter(q1 & q2)
    print(p)
    context={}
    context['products']=p
   
    return render(request,'index.html',context)

def pricerange(request):
    min=request.GET['min']
    max=request.GET['max']
    q1=Q(price__gte=min)
    q2=Q(price__lte=max)
    q3=Q(is_active=1)
    p=Product.objects.filter(q1 & q2 & q3)
    context={}
    context['products']=p
    return render(request,'index.html',context)

def sort(request,sv):
    if sv == '1':
        para='-price'
    else:
        para='price'

    p=Product.objects.order_by(para).filter(is_active=1)
       

    context={}
    context['products']=p
    return render(request,'index.html',context)

def addcart(request,rid):
    p=Product.objects.filter(id=rid)
    #print(p)
    u=User.objects.filter(id=request.user.id)
    print(u)
    print(u[0])
    c=Cart.objects.create(uid=u[0],pid=p[0])
    c.save()

    return HttpResponse(" product added ")

def addcart(request,rid):
    context={}
    p=Product.objects.filter(id=rid)
    u=User.objects.filter(id=request.user.id)
    if request.user.is_authenticated:
        q1=Q(pid=p[0])
        q2=Q(uid=u[0])
        res=Cart.objects.filter(q1 & q2)
        if res:
            context['dup']="product already exists in Cart!!"
            context['products']=p
            return render(request,'details.html',context)
        else:
            
            print(p,u)
            c=Cart.objects.create(uid=u[0],pid=p[0])
            c.save()
            context['products']=p
            context['success']="Product added Successfully in Cart"
            return render(request,'details.html',context)
    else:
        return redirect('/user_login')

def viewcart(request):
    context={}
    print("User ID:",request.user.id)
    if request.user.is_authenticated:
        c=Cart.objects.filter(uid=request.user.id)
        cp=len(c)
        print("count",cp)
        #print(c[0].uid)
        #print(c[0].pid)
        #print("pass",c[0].uid.password)
        s=0
        for x in c:
            s=s+(x.qty*x.pid.price)
        print("summation",s)
        context['total']=s
        context['cdata']=c
        return render(request,'cart.html',context)
    else:
        return redirect('/user_login')
    
def removecart(request,rid):
    c=Cart.objects.filter(id=rid)
    c.delete()
    return redirect('/cart')

def cartqty(request,sig,pid):
    q1=Q(uid=request.user.id)
    q2=Q(pid=pid)
    c=Cart.objects.filter(q1 & q2)
    #print(c)
    qty=c[0].qty
    if sig=='0':
        if qty>1:
         qty=qty-1
         c.update(qty=qty)
    else:
        qty=qty+1
        c.update(qty=qty)

    
    
    print("existing",qty)
    return redirect("/cart")

def makepayment(request):
    context={}
    client = razorpay.Client(auth=("rzp_test_IvVjieI9llz4x6", "mkyi8RCXFgnPWggFxPUc9jCc"))

    o=Orders.objects.filter(uid=request.user.id)
    oid=str(o[0].order_id)
    s=0
    for y in o:
        s=s+(y.qty*y.pid.price)
    #("order id",oid)
    #print("total: ",s)
    s=s*100
    data = { "amount": s, "currency": "INR", "receipt":oid }
    payment = client.order.create(data=data)
    print(payment)
    context['payment']=payment

    


    return render (request,'pay.html',context)

def send_mail(request):
    pid=request.GET['p1']
    oid=request.GET['p2']
    sign=request.GET['p3']

    print("PAYMENT ID: ",pid)
    print("order ID",oid)
    print("sign:",sign)
    return HttpResponse("email send")
    




    
    
    
