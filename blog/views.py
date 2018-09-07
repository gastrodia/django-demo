from django.shortcuts import render
#from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import Post
import datetime
 
 
def index(request):
    if request.method == 'POST':
        # save new post
        title = request.POST['title']
        content = request.POST['content']
 
        post = Post(title=title)
        post.last_update = datetime.datetime.now()
        post.content = content
        post.save()
 
    # Get all posts from DB
    posts = Post.objects
    return render(request ,'MyApplication/index.html', {'Posts': posts})
 
 
def update(request):
    id = eval("request." + request.method + "['id']")
    post = Post.objects(id=id)[0]
 
    if request.method == 'POST':
        # update field values and save to mongo
        post.title = request.POST['title']
        post.last_update = datetime.datetime.now()
        post.content = request.POST['content']
        post.save()
        template = 'index.html'
        params = {'Posts': Post.objects}
 
    elif request.method == 'GET':
        template = 'MyApplication/update.html'
        params = {'post': post}
 
    return render(request , template, params)
 
 
def delete(request):
    id = eval("request." + request.method + "['id']")
 
    if request.method == 'POST':
        post = Post.objects(id=id)[0]
        post.delete()
        template = 'index.html'
        params = {'Posts': Post.objects}
    elif request.method == 'GET':
        template = 'MyApplication/delete.html'
        params = {'id': id}
 
    return render(request ,template, params)
 
 
