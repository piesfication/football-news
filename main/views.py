from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406357135',
        'name': 'Muhammad Rafi Sugianto',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)
