# SPDX-License-Identifier: Apache-2.0

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import numpy as np

import onnx
from ..base import Base
from . import expect


class Round(Base):

    @staticmethod
    def export():  # type: () -> None
        node = onnx.helper.make_node(
            'Round',
            inputs=['x'],
            outputs=['y'],
        )

        x = np.array([0.1, 0.5, 0.9, 1.2, 1.5,
                    1.8, 2.3, 2.5, 2.7, -1.1,
                    -1.5, -1.9, -2.2, -2.5, -2.8]).astype(np.float32)
        y = np.array([0., 0., 1., 1., 2.,
                    2., 2., 2., 3., -1.,
                    -2., -2., -2., -2., -3.]).astype(np.float32)  # expected output
        expect(node, inputs=[x], outputs=[y],
               name='test_round')
