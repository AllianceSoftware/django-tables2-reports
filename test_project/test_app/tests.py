# -*- coding: utf-8 -*-
# Copyright (c) 2012-2013 by Pablo Martín <goinnn@gmail.com>
#
# This software is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this software.  If not, see <http://www.gnu.org/licenses/>.

from django.test import TestCase

from django.core.urlresolvers import reverse


class TestRenderDT2R(TestCase):

    def _test_check_render(self, url):
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        return response

    def test_check_render_class_view(self):
        url = reverse('index')
        response = self._test_check_render(url)
        return response

    def test_check_render_function_view(self):
        url = reverse('index_function_view')
        response = self._test_check_render(url)
        return response

    def test_equal_class_view_and_function_view(self):
        response_clv = self.test_check_render_class_view()
        response_fv = self.test_check_render_function_view()
        self.assertEqual(response_clv.status_code, response_fv.status_code)
        self.assertEqual(response_clv.content, response_fv.content)
