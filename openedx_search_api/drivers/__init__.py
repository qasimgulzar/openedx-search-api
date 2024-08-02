from django.conf import settings
from django.utils.module_loading import import_string


class BaseDriver:
    def get_user_token(self, index_search_rules=None):
        raise Exception("Not Implemented")

    def check_connection(self):
        raise Exception("Not Implemented")

    def indexes(self):
        raise Exception("Not Implemented")

    def index(self, index_name, payload):
        raise Exception("Not Implemented")

    def get_search_rules(self, search_rules=None):
        """
        [
            "ORG: some-value"
        ]
        :param search_rules: you can set list of string filters
        :return:
        """
        raise Exception("Not Implemented")


class DriverFactory:
    @classmethod
    def get_client(cls, request, *args, **kwargs) -> BaseDriver:
        search_driver = getattr(
            settings,
            'SEARCH_ENGINE',
            'django_search_api.drivers.meilisearch.MeiliSearchEngine'
        )
        klass = import_string(search_driver)
        return klass.get_instance(request, *args, **kwargs)
