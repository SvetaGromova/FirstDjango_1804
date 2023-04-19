from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


author = {
       "name" : "Иван",
       "middle": "Петрович",
       "surname": "Иванов",
       "phone": "8-923-600-01-02",
       "email": "vasya@mail.ru"
}


items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 7, "name": "Картофель фри" ,"quantity":0},
   {"id": 8, "name": "Кепка" ,"quantity":124},
]


# Create your views here.
def home(request):

    context = {
        "name": 'Петров Николай Иванович',
        "email": "my_mail@mail.ru"

    }
    return render(request, "index.html", context)

def about(request):
    result = f"""
       Имя: <b>{author["name"]}</b><br>
       Отчество: <b>{author["middle"]}</b><br>
       Фамилия: <b>{author["surname"]}</b><br>
       телефон: <b>{author["phone"]}</b><br>
       email: <b>{author["email"]}</b><br>
       <a href='/'> Home </a>
       """

    return HttpResponse(result)


def get_item(request, id):
    for item in items:
        if item['id'] == id:
#             result = f"""
#             <h1>Имя: {item["name"]} </h1>
#             <p>Количество: {item['quantity']} </p>
#             <a href='/items'> Назад </a>
# """
#             return HttpResponse(result)
          context = {
              'item': item
    }
    return render(request, "item-page.html", context)


def list_items(request):
    # result = "<h2>список товаров</h2><ol>"
    # for item in items:
    #     result += f"<li><a href='/item/{item['id']}'>{item['name']}</a></li>"
    # result += '</ol>'
    # return HttpResponse(result)
    context = {
        "items": items

    }
    
    return render(request, "item-list.html", context)