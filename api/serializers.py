from rest_framework import serializers
from rest_framework.response import Response

from .models import PackageRelease, Project

from django.db import transaction
import requests


class PackageSerializer(serializers.ModelSerializer):
	class Meta:
		model = PackageRelease
		fields = ['name', 'version']
		extra_kwargs = {'version': {'required': False}}


class ProjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = Project
		fields = ['name', 'packages']
		depth = 1

	packages = PackageSerializer(many=True)

	@transaction.atomic
	def create(self, validated_data):
		# TODO
		# - Processar os pacotes recebidos
		# - Persistir informações no banco
		packages = validated_data['packages']

		project = Project.objects.get_or_create(name=validated_data['name'])[0]

		for package in packages:

			package_name = package['name']
			package_version = package.get('version', None)

			r = requests.get(f"https://pypi.org/pypi/{package_name}/json/")
			if r.status_code == 404:
				raise serializers.ValidationError({"error": "One or more packages doesn't exist"})

			package_name = r.json()['info']['name']

			if not package_version:
				package_version = r.json()['info']['version']

			r = requests.get(f"https://pypi.org/pypi/{package_name}/{package_version}/json/")

			if r.status_code == 404:
				raise serializers.ValidationError({"error": "One or more packages doesn't exist"})

			package_release = PackageRelease.objects \
				.get_or_create(name=package_name, version=package_version, project=project)[0]

		return project
