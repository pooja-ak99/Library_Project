from django.shortcuts import render
from Books.models import Booktable
from rest_framework.decorators import api_view
from Books.serializers import bookserializer, userserializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins, generics , viewsets

# #function based

# @api_view(['GET','POST'])
#
# def booklist(request):
#     if(request.method=="GET"):
#         book = Booktable.objects.all()
#         b = bookserializer(book,many=True)
#         return Response(b.data)
#     elif(request.method=="POST"):
#         b = bookserializer(data=request.data)
#         if b.is_valid():
#             b.save()
#             return Response(b.data,status=status.HTTP_201_CREATED)
#         return Response(b.errors,status=status.HTTP_400_BAD_REQUEST)
#
#
#
# @api_view(['GET','PUT','DELETE'])
# def book_detail(request,pk):
#     try:
#         book = Booktable.objects.get(pk=pk)
#     except:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if(request.method=="GET"):
#         b = bookserializer(book)
#         return Response(b.data)
#     elif(request.method=="PUT"):
#         b = bookserializer(book,data=request.data)
#         if b.is_valid():
#             b.save()
#             return Response(b.data, status=status.HTTP_201_CREATED)
#         return Response(b.error,status=status.HTTP_400_BAD_REQUEST)
#     elif(request.method=="DELETE"):
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# #class based (using mixins)

# class booklist(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Booktable.objects.all()
#     serializer_class = bookserializer
#
#     def get(self,request):
#         return self.list(request)
#
#     def post(self,request):
#         return self.create(request)
#
#
# class bookdetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset = Booktable.objects.all()
#     serializer_class = bookserializer
#
#     def get(self, request, pk):
#         return self.retrieve(request)
#
#     def put(self,request,pk):
#         return self.update(request)
#
#     def delete(self,request,pk):
#         return self.destroy(request)


# # class based using Generics
#
# class booklist(generics.ListCreateAPIView):
#     queryset = Booktable.objects.all()
#     serializer_class = bookserializer
#
# class bookdetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Booktable.objects.all()
#     serializer_class = bookserializer


# # class based using view set

class bookviewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]     #to access only if authenticated
    queryset = Booktable.objects.all()
    serializer_class = bookserializer


class Userviewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = userserializer
