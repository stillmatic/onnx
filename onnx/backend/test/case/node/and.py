# SPDX-License-Identifier: Apache-2.0

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import numpy as np

import onnx
from ..base import Base
from . import expect


class And(Base):

    @staticmethod
    def export():  # type: () -> None
        node = onnx.helper.make_node(
            'And',
            inputs=['x', 'y'],
            outputs=['and'],
        )

        # 2d
        x = (np.random.randn(3, 4) > 0).astype(bool)
        y = (np.random.randn(3, 4) > 0).astype(bool)
        z = np.logical_and(x, y)
        expect(node, inputs=[x, y], outputs=[z],
               name='test_and2d')

        # 3d
        x = (np.random.randn(3, 4, 5) > 0).astype(bool)
        y = (np.random.randn(3, 4, 5) > 0).astype(bool)
        z = np.logical_and(x, y)
        expect(node, inputs=[x, y], outputs=[z],
               name='test_and3d')

        # 4d
        x = (np.random.randn(3, 4, 5, 6) > 0).astype(bool)
        y = (np.random.randn(3, 4, 5, 6) > 0).astype(bool)
        z = np.logical_and(x, y)
        expect(node, inputs=[x, y], outputs=[z],
               name='test_and4d')

    @staticmethod
    def export_and_broadcast():  # type: () -> None
        node = onnx.helper.make_node(
            'And',
            inputs=['x', 'y'],
            outputs=['and'],
        )

        # 3d vs 1d
        x = (np.random.randn(3, 4, 5) > 0).astype(bool)
        y = (np.random.randn(5) > 0).astype(bool)
        z = np.logical_and(x, y)
        expect(node, inputs=[x, y], outputs=[z],
               name='test_and_bcast3v1d')

        # 3d vs 2d
        x = (np.random.randn(3, 4, 5) > 0).astype(bool)
        y = (np.random.randn(4, 5) > 0).astype(bool)
        z = np.logical_and(x, y)
        expect(node, inputs=[x, y], outputs=[z],
               name='test_and_bcast3v2d')

        # 4d vs 2d
        x = (np.random.randn(3, 4, 5, 6) > 0).astype(bool)
        y = (np.random.randn(5, 6) > 0).astype(bool)
        z = np.logical_and(x, y)
        expect(node, inputs=[x, y], outputs=[z],
               name='test_and_bcast4v2d')

        # 4d vs 3d
        x = (np.random.randn(3, 4, 5, 6) > 0).astype(bool)
        y = (np.random.randn(4, 5, 6) > 0).astype(bool)
        z = np.logical_and(x, y)
        expect(node, inputs=[x, y], outputs=[z],
               name='test_and_bcast4v3d')

        # 4d vs 4d
        x = (np.random.randn(1, 4, 1, 6) > 0).astype(bool)
        y = (np.random.randn(3, 1, 5, 6) > 0).astype(bool)
        z = np.logical_and(x, y)
        expect(node, inputs=[x, y], outputs=[z],
               name='test_and_bcast4v4d')
