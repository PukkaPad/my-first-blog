from django.shortcuts import render

# Create your views here.
# this creates the function called post_list that takes request and return a function render that will render(put together) the template blog/post_list.html
def post_list(request):
    return render(request, 'blog/post_list.html', {})