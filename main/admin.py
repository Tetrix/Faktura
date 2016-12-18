from django.contrib import admin
from main.models import Article, Import, PackingList, Export


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id','fabric','color', 'supplier'] 

class PackingListAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','date'] 

class ImportAdmin(admin.ModelAdmin):
    def fabric(self,obj):
        return obj.article.fabric
    def color(self,obj):
        return obj.article.color
    def supplier(self,obj):
        return obj.article.supplier


    list_display = ['id', 'fabric', 'color', 'supplier','quantity','comment', 'packing_list'] 
    list_filter = ('packing_list',)
    search_fields = ['packing_list__name']

    def get_queryset(self, request):
        query_set = super(ImportAdmin, self).get_queryset(request)
        return query_set.order_by('packing_list', 'article__fabric')



class ExportAdmin(admin.ModelAdmin):
    def fabric(self,obj):
        return obj.article.fabric
    def color(self,obj):
        return obj.article.color
    def supplier(self,obj):
        return obj.article.supplier

    list_display = ['id', 'fabric', 'color', 'supplier','order','art','use','comment'] 
    search_fields = ['packing_list__name']

    def get_queryset(self, request):
        query_set = super(ExportAdmin, self).get_queryset(request)
        return query_set.order_by('packing_list', 'article__fabric')


admin.site.register(Article, TaskAdmin)
admin.site.register(Import, ImportAdmin)
admin.site.register(PackingList,PackingListAdmin)
admin.site.register(Export,ExportAdmin)