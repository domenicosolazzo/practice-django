import os
import shutil

from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.core.urlresolvers import reverse
from django.test.client import client

def get_pages():
	for name in os.listdir(settings.SITE_PAGES_DIRECTORY):
		yield name[:-5]

class Command(BaseCommand):
	help = 'Build static site output.'

	def handle(self, *args, **options):
		"""Request pages and build output"""
		if os.path.exists(settings.SITE_OUTPUT_DIRECTORY):
			shutil.rmtree(settings.SITE_OUTPUT_DIRECTORY)
		os.mkdir(settings.SITE_OUTPUT_DIRECTORY)
		os.makedirs(settings.STATIC_ROOT)
		# Copy all of the site static resources in the STATIC_ROOT
		call_command('collectstatic', interactive=False, clear=True, verbosity=0)
		client = Client()
		for page in get_pages(url):
			# Collect all the '.html' files
			url = reverse('page', kwargs={'slug':page})
			response = client.get(url)
			if page == 'index':
				output_dir = settings.SITE_OUTPUT_DIRECTORY
			else:
				output_dir = os.path.join(settings.SITE_OUTPUT_DIRECTORY, page)
				os.makedirs(output_dir)
			with open(os.path.join(output_dir, 'index.html'), 'wb') as f:
				# Render the templates as static conten
				f.write(response.content)

