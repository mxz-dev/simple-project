from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from .models import Posts
from django.utils import timezone
from mag.forms import ContactForm
from django.contrib import messages
# Create your views here.
def blog_view(request, **kwargs):
    posts = Posts.objects.filter(published_date__lt=timezone.now(), is_published=True)
    if cat := kwargs.get("category"):
        posts = posts.filter(category__name=cat)
    return render(request, "blog/blog.html", context={"posts":posts})

def post_view(request,pk):
    post = get_object_or_404(Posts, id=pk, published_date__lt=timezone.now())
    if post.is_published:
        post.views += 1
        post.save()
        published_posts = Posts.objects.filter(is_published=True,published_date__lt=timezone.now()).order_by('id')
        next_post = published_posts.filter(id__gt=post.id).first()
        prev_post = published_posts.filter(id__lt=post.id).last()

        return render(request, "blog/blog-post.html", context={"post":post,"next":next_post,"prev":prev_post})
    else:
        raise Http404("Page is Not Found")

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.cleaned_data['sender'] = "Anonymous"
            form.instance.sender = "Anonymous"
            messages.add_message(request,messages.SUCCESS,"Nice Job, Thank you")
            form.save()
        else:
            messages.add_message(request,messages.ERROR,"please check the provided data... :(")


    return render(request, "contact.html")

def about_view(request):
    return render(request,"about.html")

def home_view(request):
    return render(request, "index.html")