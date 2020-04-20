from django import template
from ..forms import CommentForm
from exercise.models import LearningObject
from django.shortcuts import get_object_or_404
from django.db.models import Count
from ..models import Comment

register = template.Library()
 

@register.inclusion_tag('comments/inclusions/_form.html', takes_context=True)
def show_comment_form(context, post, form=None):
    if form is None:
        form = CommentForm()
    return {
        'form': form,
        'post': post,
    }

@register.inclusion_tag('comments/inclusions/_list.html', takes_context=True)
def show_comments(context, exercise):
    learningobject = get_object_or_404(LearningObject, service_url=exercise.service_url)
    q = LearningObject.objects.annotate(page_count=Count('comments')).filter(service_url=exercise.service_url).count()

    # con = get_object_or_404(Comment, post=learningobject)
    q2 = Comment.objects.annotate(page_count=Count('text')).filter(post=learningobject).count()

    comment_list = learningobject.comment_set.all()
    #comment_list = learningobject.comments
    comment_count = q2
    return {
        'comment_count': comment_count,
        'comment_list': comment_list,
        'learningobject': learningobject,
    }