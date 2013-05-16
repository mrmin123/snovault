from pyramid.view import view_config
from ..contentbase import (
    Root,
    location,
    location_root,
)


def includeme(config):
    config.scan()


@location_root
class EncodedRoot(Root):
    properties = {
        'title': 'Home',
        'portal_title': 'ENCODE 3',
    }


# BBB
def root():
    pass

root.location = location


@view_config(context=Root, request_method='GET')
def home(context, request):
    result = context.__json__(request)
    result['_links'] = {
        'self': {'href': request.resource_path(context)},
        'profile': {'href': '/profiles/portal'},
        # 'login': {'href': request.resource_path(context, 'login')},
    }
    return result
