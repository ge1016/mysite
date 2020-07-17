from django.shortcuts import render,get_object_or_404
from django.contrib.contenttypes.models import ContentType
from .models import Blog,BlogType
from comment.models import Comment
from comment.forms import CommentForm

def blog_list(request):
    context = {}
    context['blogs'] = Blog.objects.all()
    context['blog_types'] = BlogType.objects.all()
    return render(request,'blog_list.html',context)

def blogs_with_type(request,blog_type_pk):
    context = {}
    blog_type = get_object_or_404(BlogType,pk=blog_type_pk  )
    context['blogs'] = Blog.objects.filter(blog_type=blog_type)
    context['blog_type'] = blog_type
    context['blog_types'] = BlogType.objects.all()
    return render(request,'blogs_with_type.html',context)

def blog_detail(request,blog_pk):
    blog = get_object_or_404(Blog,pk=blog_pk)
    blog_content_type = ContentType.objects.get_for_model(blog)
    comments = Comment.objects.filter(content_type=blog_content_type,object_id=blog.pk,parent=None)

    context = {}
    context['blog'] = get_object_or_404(Blog,pk=blog_pk)
    context['user'] = request.user
    context['comments'] = comments.order_by('-comment_time')
    context['comment_form'] = CommentForm(initial = {'content_type':blog_content_type.model,'object_id':blog_pk,'reply_comment_id':0})
    return render(request,'blog_detail.html',context)


