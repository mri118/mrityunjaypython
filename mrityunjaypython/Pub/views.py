from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

def home(request):
    return render(request, 'publisher.html',{})
def about(request):
    return render(request, 'about.html',{})
def team(request):
    return render(request, 'team.html',{})
class formsubmit(APIView):
    def post(self,request):
        import ipdb
        ipdb.set_trace()
        return Response()