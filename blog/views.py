from django.shortcuts import render


posts=[
    {
        'author':'Sachin',
        'title':'Blog Post 1',
        'content':'First Content',
        'date_posted':'25 jan ,2020',
    },
    {
        'author':'Test',
        'title':'Blog Post 2',
        'content':'Second Content',
        'date_posted':'24 jan ,2020',
    },
]

# Create your views here.

def home(request):
    # return HttpResponse("<h1>HELLO</h1>")
    context={
        'posts':posts
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':"about"})
