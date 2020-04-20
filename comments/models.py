from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
# Create your models here.
from django.utils import timezone

class Comment(models.Model):
    name = models.CharField('名字', max_length=50)
    text = models.TextField('内容')
    created_time = models.DateTimeField('创建时间', default=timezone.now)
    post = models.ForeignKey('exercise.LearningObject', verbose_name='练习', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{}: {}'.format(self.name, self.text[:20])

class CommentMultip(MPTTModel):
    name = models.CharField('名字',max_length=50)
    text = models.TextField('内容')
    created_time = models.DateTimeField('创建时间', default=timezone.now)
    commentobject = models.ForeignKey(Comment, verbose_name='一级评论', on_delete=models.CASCADE, related_name='replies')#对应属于上一级评论
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children', verbose_name='回复对象')
    
    class Meta:
        verbose_name = '多级评论'
        verbose_name_plural = verbose_name

    class MPTTMeta:
        order_insertion_by = ['created_time']
        
        

    def __str__(self):
        return '{}: {}'.format(self.name, self.text[:20])