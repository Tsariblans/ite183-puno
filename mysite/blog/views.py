from django.shortcuts import render
from .models import Post
from django.http import HttpResponseRedirect
from .forms import PostForm
# Create your views here.

def blog_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/posts')
    context = {
        "form": form,
        "form_type":'Create'
    }    
    return render (request, "blog/blog_create.html", context)

# Suggested code may be subject to a license. Learn more: ~LicenseLog:2092949153.
def blog_update(request, id):
    post = Post.objects.get(id = id)
# Suggested code may be subject to a license. Learn more: ~LicenseLog:1848471879.
    form = PostForm(request.POST or None, instance = post)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/posts')
    context ={
        "form":form,
        "form_type":'Update'
    }
    return render(request, "blog/blog_create.html", context)



def blog_list(request):
   post = Post.objects.all()
   context = {

       'blog_list':post
   }
   return render(request, "blog/blog_list.html",context)

def blog_detail(request, id):
    debug_tool = Post.objects.get(id = id)
    context = {

        'blog_detail':debug_tool
    }
    return render( request, "blog/blog_detail.html",context)

def blog_delete(request,id):
    each_post = Post.objects.get(id =id)
    each_post.delete()
    return HttpResponseRedirect('/posts/')

# Create your views here.
