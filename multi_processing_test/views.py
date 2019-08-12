from rest_framework import generics
from rest_framework import permissions, status
from rest_framework.response import Response

from .serializers import *
import logging
import queue
import time
from multiprocessing import Process, Queue, current_process, cpu_count


class ImportRequestList(generics.ListCreateAPIView):
    queryset = ImportRequest.objects.all().order_by('id')
    serializer_class = ImportRequestSerializer
    permission_classes = (permissions.AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST, headers=headers)

    def perform_create(self, serializer):
        # serializer.save(owner=self.request.user)
        serializer.save()

    def get_queryset(self):
        # return ImportRequest.objects.filter(owner=self.request.user)
        return ImportRequest.objects.all()


class ImportRequestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ImportRequest.objects.all().order_by('id')
    serializer_class = ImportRequestSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        # return ImportRequest.objects.filter(owner=self.request.user)
        return ImportRequest.objects.all()


class MultiProcessing:

    def __init__(self):
        self.running = ImportRequest.objects.filter(running=1)
        self.queued = ImportRequest.objects.filter(running=0)

    def initialize_import(self):
        tasks = self.queued
        number_of_processes = cpu_count()
        tasks_to_process = Queue()
        tasks_completed = Queue()
        processes = []

        for task in tasks:
            tasks_to_process.put(str(task))

        # creating processes
        for _ in range(number_of_processes):
            p = Process(target=self.do_job, args=(tasks_to_process, tasks_completed))
            processes.append(p)
            p.start()

        # completing process
        for p in processes:
            p.join()

        # print the output
        while not tasks_completed.empty():
            print(tasks_completed.get())

    def do_job(self, tasks_to_accomplish, tasks_that_are_done):
        while True:
            try:
                task = tasks_to_accomplish.get_nowait()
                self.initialize_logger('log_' + str(task), str(task) + ".log")
            except queue.Empty:
                break
            else:
                self.print_func(task)
                tasks_that_are_done.put(task + ' is done by ' + current_process().name)
                time.sleep(1)
        return True

    @staticmethod
    def initialize_logger(logger_name, log_file, level=logging.INFO):
        log_setup = logging.getLogger(logger_name)
        formatter = logging.Formatter('%(levelname)s: %(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        file_handler = logging.FileHandler(log_file, mode='a')
        file_handler.setFormatter(formatter)
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        log_setup.setLevel(level)
        log_setup.addHandler(file_handler)
        log_setup.addHandler(stream_handler)

    @staticmethod
    def print_func(task):
        log = logging.getLogger("log_" + task)
        log.info("started")
        log.info(task + ' is done by ' + current_process().name)
        log.info("ended")
