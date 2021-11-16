from django.shortcuts import render, HttpResponse, Http404
from MainApp.models import Item
from django.core.exceptions import ObjectDoesNotExist

# items = [
#    {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
#    {"id": 2, "name": "Куртка кожаная", "quantity": 2},
#    {"id": 3, "name": "Coca-cola 1 литр", "quantity": 12},
#    {"id": 4, "name": "Картофель фри", "quantity": 0},
#    {"id": 5, "name": "Кепка", "quantity": 124},
# ]


user = {
    "name": "Андрей",
    "last_name": "Литовкин",
    "middlename": "Александрович",
    "phone": "+7-900-800-11-22",
    "email": "litrovkin@mail.ru",
}


def home(request):
    # context = {
    #     "name": "Андрей",
    #     "surname": "Литовкин"
    # }
    context = {
        "page_title": 'Наименование товара',
        "user": user
    }
    return render(request, 'index.html', context)


def about(request):
    result = f"""
        Имя: <b>{user['name']}</b><br>
        Отчество: {user['middlename']}<br>
        Фамилия: Иванов<br>
        телефон: {user['phone']}<br>
        email: vasya@mail.ru<br>
    """
    return HttpResponse(result)


def get_item(request, id):
    # for item in items:
    #     if item["id"] == id:
    #         context = {
    #             "item" : item
    #         }
    #         # return HttpResponse(f"<h2>{item['name']}</h2><a href='/items'>back</a>")
    #         return render(request, 'item.html', context)
    # raise Http404
    # item = items[id-1].id
    try:
        item = Item.objects.get(id=id)
    except ObjectDoesNotExist:
        raise Http404
    context = {
        "page_title": 'Наименование товара',
        "item": item
    }
    return render(request, 'item.html', context)


def items_list(request):
    # result = "<ol>"
    # for item in items:
    #     result += f"<li><a href='/item/{item['id']}'>{item['name']}</a></li>"
    # result += "</ol>"
    # return HttpResponse(result)

    items = Item.objects.all()
    context = {
        "page_title": 'Список товаров',
        "items": items
    }
    return render(request, 'items_list.html', context)
