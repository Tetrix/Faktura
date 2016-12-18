from django.db import models



class Article(models.Model):
    fabric = models.IntegerField()
    color = models.CharField(max_length = 10)
    supplier = models.CharField(max_length = 50)

    def __str__(self):
        return "fabric: %s  color: %s  supplier: %s" %(self.fabric,self.color,self.supplier)


class PackingList(models.Model):
    name = models.CharField(max_length = 50, unique=True)
    date = models.DateField()

    def __str__(self):
        return self.name

class Import(models.Model):
    packing_list = models.ForeignKey(PackingList)
    article = models.ForeignKey(Article)
    quantity = models.IntegerField()
    comment = models.CharField(max_length = 200)

    def __str__(self):
        return str(self.id)

class Export(models.Model):
    packing_list = models.ForeignKey(PackingList)
    article = models.ForeignKey(Article)
    order = models.CharField(max_length=100)
    art = models.CharField(max_length = 100)
    use = models.CharField(max_length = 100)
    comment = models.CharField(max_length = 200)

    def __str__(self):
        return str(self.id)


