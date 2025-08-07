from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination

#Function based view

# @api_view(['GET', ])
# def List(request):
#     sumka = Sumkalar.objects.all()
#     category = request.GET.get('category')
#     price = request.GET.get('price')
#     if category:
#         sumka = sumka.filter(Category__name=category)
#     if price:
#         sumka = sumka.filter(price=price)
#     search = request.GET.get('search')
#     if search:
#         sumka = sumka.filter(Q(name__icontains=search) | Q(type__icontains=search))
#     ordering = request.GET.get('ordering')
#     if ordering:
#         sumka = sumka.order_by(ordering)
#     paginator = PageNumberPagination()
#     paginator.page_size = 3
#     paginated_sumka = paginator.paginate_queryset(sumka, request)
#
#     serializer = SumkalarSerializer(paginated_sumka, many=True)
#     res = {
#         'status': status.HTTP_200_OK,
#         'count': len(serializer.data),
#         'results': serializer.data
#     }
#     return paginator.get_paginated_response(res)

# @api_view(['GET'], )
# def detail(request, pk):
#     try:
#         sumka = Sumkalar.objects.get(id=pk)
#     except Sumkalar.DoesNotExist:
#         return Response({'status': status.HTTP_400_BAD_REQUEST,
#                          'error': 'bunday id li sumka mavjud emas'})
#     serializer = SumkalarSerializer(sumka)
#     return Response({'status':status.HTTP_200_OK, 'data':serializer.data})
#
# @api_view(['POST'], )
# def create(request):
#     serializer = SumkalarSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({'status':status.HTTP_200_OK})
#     return Response({'status':status.HTTP_400_BAD_REQUEST, 'error':serializer.errors})
#
# @api_view(['POST'], )
# def update(request, pk):
#     try:
#         sumka = Sumkalar.objects.get(id=pk)
#     except Sumkalar.DoesNotExist:
#         return Response({'status':status.HTTP_404_NOT_FOUND, 'message':'bunday id li sumka topilmadi'})
#     serializer = SumkalarSerializer(instance=sumka, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({'message':'Sumka yangilandi', 'data':serializer.data, 'status':status.HTTP_200_OK})
#
# @api_view(['GET'], )
# def delete(request, pk):
#     try:
#         sumka = Sumkalar.objects.get(id=pk)
#         sumka.delete()
#     except Sumkalar.DoesNotExist:
#         return Response({'status':status.HTTP_404_NOT_FOUND, 'error':'id mavjud emas'})
#     res = {
#         'xabar': 'Ochirildi',
#         'status': status.HTTP_200_OK
#     }
#     return Response(res)
#

#APIView

# class APIViewList(APIView):
#     def get(self, request):
#         sumka = Sumkalar.objects.all()
#         category = request.GET.get('category')
#         price = request.GET.get('price')
#         if category:
#             sumka = sumka.filter(Category__name=category)
#         if price:
#             sumka = sumka.filter(price=price)
#         search = request.GET.get('search')
#         if search:
#             sumka = sumka.filter(Q(name__icontains=search) | Q(type__icontains=search))
#         ordering = request.GET.get('ordering')
#         if ordering:
#             sumka = sumka.order_by(ordering)
#
#         paginator = PageNumberPagination()
#         paginator.page_size = 3
#         paginated_queryset = paginator.paginate_queryset(sumka, request)
#
#         serializer = SumkalarSerializer(paginated_queryset, many=True)
#         data = {
#             'status': status.HTTP_200_OK,
#             'results': serializer.data
#         }
#         return paginator.get_paginated_response(data)


#GenericAPIView

class GenericList(GenericAPIView):
    queryset = Sumkalar.objects.all()
    serializer_class = SumkalarSerializer

    def get(self, request):
        sumka = self.get_queryset()
        category = request.GET.get('category')
        price = request.GET.get('price')
        if category:
            sumka = sumka.filter(Category__name=category)
        if price:
            sumka = sumka.filter(price=price)
        search = request.GET.get('search')
        if search:
            sumka = sumka.filter(Q(name__icontains=search) | Q(type__icontains=search))
        ordering = request.GET.get('ordering')
        if ordering:
            sumka = sumka.order_by(ordering)

        paginator = PageNumberPagination()
        paginator.page_size = 3
        sumka = paginator.paginate_queryset(sumka, request)
        serializer = self.get_serializer(sumka, many=True)
        res = {'data':serializer.data, 'status':status.HTTP_200_OK}
        return paginator.get_paginated_response(res)





