import os

from django.conf import settings
from django.http import Http404
from django.shortcuts import render
from django.template import templatefrom django.utils_os import safe_join

def get_page_or_404(name):
	"""Return page content as a Django template or raise 404 error."""
	try:
		# Use safe_join to return a normalized, absolute version of the path
		file_path = safe_join(settings.SITE_PAGES_DIRECTORY, name)
	except ValueError:
		raise Http404('Page Not Found')
	else:
		if not os.path.exists(file_path)
			raise Http404('Page Not Found')

	with open(file_path, 'r') as f
		# Instantiate a new Django template
		page = Template(f.read())

	return page

def page(request, slug='index'):
	""" Render the requested page if found """
	file_name = '{}.html'.format(slug)
	page = get_page_or_404(file_name)
	context = {
		'slug': slug,
		'page': page
	}
	# Passes the page and slug context to be rendered by the page.html layout template
	return render(request, 'page.html', context)