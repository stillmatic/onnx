# SPDX-License-Identifier: Apache-2.0

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import numpy as np

import onnx
from ..base import Base
from . import expect


def hardmax(x, axis=-1):  # type: (np.ndarray, int) -> np.ndarray
    x_argmax = np.argmax(x, axis=axis)
    y = np.zeros_like(x)
    np.put_along_axis(y, np.expand_dims(x_argmax, axis=axis), 1, axis=axis)
    return y


class Hardmax(Base):
    @staticmethod
    def export():  # type: () -> None
        node = onnx.helper.make_node(
            'Hardmax',
            inputs=['x'],
            outputs=['y'],
        )

        x = np.array([[3, 0, 1, 2], [2, 5, 1, 0], [0, 1, 3, 2],
                      [0, 1, 2, 3]]).astype(np.float32)
        # expect result:
        # [[1. 0. 0. 0.]
        # [0. 1. 0. 0.]
        # [0. 0. 1. 0.]
        # [0. 0. 0. 1.]]
        y = hardmax(x)
        expect(node, inputs=[x], outputs=[y],
               name='test_hardmax_example')

        # For multiple occurrences of the maximal values, the first occurrence is selected for one-hot output
        x = np.array([[3, 3, 3, 1]]).astype(np.float32)
        # expect result:
        # [[1, 0, 0, 0]]
        y = hardmax(x)
        expect(node, inputs=[x], outputs=[y],
               name='test_hardmax_one_hot')

    @staticmethod
    def export_hardmax_axis():  # type: () -> None
        x = np.random.randn(3, 4, 5).astype(np.float32)
        node = onnx.helper.make_node(
            'Hardmax',
            inputs=['x'],
            outputs=['y'],
            axis=0,
        )
        y = hardmax(x, axis=0)
        expect(node, inputs=[x], outputs=[y],
               name='test_hardmax_axis_0')

        node = onnx.helper.make_node(
            'Hardmax',
            inputs=['x'],
            outputs=['y'],
            axis=1,
        )
        y = hardmax(x, axis=1)
        expect(node, inputs=[x], outputs=[y],
               name='test_hardmax_axis_1')

        node = onnx.helper.make_node(
            'Hardmax',
            inputs=['x'],
            outputs=['y'],
            axis=2,
        )
        y = hardmax(x, axis=2)
        expect(node, inputs=[x], outputs=[y],
               name='test_hardmax_axis_2')

        node = onnx.helper.make_node(
            'Hardmax',
            inputs=['x'],
            outputs=['y'],
            axis=-1,
        )
        y = hardmax(x, axis=-1)
        expect(node, inputs=[x], outputs=[y],
               name='test_hardmax_negative_axis')

        # default axis is -1
        node = onnx.helper.make_node(
            'Hardmax',
            inputs=['x'],
            outputs=['y'],
        )
        expect(node, inputs=[x], outputs=[y],
               name='test_hardmax_default_axis')
