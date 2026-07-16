from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from .models import Comment
from .forms import CommentForm

def contact(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = CommentForm()

    comments = Comment.objects.all()
    return render(request, 'contact.html', {
        'form': form,
        'comments': comments,
    })


@user_passes_test(lambda u: u.is_staff)
def reply_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'POST':
        reply_text = request.POST.get('reply', '').strip()
        if reply_text:
            comment.reply = reply_text
            comment.save()
    return redirect('contact')