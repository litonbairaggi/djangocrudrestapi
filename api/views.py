from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response 
from rest_framework import status
 
from api.models import Admission
from api.serializers import AdmissionSerializer
from rest_framework.decorators import api_view

@api_view(["GET"])
def get_admission(request):
    admission = Admission.objects.all()
    serializer = AdmissionSerializer(admission, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def get_admission_detail(request, pk):
    admission = Admission.objects.get(id=pk)
    serializer = AdmissionSerializer(admission, many=False)
    return Response(serializer.data)

@api_view(["POST"])
def post_admission(request):
    serializer = AdmissionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(["POST"])
def post_admission_detail(request, pk):
    admission = Admission.objects.get(id=pk)
    serializer = AdmissionSerializer(instance=admission, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)    

@api_view(['PUT'])
def update_admission(request, pk):
    admission = Admission.objects.get(id=pk)
    serializer = AdmissionSerializer(instance=admission, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
    

@api_view(['DELETE'])
def delete_admission(request, pk):
    admission = Admission.objects.get(id=pk)
    admission.delete()

    return Response('Delete Successfully')        