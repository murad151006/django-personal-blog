from django.shortcuts import render, redirect
from .models import Blog, BlogComment
from django.contrib import messages
from blog.templatetags import extras
# Create your views here.
def Home(request):
    allPosts = Blog.objects.all()
    context = {'allPosts': allPosts}
    return render(request, 'blog/blogHome.htm', context)

#when we click read more, then this function opens the blogpost.html

def Post(request, slug):
    #first variable takes filter method which filter the bolgs by their slug by clicking on read more
    posts = Blog.objects.filter(slug=slug).first()

    #comment for filterout with realted blog's commnet
    comment = BlogComment.objects.filter(post=posts, parent=None)

    #replies for filterout with realted blog's replies,
    replies = BlogComment.objects.filter(post=posts).exclude(parent=None)

    #make all replied into a dictionary
    replyDict = {}

    #for every reply, if replydict doesn't contain the serial number  of a reply then assume the reply as that no, otherwise append new
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)

    print(request.user)
    context = {'posts': posts, 'comments':comment, 'user':request.user, 'replyDict': replyDict}
    return render(request, 'blog/blogPost.htm', context)

def postComment(request):
    if request.method == "POST":
        comment = request.POST.get("comment")
        user = request.user
        postSno = request.POST.get("postSno")
        post = Blog.objects.get(slno=postSno)
        parentSno = request.POST.get("parentSno")
        
        #if only we have parent means comment, only then we have reply, if parent is not available, add as comment otherwise make reply
        if parentSno == "":
            com = BlogComment(comment=comment, user=user, post=post)
            com.save()
            messages.success(request, "Your comment has been commented")
        else:
            parent = BlogComment.objects.get(sno=parentSno)
            com = BlogComment(comment=comment, user=user, post=post, parent = parent )
            com.save()
            messages.success(request, "Your reply has been commented")
    return redirect(f"/blog/{post.slug}")