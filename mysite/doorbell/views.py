from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from twitter.models import User
from django.db import IntegrityError
from .models import UserProfile, Borough, Post, Group

# Create your views here.

def load_signup_page(request):
    context={'boroughs': Borough.objects.all()}
    print(context)
    return render(request, 'doorbell/login.html', context=context)


def signin(request):
    username = request.POST['username']
    password = request.POST['password']
    print(f'{username} / {password}: Trying to signin')
    user = authenticate(request, username= username, password=password)
    if not user:
        return redirect('doorbell:login')
    else:
        login(request, user)

        return redirect('doorbell:home')


def logout_view(request):
    logout(request)
    return redirect('doorbell:login')

def create_user(request):
    print(request.POST)
    username = request.POST['username']
    passw = request.POST['password']
    borough = request.POST['borough']
    print(username, passw, borough)
    try:
        user = User.objects.create_user(username=username, password=passw)
        userprofile = UserProfile(user=user, borough=Borough.objects.get(bname=borough))
        userprofile.save()

        userprofile.groups.add(Group.objects.get(group='News'))
        userprofile.groups.add(Group.objects.get(group='Traffic'))
        userprofile.groups.add(Group.objects.get(group='Politics'))

    except IntegrityError:
        print('THIS USERNAME AND PASSWORD ALREADY EXITS, PICK SOMETHING ELSE.')
        # TODO: send error back to user.
        return redirect('doorbell:login')
    except:
        print(f'user: {user.username}, borough:{borough.bname}')
        print('Problem with UserProfileCreation')
        return redirect('doorbell:login')

    if user:
        login(request, user)

        return redirect('doorbell:home')
    

    return redirect('doorbell:login')


def joingroup(request, group_name):
    userprofile = UserProfile.objects.get(user=request.user)
    group = Group.objects.get(group=group_name)
    userprofile.groups.add(group)

    return redirect(request.META['HTTP_REFERER']) 

    


def index(request):
    
    userprofile = UserProfile.objects.get(user=request.user)
    return render(request, 'doorbell/home.html', {'userprofile': userprofile, 'groups':Group.objects.all()})

def loadboroughpage(request):
    return render(request, 'doorbell/borough.html')

def post(request, group_name):
    text = request.POST['post']
    user = request.user
    print(group_name)
    userp = UserProfile.objects.get(user=request.user) 
    group = Group.objects.get(group=group_name)
    post = Post(post_text=text, borough=userp.borough, group=group, author=user)
    post.save()

    return redirect(request.META['HTTP_REFERER']) 

def group(request, group_name):
    print('On Group page')
    group_obj = Group.objects.get(group=group_name)
    borough = UserProfile.objects.get(user=request.user).borough

    posts = Post.objects.filter(group=group_obj, borough=borough)
    print(f'Posts: {posts}')

    userprofile = UserProfile.objects.get(user=request.user)

    return render(request, 'doorbell/grouppage.html', {'group':group_obj , 'posts':posts, 'userprofile':userprofile})



def add_to_group(request, group_id):
    return render(request, 'doorbell/add.html')

def search_posts(request):
    search_text =request.GET['search_post']
    po = Post.objects.filter(post_text__icontains=search_text)

    return render(request, 'doorbell/search_posts.html', {'search_term':search_text, 'post':po, 'groups':Group.objects.all()})

def unlike(request, post_id):
    po = Post.objects.get(id = post_id)
    po.likers.remove(request.user)
    return redirect(request.META['HTTP_REFERER'])

def like(request, post_id):
    po = Post.objects.get(id = post_id)
    po.likers.add(request.user)
    return redirect(request.META['HTTP_REFERER'])

def delete(request, post_id):
    po = Post.objects.get(id = post_id)
    po.delete()
    return redirect(request.META['HTTP_REFERER'])

def polls(request):
    return render(request, 'doorbell/poll.html')

def join(request):
    userprofile = UserProfile.objects.get(user=request.user)
    return render(request, 'doorbell/join.html', {'userprofile': userprofile, 'groups':Group.objects.all()})



