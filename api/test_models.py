from django.test import TestCase
from .models import Project, PackageRelease


class ProjectModelTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		cls.project_solo = Project.objects.create(
			name="Foo"
		)

		cls.project = Project.objects.create(
			name="Bar",
		)

		cls.package_django = PackageRelease.objects.create(
			name="Django",
			version="3.0",
			project=cls.project
		)

		cls.package_flask = PackageRelease.objects.create(
			name="Flask",
			version="2.0.0",
			project= cls.project
		)

		cls.project_last = Project.objects.create(
			name="Baz",
		)

		cls.package_django_last = PackageRelease.objects.create(
			name="Django",
			version="3.2.5",
			project=cls.project_last
		)
		cls.package_flask_last = PackageRelease.objects.create(
			name="Flask",
			version="2.0.1",
			project=cls.project_last
		)

	def test_input_model_solo(self):
		self.assertIsInstance(self.project_solo.name, str)
		self.assertEqual(self.project_solo.name, "Foo")
		# self.assertEqual(self.project_solo.packages, [])

	def test_input_model(self):
		self.assertIsInstance(self.project.name, str)
		self.assertEqual(self.project.name, "Bar")

		self.assertIsInstance(self.package_django.name, str)
		self.assertEqual(self.package_django.name, "Django")
		self.assertIsInstance(self.package_django.version, str)
		self.assertEqual(self.package_django.version, "3.0")
		self.assertEqual(self.package_django.project, self.project)

		self.assertIsInstance(self.package_flask.name, str)
		self.assertEqual(self.package_flask.name, "Flask")
		self.assertIsInstance(self.package_flask.version, str)
		self.assertEqual(self.package_flask.version, "2.0.0")
		self.assertNotEqual(self.package_flask.version, "2.0.1")
		self.assertEqual(self.package_flask.project, self.project)

	def test_input_model_last(self):
		self.assertIsInstance(self.project_last.name, str)
		self.assertEqual(self.project_last.name, "Baz")

		self.assertIsInstance(self.package_django_last.name, str)
		self.assertEqual(self.package_django_last.name, "Django")
		self.assertIsInstance(self.package_django_last.version, str)
		self.assertEqual(self.package_django_last.version, "3.2.5")
		self.assertEqual(self.package_django_last.project, self.project_last)

		self.assertIsInstance(self.package_flask_last.name, str)
		self.assertEqual(self.package_flask_last.name, "Flask")
		self.assertIsInstance(self.package_flask_last.version, str)
		self.assertEqual(self.package_flask_last.version, "2.0.1")
		self.assertEqual(self.package_flask_last.project, self.project_last)
