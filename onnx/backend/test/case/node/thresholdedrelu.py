# SPDX-License-Identifier: Apache-2.0

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import numpy as np

import onnx
from ..base import Base
from . import expect


class ThresholdedRelu(Base):

    @staticmethod
    def export():  # type: () -> None
        alpha = 2.0
        node = onnx.helper.make_node(
            'ThresholdedRelu',
            inputs=['x'],
            outputs=['y'],
            alpha=alpha
        )

        x = np.array([-1.5, 0., 1.2, 2.0, 2.2]).astype(np.float32)
        y = np.clip(x, alpha, np.inf)  # expected output [0., 0., 0., 0., 2.2]
        y[y == alpha] = 0

        expect(node, inputs=[x], outputs=[y],
               name='test_thresholdedrelu_example')

        x = np.random.randn(3, 4, 5).astype(np.float32)
        y = np.clip(x, alpha, np.inf)
        y[y == alpha] = 0

        expect(node, inputs=[x], outputs=[y],
               name='test_thresholdedrelu')

    @staticmethod
    def export_default():  # type: () -> None
        default_alpha = 1.0
        node = onnx.helper.make_node(
            'ThresholdedRelu',
            inputs=['x'],
            outputs=['y']
        )
        x = np.random.randn(3, 4, 5).astype(np.float32)
        y = np.clip(x, default_alpha, np.inf)
        y[y == default_alpha] = 0

        expect(node, inputs=[x], outputs=[y],
               name='test_thresholdedrelu_default')
