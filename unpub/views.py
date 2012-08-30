# -*- coding: utf-8 -*-
from pyramid.view import view_config


SITE_TITLE = 'Connexions Authoring Services'


@view_config(route_name='casa', renderer='casa.jinja2')
def casa(request):
    """The home page for this application."""
    return {'title': SITE_TITLE}

@view_config(route_name='edit', renderer='edit.jinja2')
def edit(request):
    """The editor page for this application."""
    return {'title': SITE_TITLE}

@view_config(route_name='metadata', renderer='metadata.jinja2')
def metadata(request):
    """The metadata form page for this application."""
    return {'title': SITE_TITLE}
