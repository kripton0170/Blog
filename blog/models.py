from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField 


class CategoryModel(models.Model):
    name = models.CharField(max_length=100)

class BlogModel(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextUploadingField
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey("CategoryModel", on_delete=models.RESTRICT)
    
    def __str__(self):
        return self.title
    
    class  Meta:
        db_table = ''
        managed = True
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'
