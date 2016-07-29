# coding=utf-8
"""
The E-commerce Store Orders endpoint API endpoint

Documentation: http://developer.mailchimp.com/documentation/mailchimp/reference/ecommerce/stores/orders/
Schema: https://api.mailchimp.com/schema/3.0/Ecommerce/Stores/Customers/Instance.json
"""
from __future__ import unicode_literals

from mailchimp3.baseapi import BaseApi
from mailchimp3.entities.storeorderline import StoreOrderLine


class StoreOrder(BaseApi):
    """
    Orders represent successful e-commerce transactions, and this data can be
    used to provide more detailed campaign reports, track sales, and
    personalize emails to your targeted consumers, and view other e-commerce
    data in your MailChimp account.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(StoreOrder, self).__init__(*args, **kwargs)
        self.endpoint = 'ecommerce/stores'
        self.store_id = None
        self.order_id = None
        self.line = StoreOrderLine(self)


    def create(self, store_id, data):
        """
        Add a new order to a store.

        :param store_id: The store id.
        :type store_id: :py:class:`str`
        :param data: The request body parameters
        :type data: :py:class:`dict`
        """
        self.store_id = store_id
        response = self._mc_client._post(url=self._build_path(store_id, 'orders'), data=data)
        self.order_id = response['id']
        return response


    def all(self, store_id, get_all=False, **queryparams):
        """
        Get information about a store’s orders.

        :param store_id: The store id.
        :type store_id: :py:class:`str`
        :param get_all: Should the query get all results
        :type get_all: :py:class:`bool`
        :param queryparams: The query string parameters
        queryparams['fields'] = []
        queryparams['exclude_fields'] = []
        queryparams['count'] = integer
        queryparams['offset'] = integer
        """
        self.store_id = store_id
        self.order_id = None
        if get_all:
            return self._iterate(url=self._build_path(store_id, 'orders'), **queryparams)
        else:
            return self._mc_client._get(url=self._build_path(store_id, 'orders'), **queryparams)


    def get(self, store_id, order_id, **queryparams):
        """
        Get information about a specific order.

        :param store_id: The store id.
        :type store_id: :py:class:`str`
        :param order_id: The id for the order in a store.
        :type order_id: :py:class:`str`
        :param queryparams: The query string parameters
        queryparams['fields'] = []
        queryparams['exclude_fields'] = []
        """
        self.store_id = store_id
        self.order_id = order_id
        return self._mc_client._get(url=self._build_path(store_id, 'orders', order_id), **queryparams)


    def update(self, store_id, order_id, data):
        """
        Update a specific order.

        :param store_id: The store id.
        :type store_id: :py:class:`str`
        :param order_id: The id for the order in a store.
        :type order_id: :py:class:`str`
        :param data: The request body parameters
        :type data: :py:class:`dict`
        """
        self.store_id = store_id
        self.order_id = order_id
        return self._mc_client._patch(url=self._build_path(store_id, 'orders', order_id), data=data)


    def delete(self, store_id, order_id):
        """
        Delete an order.

        :param store_id: The store id.
        :type store_id: :py:class:`str`
        :param order_id: The id for the order in a store.
        :type order_id: :py:class:`str`
        """
        self.store_id = store_id
        self.order_id = order_id
        return self._mc_client._delete(url=self._build_path(store_id, 'orders', order_id))