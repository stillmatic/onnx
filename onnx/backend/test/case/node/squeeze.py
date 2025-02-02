# SPDX-License-Identifier: Apache-2.0

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import numpy as np

import onnx
from onnx.backend.test.case.base import Base
from onnx.backend.test.case.node import expect


class Squeeze(Base):

    @staticmethod
    def export_squeeze():  # type: () -> None
        node = onnx.helper.make_node(
            'Squeeze',
            inputs=['x', 'axes'],
            outputs=['y'],
        )
        x = np.random.randn(1, 3, 4, 5).astype(np.float32)
        axes = np.array([0], dtype=np.int64)
        y = np.squeeze(x, axis=0)

        expect(node, inputs=[x, axes], outputs=[y],
               name='test_squeeze')

    @staticmethod
    def export_squeeze_negative_axes():  # type: () -> None
        node = onnx.helper.make_node(
            'Squeeze',
            inputs=['x', 'axes'],
            outputs=['y'],
        )
        x = np.random.randn(1, 3, 1, 5).astype(np.float32)
        axes = np.array([-2], dtype=np.int64)
        y = np.squeeze(x, axis=-2)
        expect(node, inputs=[x, axes], outputs=[y],
               name='test_squeeze_negative_axes')
