from background_task import background
from rest_framework import generics
from rest_framework import permissions, status
from rest_framework.response import Response

from .serializers import *


class ImportRequestList(generics.ListCreateAPIView):
    queryset = ImportRequest.objects.all().order_by('id')
    serializer_class = ImportRequestSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            self.perform_create(serializer)
            execute_task()
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST, headers=headers)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        # serializer.save()

    def get_queryset(self):
        return ImportRequest.objects.filter(owner=self.request.user).order_by('id')
        # return ImportRequest.objects.all().order_by('id')


class ImportRequestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ImportRequest.objects.all().order_by('id')
    serializer_class = ImportRequestSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return ImportRequest.objects.filter(owner=self.request.user).order_by('id')
        # return ImportRequest.objects.all().order_by('id')


@background(schedule=10)
def execute_task():
    print("background_task_executed")
