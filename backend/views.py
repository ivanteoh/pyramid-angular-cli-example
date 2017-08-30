import logging
log = logging.getLogger(__name__)

from pyramid.view import (
    view_config
    )

@view_config(route_name='home', renderer='static/index.pt')
def home_view(request):
    log.debug('In home view')
    return {}
