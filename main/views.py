from django.shortcuts import render
from django.contrib import messages 
from .forms import ArticleForm, ImportForm, PackingListForm, ExportForm
from main.models import Article, Import, PackingList, Export
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect



def index(request):
    return render(request, 'main/home.html')

def article(request):
    if request.method == 'POST':
        article = ArticleForm(data=request.POST)
        if article.is_valid():
            article.save()
        else:
            messages.error(request, "Error")


    article_object = Article.objects.all().order_by('fabric')

    context = {"article_object": article_object}    

    return render(request, 'main/article.html', context)    


def import_view(request):
    context = {}
    packing_list_form = PackingListForm
    import_form = ImportForm
    import_object = Import.objects.all().order_by('packing_list', 'article__fabric')
    packing_list_object = PackingList.objects.all().order_by('name')
    article_object = Article.objects.all().order_by('fabric')


    if request.method == 'GET':
        GET = request.GET
        if 'packing_list' in GET.keys():
            if GET['packing_list'] != '':
                import_object = import_object.filter(packing_list__id=int(GET['packing_list']))
                context['import_form'] = import_form
                context['packing_list_id'] = GET['packing_list']
    if request.method == 'POST':
        POST = request.POST
        if "date" in POST.keys():
            packing_list_form = packing_list_form(POST)
            if packing_list_form.is_valid():
                packing_list_form.save()
        import_form = import_form(POST)
        if import_form.is_valid():
            packing_list_obj=get_object_or_404(PackingList, id=POST['add_packing_list'])
            import_form.instance.packing_list = packing_list_obj
            context["import_packing_list_id"] = POST["add_packing_list"]
            import_form.save()
            params = "packing_list=%s" %(POST["add_packing_list"])
            return HttpResponseRedirect('/imports/' + "?%s" % params)

        
    context['article_object'] = article_object    
    context['import_object'] = import_object
    context['packing_list_object'] = packing_list_object
    context['packing_list_form'] = packing_list_form
    return render(request, 'main/import.html', context)


def delete_article(request):
    Article.objects.filter(id=request.POST['article_id']).delete()
    article_object = Article.objects.all()
    return render(request,'main/list_article.html',{'article_object':article_object})

def delete_imports(request):
    Import.objects.filter(id=request.POST['import_id']).delete()
    if "packing_list" in request.POST.keys():
        print(request.POST)
        import_object = Import.objects.filter(packing_list=int(request.POST['packing_list']))
    else:        
        import_object = Import.objects.all()
    return render(request,'main/list_imports.html',{'import_object':import_object})



def export_view(request):
    context = {}
    export_form = ExportForm
    packing_list_form = PackingListForm
    export_object = Export.objects.all().order_by('packing_list', 'article__fabric')
    packing_list_object = PackingList.objects.all().order_by('name')
    article_object = Article.objects.all().order_by('fabric')

    if request.method == 'GET':
        GET = request.GET
        if 'packing_list' in GET.keys():
            if GET['packing_list'] != '':
                export_object = export_object.filter(packing_list__id=int(GET['packing_list']))
                context['export_form'] = export_form
                context['packing_list_id'] = GET['packing_list']
    if request.method == 'POST':
        POST = request.POST    
        if "date" in POST.keys():
            packing_list_form = packing_list_form(POST)
            if packing_list_form.is_valid():
                packing_list_form.save()
        export_form = export_form(POST)
        if export_form.is_valid():
            packing_list_obj=get_object_or_404(PackingList, id=POST['add_packing_list'])
            export_form.instance.packing_list = packing_list_obj
            context["export_packing_list_id"] = POST["add_packing_list"]
            export_form.save()
            params = "packing_list=%s" %(POST["add_packing_list"])
            return HttpResponseRedirect('/exports/' + "?%s" % params)


    context['article_object'] = article_object
    context['export_object'] = export_object
    context['packing_list_object'] = packing_list_object
    context['packing_list_form'] = packing_list_form
    return render(request, 'main/export.html', context)
