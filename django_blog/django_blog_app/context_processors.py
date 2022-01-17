from .models import Category

def common(request):
    """list for template"""
    context = {
        "category_list":Category.objects.all(),
    }

    return context