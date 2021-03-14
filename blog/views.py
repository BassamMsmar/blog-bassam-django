from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import  NewComment, PostCreateForm
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin




# Create your views here.

def home(request):
    posts = Post.objects.all()
    context ={
        'title':'الصفحة الرئيسية',
        'posts': posts
        }
    return render(request, 'blog/index.html', context)

def about_us(request):
   
    return render(request, 'blog/about-us.html')
 





def post_detail(request, post_id):
    
    post = get_object_or_404(Post, pk=post_id)
    comments = post.comments.filter(active=True)
    
    if request.method == 'POST':
        comment_form = NewComment(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return redirect('detail', post_id)
    else:
        comment_form = NewComment()
        

    comment_form = NewComment()
    context ={
        'title': post,
        'post': post,
        'comments': comments,
        'comment_form': comment_form
    }
    
    return render(request, 'blog/detail.html', context)




def edit_post(request):
    
    if request.method == 'POST':
        form_edit_post = Post(request.post, instance=request.user)

        if form_edit_post.is_valid:
            form_edit_post.save()
            return redirect('profile')
    else:
             form_edit_post = Post(request.post, instance=request.user)

    return render(request, 'blog/detail.html', {'form_edit_post':form_edit_post})






class PostCreateView(LoginRequiredMixin,  CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/new_posts.html'
    # from_class = PostCreateForm
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/new_posts.html'
    # from_class = PostCreateForm()
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False




class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'


    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

    


