# coding: utf-8

# Copyright (C) 2015 by the Free Software Foundation, Inc.
#
# This file is part of mailman.client.
#
# mailman.client is free software: you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published by the
# Free Software Foundation, version 3 of the License.
#
# mailman.client is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public
# License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with mailman.client.  If not, see <http://www.gnu.org/licenses/>.


"""Test unicode data when using REST endpoint."""

from __future__ import absolute_import, print_function, unicode_literals

__metaclass__ = type
__all__ = [
    'TestUnicode',
    ]

import sys
import unittest

from mailmanclient import Client
from six.moves.urllib_error import HTTPError


@unittest.skipIf(sys.version_info.major == 3, "Expected failure on Py3.")
class TestUnicode(unittest.TestCase):
    def setUp(self):
        self._client = Client(
            'http://localhost:9001/3.1', 'restadmin', 'restpass')
        self.email = 'jeremy@example.com'
        self.unicode_string = u'Jérôme'

    def tearDown(self):
        try:
            self._client.get_user(self.email).delete()
        except HTTPError as error:
            if error.status_code == 404:
                pass

    def test_create_user(self):
        user = self._client.create_user(
            email=self.email, password='1234',
            display_name=self.unicode_string)
        self.assertEqual(user.display_name, self.unicode_string)
