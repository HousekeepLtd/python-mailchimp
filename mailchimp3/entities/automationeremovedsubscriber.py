# coding=utf-8
"""
The Automation Removed Subscribers endpoint

Note: This is a paid feature

Documentation: http://developer.mailchimp.com/documentation/mailchimp/reference/automations/removed-subscribers/
Schema: https://api.mailchimp.com/schema/3.0/Automations/RemovedSubscribers/Instance.json
"""
from __future__ import unicode_literals

from mailchimp3.baseapi import BaseApi


class AutomationRemovedSubscriber(BaseApi):
    """
    Remove subscribers from an Automation workflow.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(AutomationRemovedSubscriber, self).__init__(*args, **kwargs)
        self.endpoint = 'automations'
        self.workflow_id = None


    # Paid feature
    def create(self, workflow_id, data):
        """
        Remove a subscriber from a specific Automation workflow. You can
        remove a subscriber at any point in an Automation workflow, regardless
        of how many emails they’ve been sent from that workflow. Once they’re
        removed, they can never be added back to the same workflow.

        :param workflow_id: The unique id for the Automation workflow.
        :type workflow_id: :py:class:`str`
        :param data: The request body parameters
        :type data: :py:class:`dict`
        """
        self.workflow_id = workflow_id
        return self._mc_client._post(url=self._build_path(workflow_id, 'removed-subscribers'), data=data)


    # Paid feature
    def all(self, workflow_id):
        """
        Get information about subscribers who were removed from an Automation
        workflow.

        :param workflow_id: The unique id for the Automation workflow.
        :type workflow_id: :py:class:`str`
        """
        self.workflow_id = workflow_id
        return self._mc_client._get(url=self._build_path(workflow_id, 'removed-subscribers'))

