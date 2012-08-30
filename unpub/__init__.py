# -*- coding: utf-8 -*-
from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.

    """
    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)
    # XXX Temporary resource locations until we determine how to best
    #     distribute the aloha-editor code base.
    config.add_static_view('Aloha-Editor',
                           settings['unpub.aloha_editor_resource'])

    # Include the Jinja2 integration package
    config.include('pyramid_jinja2')
    config.add_jinja2_search_path('unpub:templates/')

    # Views / Routes
    config.add_route('casa', '/')
    config.add_route('edit', '/edit')
    config.add_route('metadata', '/metadata')

    config.scan()
    return config.make_wsgi_app()
