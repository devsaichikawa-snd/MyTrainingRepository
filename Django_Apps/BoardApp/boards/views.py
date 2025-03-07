from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.cache import cache
from django.http import Http404, JsonResponse

from .models import Themes, Comments
from . import forms


def create_theme(request):
    create_theme_form = forms.CreateThemeForm(request.POST or None)
    if create_theme_form.is_valid():
        create_theme_form.instance.user = request.user
        create_theme_form.save()
        messages.success(request, '記事を作成しました。')
        return redirect('boards:list_themes')
    return render(request, 'boards/create_theme.html',
                context={'create_theme_form': create_theme_form, })


def list_themes(request):
    themes = Themes.objects.fetch_all_themes()
    return render(
        request,
        'boards/list_themes.html',
        context={'themes': themes, }
        )


def edit_theme(request, id):
    theme = get_object_or_404(Themes, id=id)
    if theme.user.id != request.user.id:
        raise Http404
    edit_theme_form = forms.CreateThemeForm(request.POST or None, instance=theme)
    if edit_theme_form.is_valid():
        edit_theme_form.save()
        messages.success(request, '記事を更新しました。')
        return redirect('boards:list_themes')
    return render(request, 'boards/edit_theme.html',
                context={'edit_theme_form': edit_theme_form,
                        'id': id })

def delete_theme(request, id):
    theme = get_object_or_404(Themes, id=id)
    if theme.user.id != request.user.id:
        raise Http404
    delete_theme_form = forms.DeleteThemeForm(request.POST or None)
    if delete_theme_form.is_valid(): # csrf tokenのCheck
        theme.delete()
        messages.success(request, '記事を削除しました。')
        return redirect('boards:list_themes')
    return render(request, 'boards/delete_theme.html',
                context={'delete_theme_form': delete_theme_form,})


def post_comments(request, theme_id):
    saved_comment = cache.get(f'saved_comment-theme_id={theme_id}-user_id={request.user.id}', '')
    theme = get_object_or_404(Themes, id=theme_id)
    post_comments_form = forms.PostCommentForm(request.POST or None, initial={'comment': saved_comment})
    comments = Comments.objects.fetch_by_theme_id(theme_id)

    if post_comments_form.is_valid():
        if not request.user.is_authenticated:
            raise Http404
        post_comments_form.instance.theme = theme
        post_comments_form.instance.user = request.user
        post_comments_form.save()
        cache.delete(f'saved_comment-theme_id={theme_id}-user_id={request.user.id}')
        messages.success(request, 'コメントを作成しました。')
        return redirect('boards:post_comments', theme_id=theme_id)
    
    return render(request, 'boards/post_comments.html',
                context={'post_comments_form': post_comments_form,
                        'theme': theme,
                        'comments': comments,})


def save_comment(request):
    # request.is_ajaxはDjango4からは廃止となったので、以下コードにリプレイス
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        comment = request.GET.get('comment')
        theme_id = request.GET.get('theme_id')
        if comment and theme_id:
            cache.set(f'saved_comment-theme_id={theme_id}-user_id={request.user.id}',
                    comment)
            return JsonResponse({'message': '一時保存をしました。',})
        
