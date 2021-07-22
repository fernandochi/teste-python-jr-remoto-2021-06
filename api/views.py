from rest_framework import generics, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
import requests



from .models import Project
from .serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = "name"

    @action(detail=True)
    def get_by_name(self, request, name=None):

        project = self.queryset.filter(name__iexact=name).first()

        if not project:
            return Response({"error": "Project does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(project)

        return Response(serializer.data)

    @action(detail=False)
    def delete_project(self, request, name=None):
        project = self.queryset.filter(name__iexact=name)

        if not project:
            return Response({"error": "Project does not exist"}, status=status.HTTP_404_NOT_FOUND)

        project.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)