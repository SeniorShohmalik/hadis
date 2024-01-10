from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import H_Kitoblar ,H_Qismlar ,Q_Parchalar ,V_Hadislar
from django.db.models import Q
from django.core.paginator import Paginator

def home(request):
    kitob_arab = H_Kitoblar.objects.all()

    soni = V_Hadislar.objects.count()


    content = {'kitoblar':kitob_arab ,'soni':soni}

    return render(request ,'part/index.html',content)



def chapter(request , book_name):

    the_book = H_Kitoblar.objects.get(lotin = book_name)

    chapters = H_Qismlar.objects.all().filter(kitobdan = the_book)

    content = {'chapters':chapters ,'the_book':the_book}

    return render(request ,'part/navbar.html',content)



def khadis(request , khadis):

    the_chapter = H_Qismlar.objects.get(lotin = khadis) #chapter of the book

    parts = Q_Parchalar.objects.all().filter(qismdan = the_chapter)  #some parts

    xadislar = []

    for part in parts:

        xadis = V_Hadislar.objects.filter(parchadan = part)
        
        xadislar.append(xadis)

    
    


    content = {'xadislar':xadislar ,'parts':parts ,'the_chapter':the_chapter}
    return render(request ,'part/script.html',content)

def search(request):
    print(request.user)
    context = {}
    if request.method =='POST':
        keyword = str(request.POST.get('savol'))
        b = str(request.POST.get('submit'))
        print(keyword,b)
        if keyword:
            books = V_Hadislar.objects.filter(Q(lotin__icontains=keyword) | Q(toifa__icontains=keyword) | Q(tomonidan__icontains=keyword))
            number = len(books)
            context = {'keyword':keyword,'number':number ,'books':books}
            return render(request ,'part/searchbar.html',context)

        elif b:
            books = V_Hadislar.objects.filter(Q(lotin__icontains=keyword) | Q(toifa__icontains=keyword) | Q(tomonidan__icontains=keyword))
            number = len(books)
            context = {'keyword':b,'number':number ,'books':books}
            return render(request ,'part/searchbar.html',context)

    else:

    
        return render(request ,'part/searchbar.html')


                                                    

                                                

                                            