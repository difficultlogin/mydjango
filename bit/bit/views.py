from django.shortcuts import render_to_response

def front_page(request):
    return render_to_response('front-page.html')