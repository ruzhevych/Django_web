from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request, "home.html")

def contactpage(request):
    return render(request, "contacts.html")
    # return HttpResponse("Контакти 📞")

# def newspage(request):
#     news = [
#         {"title": "Енергетична ситуація в Україні", "content": "У зв'язку з продовженням атак на енергосистему країни, графіки погодинних відключень електроенергії діють у всіх регіонах."},
#         {"title": "Розробка нового озброєння", "content": "Український дрон-ракета під назвою 'Паляниця' вийшов у серійне виробництво, що стане важливим кроком у зміцненні обороноздатності країни."},
#         {"title": "Евакуація в Костянтинівці", "content": "Російські війська завдали удару по Костянтинівці, внаслідок чого є постраждалі. На місці працюють рятувальники та медики."},
#     ]
#     return render(request, 'news.html', {'news': news})

