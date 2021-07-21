from django.test import TestCase
from rest_framework.test import APIClient
import json


class ApiTestViews(TestCase):
	def setUp(self):
		self.client = APIClient()

		self.project_solo_data = {
			"name": "Foo",
			"packages": []
		}

		self.project_data = {
			"name": "Bar",
			"packages": [
				{"name": "django", "version": "3.0"},
				{'name': "panda", "version": "0.1.5"}
			]
		}

		self.project_last_data = {
			"name": "Baz",
			"packages": [
				{"name": "flask"},
				{"name": "panda"}
			]
		}

	def test_get_projects_empty(self):
		response = self.client.get('/api/projects/')

		self.assertListEqual(response.json(), [])

	def test_create_project_no_packages(self):
		response = self.client.post('/api/projects/', self.project_solo_data, format='json')

		expected = {
			"name": "Foo",
			"packages": []
		}

		self.assertEqual(response.status_code, 201)
		self.assertDictEqual(response.json(), expected)

	def test_crate_project(self):
		response = self.client.post('/api/projects/', self.project_data, format='json')

		expected = {
			"name": "Bar",
			"packages": [
				{"name": "Django", "version": "3.0"},
				{"name": "panda", "version": "0.1.5"}
			]
		}

		self.assertEqual(response.status_code, 201)
		self.assertDictEqual(response.json(), expected)

	def test_create_project_last(self):
		response = self.client.post('/api/projects/', self.project_last_data, format='json')

		expected = {
			"name": "Baz",
			"packages": [
				{"name": "Flask", "version": "2.0.1"},
				{"name": "panda", "version": "0.3.1"}
			]
		}

		self.assertEqual(response.status_code, 201)
		self.assertDictEqual(response.json(), expected)

	def test_list_all_projects(self):
		self.client.post('/api/projects/', self.project_last_data, format='json')

		response = self.client.get('/api/projects/')

		expected = {
			"name": "Baz",
			"packages": [
				{"name": "Flask", "version": "2.0.1"},
				{"name": "panda", "version": "0.3.1"}
			]
		}

		self.assertListEqual(response.json(), [expected])
		self.assertEqual(response.status_code, 200)

	def test_not_package(self):
		data = {
			"name": "John",
			"packages": [
				{"name": "larara"}
			]
		}

		expected = {"error": "One or more packages doesn't exist"}

		response = self.client.post('/api/projects/', data, format='json')

		self.assertEqual(response.status_code, 400)
		self.assertDictEqual(response.json(), expected)

	def test_retrieve(self):
		self.client.post('/api/projects/', self.project_last_data, format='json')

		response = self.client.get('/api/projects/baz/')

		expected = {
			"name": "Baz",
			"packages": [
				{"name": "Flask", "version": "2.0.1"},
				{"name": "panda", "version": "0.3.1"}
			]
		}

		self.assertDictEqual(response.json(), expected)
		self.assertEqual(response.status_code, 200)

		no_exist = self.client.get('/api/projects/nothing/')

		self.assertEqual(no_exist.status_code, 404)

	def test_delete(self):
		self.client.post('/api/projects/', self.project_last_data, format='json')

		response = self.client.get('/api/projects/')

		self.assertEqual(len(response.json()), 1)

		response_delete = self.client.delete('/api/projects/baz/')

		self.assertEqual(response_delete.status_code, 204)

		response = self.client.get('/api/projects/')

		self.assertEqual(response.status_code, 200)
		self.assertListEqual(response.json(), [])
