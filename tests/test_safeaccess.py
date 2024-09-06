# -*- coding: utf-8 -*-

import requests_mock

from tests.api import TestCaseApi
from tests.payload import (
    SAFE_ACCESS_STATUS_PAYLOAD,
    PUT_SUCCESS_RESPONSE
)


class TestSafeAccess(TestCaseApi):

    @requests_mock.Mocker()
    def test_get_status(self, m):
        self._mock_login(m)
        m.get(
            '{}/entry.cgi'.format(self.http._get_base_url()),
            json=SAFE_ACCESS_STATUS_PAYLOAD,
        )

        groups = self.client.safeaccess.get_status()

        self.assertEqual(len(groups), 3)
        self.assertEqual(groups[1]['name'], 'Alice')
        self.assertEqual(groups[2]['pause'], False)

        self.http.sid = None

    @requests_mock.Mocker()
    def test_pause(self, m):
        self._mock_login(m)
        m.get(
            '{}/entry.cgi'.format(self.http._get_base_url()),
            json=PUT_SUCCESS_RESPONSE,
        )

        result = self.client.safeaccess.pause(4)

        self.assertEqual(result, True)

        self.http.sid = None

    @requests_mock.Mocker()
    def test_resume(self, m):
        self._mock_login(m)
        m.get(
            '{}/entry.cgi'.format(self.http._get_base_url()),
            json=PUT_SUCCESS_RESPONSE,
        )

        result = self.client.safeaccess.resume(4)

        self.assertEqual(result, True)

        self.http.sid = None

    @requests_mock.Mocker()
    def test_reward(self, m):
        self._mock_login(m)
        m.get(
            '{}/entry.cgi'.format(self.http._get_base_url()),
            json=PUT_SUCCESS_RESPONSE,
        )

        result = self.client.safeaccess.reward(4, 60)

        self.assertEqual(result, True)

        self.http.sid = None

    @requests_mock.Mocker()
    def test_reward_cancel(self, m):
        self._mock_login(m)
        m.get(
            '{}/entry.cgi'.format(self.http._get_base_url()),
            json=PUT_SUCCESS_RESPONSE,
        )

        result = self.client.safeaccess.reward_cancel(4)

        self.assertEqual(result, True)

        self.http.sid = None
