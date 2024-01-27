from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Task, Category, Priority


from .serializers import TaskSerializer, CategorySerializer, PrioritySerializer


class TaskView(GenericAPIView):
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'id',
                openapi.IN_QUERY,
                description="The new query param",
                type=openapi.TYPE_STRING,
            ),
            openapi.Parameter(
                'status',
                openapi.IN_QUERY,
                description="The new query param",
                type=openapi.TYPE_STRING,
            ),
        ]
    )
    def get(self, request, pk=None):

        if "id" in request.GET:
            get_id = int(request.GET.get('id'))
            lst = Task.objects.filter(id=get_id) & Task.objects.filter(created_by=request.user)
        elif ("status" in request.GET):
            get_status = request.GET['status']
            lst = Task.objects.filter(status=get_status) & Task.objects.filter(created_by=request.user)
        else:
            lst = Task.objects.filter(created_by=request.user)
        return Response({'tasks': TaskSerializer(lst, many=True).data})

    def post(self, request):
        serializer = TaskSerializer(data=request.data, context={'user':request.user})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'task': serializer.data})




class TaskViewDetail(GenericAPIView):
    serializer_class = TaskSerializer
    def get(self, request, pk=None):
        task = Task.objects.get(pk=pk)
        if task.created_by == request.user or request.user.is_staff:
            serializer = TaskSerializer(task)
            return Response(serializer.data)
        return Response("not authorized")

    def put(self, request, pk=None):
        try:
            task = Task.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})
        if task.created_by == request.user or request.user.is_staff:
            data = request.data
            serializer = TaskSerializer(data=data, instance=task)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"task": serializer.data})
        return Response("not authorized")

    def delete(self, request, pk=None):
        try:
            task = Task.objects.get(pk=pk)
            if request.user.is_staff:
                task.delete()
            else:
                if task.created_by == request.user:
                    task.deleted = True
                    task.save()
                else:
                    return Response("not authorized")
        except:
            return Response({"error": "Object does not exists"})

        return Response({"task": "delete task " + str(pk)})


class CategoryView(GenericAPIView):
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk=None):
        lst = Category.objects.all()
        return Response({'category': CategorySerializer(lst, many=True).data})

    def post(self, request):
        serializer = CategorySerializer(data=request.data, context={'user': request.user})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'category': serializer.data})


class CategoryViewDetail(GenericAPIView):
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)
    def get(self, request, pk=None):
        category = Category.objects.get(pk=pk)
        if category.created_by == request.user or request.user.is_staff:
            serializer = CategorySerializer(category)
            return Response(serializer.data)
        return Response("not authorized")

    def put(self, request, pk=None):
        try:
            category = Category.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})
        if category.created_by == request.user or request.user.is_staff:
            data = request.data
            serializer = CategorySerializer(data=data, instance=category)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"category": serializer.data})
        return Response("not authorized")

    def delete(self, request, pk=None):
        try:
            category = Category.objects.get(pk=pk)
            if request.user.is_staff:
                category.delete()
            else:
                if category.created_by == request.user:
                    category.deleted = True
                    category.save()
                else:
                    return Response("not authorized")
        except:
            return Response({"error": "Object does not exists"})

        return Response({"category": "delete category " + str(pk)})


class PriorityView(GenericAPIView):
    serializer_class = PrioritySerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk=None):
        lst = Priority.objects.all()
        return Response({'priority': PrioritySerializer(lst, many=True).data})

    def post(self, request):
        serializer = PrioritySerializer(data=request.data, context={'user': request.user})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'priority': serializer.data})


class PriorityViewDetail(GenericAPIView):
    serializer_class = PrioritySerializer
    permission_classes = (IsAuthenticated,)
    def get(self, request, pk=None):
        priority = Priority.objects.get(pk=pk)
        if priority.created_by == request.user or request.user.is_staff:
            serializer = PrioritySerializer(priority)
            return Response(serializer.data)
        return Response("not authorized")

    def put(self, request, pk=None):
        try:
            priority = Priority.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})
        if priority.created_by == request.user or request.user.is_staff:
            data = request.data
            serializer = PrioritySerializer(data=data, instance=priority)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"priority": serializer.data})
        return Response("not authorized")

    def delete(self, request, pk=None):
        try:
            priority = Priority.objects.get(pk=pk)
            if request.user.is_staff:
                priority.delete()
            else:
                if priority.created_by == request.user:
                    priority.deleted = True
                    priority.save()
                else:
                    return Response("not authorized")
        except:
            return Response({"error": "Object does not exists"})

        return Response({"priority": "delete priority " + str(pk)})