from django.shortcuts import render, HttpResponse

# Create your views here.

def post_list(request):
    #return HttpResponse('page1')
    return render(request, 'blog/post_list.html', {})
