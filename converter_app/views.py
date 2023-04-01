from django.shortcuts import render
from django.http import HttpResponse
from . import conversion_logic

# Create your views here.
def home(request):
    return render(request, 'base.html')


def submitquery(request):
    conversion_type = request.GET["conversion_type"]
    q = request.GET["query"]
    if conversion_type == "AFBMA_SKF":
        try:
            ans = conversion_logic.AFBMA_to_SKF(q)
            result_dict = {
                "q": q,
                "ans": ans,
                "error": False,
                "result": True,
            }
            return render(request, "base.html", context=result_dict)
        except:
            result_dict = {
                "error": True,
                "result": False,
                "message": "Wrong AFBMA input. 6 Characters are required (e.g. 65BC03)"
            }
            return render(request, "base.html", context=result_dict)

    elif conversion_type == "SKF_AFBMA":
        try:
            ans = conversion_logic.SKF_to_AFBMA(q)
            result_dict = {
                "q": q,
                "ans": ans,
                "error": False,
                "result": True,
            }
            return render(request, "base.html", context=result_dict)
        except:
            result_dict = {
                "error": True,
                "result": False,
                "message": "Wrong SKF input. 4 Characters are required (e.g. 6313)"
            }
            return render(request, "base.html", context=result_dict)
