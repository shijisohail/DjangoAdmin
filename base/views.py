from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from base.models import Blog

# Create your views here.
# rooms = [
#    { 'id' : 1, 'name' : 'Let`s Start Hacking'},
#    { 'id' : 2, 'name' : 'Let`s learn Development'},
#    { 'id' : 3, 'name' : 'Let`s learn CyberSecurity'},
# ]
def home(request):
    rooms = Blog.objects.all() 
    context = {'rooms':rooms}
    return render(request, 'base/home.html',context)
def room(request,pk):
    room= Blog.objects.get(id = pk)
    
    context = {'room':room}

    return render(request, 'base/room.html',context)
   

class ProfileView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user.email),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)