from django.shortcuts import render
from django.http import JsonResponse, Http404
from .models import Blog, User
import pymongo

myClient = pymongo.MongoClient("mongodb+srv://mihirsheth:Mihirshethms0906@cluster0.eof6h.mongodb.net/learn?retryWrites=true&w=majority")
db = myClient["learn"]
mycol = db["blogs"]

def blogs(request):
    '''
    View for fetching all blogs
    '''
    print(db.list_collection_names())
    
    blog_list = []
    for blog in mycol.find({},{"_id":0}):
        blog_list.append(blog)
    # try:
    #     blogs = Blog.objects.all()
    # except Exception:
    #     raise Http404

    # blog_list = []

    # for blog in blogs:
    #     blog_list.append({
    #         'id' : blog.id,
    #         'title': blog.blog_title,
    #         'slug': blog.slug,
    #         'date': blog.blog_date_created,
    #         'author': blog.user.first_name,
    #         'image_url': blog.blog_image.url,
    #         'content' : blog.blog_content,
    #         'likes' : blog.blog_likes
    #     })


    return JsonResponse({
        'blogs':blog_list,
    }, safe=False)

def get_blog(request, slug):
    '''
    View for fetching a single blog
    '''
    # try:
    blog = Blog.objects.get(slug=slug)
    # except Blog.DoesNotExist:
    #     raise Http404

    return JsonResponse({
        'blog': {
            'id' : blog.id,
            'title': blog.blog_title,
            'slug': blog.slug,
            'date': blog.blog_date_created,
            'author': blog.user.first_name,
            'image_url': blog.blog_image.url,
            'content' : blog.blog_content,
            'likes' : blog.blog_likes
        }
    })

def users(request):
    '''
    View for fetching all users
    '''

    try:
        users = User.objects.all()
    except Exception as e:
        print(e)
        raise Http404

    user_list = []

    for user in users:
        user_list.append({
            'id': user.id,
            'name' : user.first_name + user.last_name,
            'email' : user.email,
        })
    
    return JsonResponse({
        'users': user_list,
    }, safe=False)

def get_user(request, pk):
    '''
    View for fetching a single blog
    '''
    try:
        user = User.objects.get(id=pk)
    except User.DoesNotExist:
        raise Http404
    
    user_blog_list = []
    for blog in user.get_blogs.all():
        i=0
        user_blog_list.append({
            f'{i}' : {
                'id' : blog.id,
                'title': blog.blog_title,
                'slug': blog.slug,
                'date': blog.blog_date_created,
                'author': blog.user.first_name,
                'image_url': blog.blog_image.url,
                'content' : blog.blog_content,
                'likes' : blog.blog_likes
            }
        })
        i+=1

    return JsonResponse({
        'user': {
            'id': user.id,
            'first_name' : user.first_name,
            'last_name' : user.last_name,
            'email' : user.email,
            'blogs' : user_blog_list,
        }
    })
