from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from blog.models import Post
from .forms import  SignupForm, UserFormUpdate, profileFormUpdate



def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.save()
            return redirect('login')
    form = SignupForm()
    return render(request, 'registration/signin.html',{'form':form})


@login_required(login_url='login')
def profile(request):
    # لأضافة عدد الدتوينات 
    posts = Post.objects.filter(author=request.user)
    content={
        'posts':posts,
    }
    return render(request, 'registration/profile.html', content)


def profile_update(request):
    if request.method == "POST":
        user_form = UserFormUpdate(request.POST, instance=request.user)
        profile_form = profileFormUpdate( request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid and profile_form.is_valid:
            user_form.save()
            profile_form.save()
            messages.success(request, 'تم تحديث الملف الشخصي ')
            return redirect('profile')
    else:
        user_form = UserFormUpdate(instance=request.user)
        profile_form = profileFormUpdate(instance=request.user.profile)
    context = {
        'user_form':user_form, 
        'profile_form':profile_form
    }
    return render(request, 'registration/profile_update.html', context)