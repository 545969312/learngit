from django.shortcuts import render, HttpResponse, redirect
from .models import Book, Publish, Author, AuthorDetail, User, Upload
from django.db.models import Avg,Max,Min,Count
from datetime import datetime
import os

# Create your views here.


def base(request):
    is_login = request.session.get('is_login')
    username = request.session.get('username')
    login_time = request.session.get('login_time')
    return render(request, 'base.html', locals())


def login(request):
    if request.method == "POST":
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        if User.objects.filter(user=user, pwd=pwd):
            request.session['is_login'] = True
            request.session['username'] = user
            request.session['login_time'] = datetime.now().strftime("%Y-%m-%d %X")
            return redirect('/base/')

    return render(request, 'login.html')


def logout(request):

    request.session.flush()
    return redirect('/login/')


def query_book(request):
    is_login = request.session.get('is_login')
    if not is_login:
        return redirect('/login/')

    book_list = Book.objects.all()

    return render(request, 'query_book.html', {'book_list':book_list})


def add_book(request):
    is_login = request.session.get('is_login')
    if not is_login:
        return redirect('/login/')

    if request.method == "POST":
        title = request.POST.get('title')
        price = request.POST.get('price')
        pub_date = request.POST.get('pub_date')
        publish_id = request.POST.get('publish')
        author_list = request.POST.getlist('author_list')

        book_obj = Book.objects.create(title=title,price=price,pub_date=pub_date,publish_id=publish_id)
        book_obj.authors.add(*author_list)

        return redirect('http://127.0.0.1:8000/query_book/')

    pub_obj = Publish.objects.all().values()
    aut_obj = Author.objects.all().values()
    return render(request, 'add_book.html', {'pub_obj':pub_obj, 'aut_obj':aut_obj})


def del_book(request, dele):

    book_obj = Book.objects.filter(id=dele).delete()

    return HttpResponse('删除成功')


def change_book(request, change_id):

    book_obj = Book.objects.filter(id=change_id).first()
    pub_obj = Publish.objects.all()
    aut_obj = Author.objects.all()

    if request.method == "POST":

        title = request.POST.get('title')
        price = request.POST.get('price')
        pub_date = request.POST.get('pub_date')
        publish_id = request.POST.get('publish')
        author_list = request.POST.getlist('author_list')

        book_obj = Book.objects.filter(id=change_id)
        book_obj.update(title=title, price=price, pub_date=pub_date, publish_id=publish_id)
        book_obj.first().authors.clear()
        book_obj.first().authors.add(*author_list)

        return redirect('query_book')

    return render(request, 'change_book.html',locals())


def upload(request):
    is_login = request.session.get('is_login')
    if not is_login:
        return redirect('/login/')

    if request.method == "POST":
        file_obj = request.FILES.get('upload_file')
        file_name = Upload.objects.create(file_name=file_obj.name)

        with open('static/images/'+file_obj.name, 'wb') as f:
            for line in file_obj:
                f.write(line)
        return redirect('/upload/')
    file_all = Upload.objects.all()
    return render(request, 'upload.html', locals())