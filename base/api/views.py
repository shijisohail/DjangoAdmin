from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Blog, Machine
from .serializers import BlogSerializer
@api_view(['GET','POST'])
def getroutes(request):
    routes = [
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id'
        'POST /api'
        'POST /api/rooms'
        'POST /api/rooms/:id'
    ]
    return Response(routes) 

@api_view(['GET','POST'])
def getrooms(request): 
    rooms = Blog.objects.all()  
    serializer = BlogSerializer(rooms,many = True)
    return Response(serializer.data)

@api_view(['GET','POST'])   
def getroom(request,pk):
    Blog = Blog.objects.get(id=pk)
    serializer = BlogSerializer(Blog,many = False)
    return Response(serializer.data)