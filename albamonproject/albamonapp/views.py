from django.core.handlers.wsgi import get_bytes_from_wsgi
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Store, Comment

# Create your views here.

def home(request):
    stores = Store.objects.all()
    context = {
        'stores':stores
    }
    return render(request, 'home.html', context)

def detail(request, id):
    detail_data = get_object_or_404(Store, pk=id)
    comments = Comment.objects.filter(store_id=id)
    context = {
        'title' : detail_data.title,
        'local' : detail_data.local,
        'enpl_area' : detail_data.enpl_area,
        'salary' : detail_data.salary,
        'todo' : detail_data.todo,
        'appl_num' : detail_data.appl_num,
        'detail' : detail_data.detail,
        'id' : id,
        'comments' : comments,
        'image' : detail_data.image,
    }
    return render(request, 'detail.html', context)

def create_page(request):
    return render(request, 'create.html')

def create(request):
    new_data = Store()
    new_data.title = request.POST['title']
    new_data.local = request.POST['local']
    new_data.detail = request.POST['detail']
    new_data.enpl_area = request.POST['enpl_area']
    new_data.salary = request.POST['salary']
    new_data.todo = request.POST['todo']
    new_data.image = request.FILES['image']
    new_data.save()
    return redirect('home')

def update_page(request, id):
    update_data = get_object_or_404(Store, pk=id)
    context = {
        'title' : update_data.title,
        'local' : update_data.local,
        'enpl_area' : update_data.enpl_area,
        'salary' : update_data.salary,
        'todo' : update_data.todo,
        'appl_num' : update_data.appl_num,
        'detail' : update_data.detail,
        'id' : id,
        'image' : update_data.image,
    }
    return render(request, 'update.html', context)

def update(request, id):
    update_data = get_object_or_404(Store, pk=id)
    update_data.title = request.POST['title']
    update_data.local = request.POST['local']
    update_data.detail = request.POST['detail']
    update_data.enpl_area = request.POST['enpl_area']
    update_data.salary = request.POST['salary']
    update_data.todo = request.POST['todo']
    update_data.image = request.FILES['image']
    update_data.save()
    return redirect('home')

def delete(request, id):
    delete_data = get_object_or_404(Store, pk=id)
    delete_data.delete()
    return redirect('home')

def apply(request, id):
    apply_data = get_object_or_404(Store, pk=id)
    apply_data.cnt()
    return redirect('detail', id)

def cancel(request, id):
    apply_data = get_object_or_404(Store, pk=id)
    apply_data.dcnt()
    return redirect('detail', id)

def create_comment(request, id):
    new_comment = Comment()
    store_id = Store.objects.get(pk=id)
    new_comment.store_id = store_id
    new_comment.user = request.POST['user']
    new_comment.content = request.POST['content']
    new_comment.pub_date = timezone.now()
    new_comment.save()

    return redirect('detail', id)

def delete_comment(request, id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()

    return redirect('detail', id)