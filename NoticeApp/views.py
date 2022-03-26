from django.shortcuts import render, get_object_or_404, redirect 

# Create your views here.
from django.views.generic.base import TemplateView
from .models import Post,Comment
from  .forms import CommentForm
from django.views.generic import ListView
from django.http import JsonResponse
import json

class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = Post.objects.all() 
        return context
def json(request):
      data = list(Post.objects.values())
      return JsonResponse(data, safe=False)
      


def comment(request, postid):
     post_q = get_object_or_404(Post,id=postid)
     

     if request.method=="POST":
            form = CommentForm(request.POST)

            if form.is_valid():
                obj = form.save(commit=False)
                obj.post = post_q
                obj.save()
                return redirect('home')
    
            # content = request.POST.get('message')
            # print(content)
            # coment = Comment(body=content)
            # coment.save()
                 
     else:
         form = CommentForm()
     context={
         'single': post_q,
         'form': form
        }

     return render(request,"singledata/singledata.html",context)

    # comment = Post_Comment.objects.create(post_title=post, comment=request.POST['comment'])

    # return HttpResponseRedirect('home/home.html')



def blog(request):
    data = list(Comment.objects.values())
    return JsonResponse(data, safe=False)