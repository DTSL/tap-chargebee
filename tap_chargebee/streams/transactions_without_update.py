from tap_chargebee.streams.base import BaseChargebeeStream


class TransactionsWithoutUpdateStream(BaseChargebeeStream):
    TABLE = 'transactions_without_update'
    ENTITY = 'transaction'
    REPLICATION_METHOD = 'INCREMENTAL'
    REPLICATION_KEY = 'date'
    KEY_PROPERTIES = ['id']
    BOOKMARK_PROPERTIES = ['date']
    SELECTED_BY_DEFAULT = True
    VALID_REPLICATION_KEYS = ['date']
    INCLUSION = 'available'
    API_METHOD = 'GET'

    def get_url(self):
        return 'https://{}/api/v2/transactions'.format(self.config.get('full_site'))
