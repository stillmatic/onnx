# SPDX-License-Identifier: Apache-2.0

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import numpy as np

import onnx
from ..base import Base
from . import expect


def bernoulli_reference_implementation(x, dtype):  # type: ignore
    # binomial n = 1 equal bernoulli
    # This example and test-case is for informational purpose. The generator operator is
    # non-deterministic and may not produce the same values in different implementations
    # even if a seed is specified.
    return np.random.binomial(1, p=x).astype(dtype)


class Bernoulli(Base):
    @staticmethod
    def export_bernoulli_without_dtype():  # type: () -> None
        node = onnx.helper.make_node(
            'Bernoulli',
            inputs=['x'],
            outputs=['y'],
        )

        x = np.random.uniform(0.0, 1.0, 10).astype(np.float)
        y = bernoulli_reference_implementation(x, np.float)
        expect(node, inputs=[x], outputs=[y], name='test_bernoulli')

    @staticmethod
    def export_bernoulli_with_dtype():  # type: () -> None
        node = onnx.helper.make_node(
            'Bernoulli',
            inputs=['x'],
            outputs=['y'],
            dtype=onnx.TensorProto.DOUBLE,
        )

        x = np.random.uniform(0.0, 1.0, 10).astype(np.float32)
        y = bernoulli_reference_implementation(x, np.float64)
        expect(node, inputs=[x], outputs=[y], name='test_bernoulli_double')

    @staticmethod
    def export_bernoulli_with_seed():  # type: () -> None
        seed = np.float(0)
        node = onnx.helper.make_node(
            'Bernoulli',
            inputs=['x'],
            outputs=['y'],
            seed=seed,
        )

        x = np.random.uniform(0.0, 1.0, 10).astype(np.float32)
        y = bernoulli_reference_implementation(x, np.float32)
        expect(node, inputs=[x], outputs=[y], name='test_bernoulli_seed')
