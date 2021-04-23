from .models import Link

def link_ctx(request):
    ctx={}
    links = Link.objects.all()
    for link in links:
        ctx[link.key]=link.url
    return ctx