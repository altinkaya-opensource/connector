# -*- coding: utf-8 -*-
# Copyright 2013-2017 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from odoo.tests import common
from odoo.addons.test_component.components.components import TestUserComponent


class TestComponentCollection(common.TransactionCase):

    def setUp(self):
        super(TestComponentCollection, self).setUp()

    def tearDown(self):
        super(TestComponentCollection, self).tearDown()

    def test_register_component(self):
        collection = self.env['test.component.collection'].create(
            {'name': 'Test'}
        )
        work = collection.work_on('res.users')
        component = work.components(name='test.user.component')
        self.assertEquals(TestUserComponent._name, component._name)
