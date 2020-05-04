from django.shortcuts import render
from rest_framework import viewsets
from .models import personalData
from .serializers import personalDataSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import parser_classes
from rest_framework.parsers import FileUploadParser 
import xlrd
from collections import OrderedDict
import json
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings

class personalDataViewSet(APIView):
    queryset = personalData.objects.all().order_by('surname','name','link','academicDegree','position','department')
    serializer_class = personalDataSerializer

    def get(self, request):
        queryset = personalData.objects.all().order_by('surname','name','link','academicDegree','position','department')
        serializer_class = personalDataSerializer(queryset, many = True)
        return Response(serializer_class.data)

    def post(self, request):
        serializer_class = personalDataSerializer(data = request.data)
        print(serializer_class)
        if serializer_class.is_valid():
            serializer_class.save()
        return Response()

class excelDownloadViewSet(APIView):

    parser_classes = [FileUploadParser]

    def post(self, request, filename, format=None):
        
        def sheetToList(sheet):
            employersData = list()
            headers = sheet.row_values(0)
            employers = OrderedDict()
            for rownum in range(1, sheet.nrows):
                employer = OrderedDict()
                row_values = sheet.row_values(rownum)
                for index in range(len(row_values)):
                    employer[headers[index]] = row_values[index]
                employers[str(rownum)] = employer
                for item in list(employers.items()):
                  employersData.append(item[1])
            return employersData

        def sheet_to_personaldata_objects():
          file_obj = request.data['file']
          path = default_storage.save('tmp/data.xlsx', ContentFile(file_obj.read()))
          wb = xlrd.open_workbook('tmp/data.xlsx')
          sh = wb.sheet_by_index(0)
          j = sheetToList(sh)
          for item in j:
            personalDataItem = personalData()
            personalDataItem.surname = item['surname']
            personalDataItem.name = item['name']
            personalDataItem.link = item['link']
            personalDataItem.academicDegree = item['academicDegree']
            personalDataItem.position = item['position']
            personalDataItem.department = item['department']
            personalDataItem.save()

        sheet_to_personaldata_objects()

        return Response(status=204)