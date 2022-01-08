# SPDX-License-Identifier: Apache-2.0

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import numpy as np

import onnx
from ..base import Base
from . import expect


class Tan(Base):

    @staticmethod
    def export():  # type: () -> None
        node = onnx.helper.make_node(
            'Tan',
            inputs=['x'],
            outputs=['y'],
        )

        x = np.array([-1, 0, 1]).astype(np.float32)
        y = np.tan(x)
        expect(node, inputs=[x], outputs=[y],
               name='test_tan_example')

        x = np.random.randn(3, 4, 5).astype(np.float32)
        y = np.tan(x)
        expect(node, inputs=[x], outputs=[y],
               name='test_tan')
