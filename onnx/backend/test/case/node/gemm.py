# SPDX-License-Identifier: Apache-2.0

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import numpy as np
from typing import Optional

import onnx
from ..base import Base
from . import expect


def gemm_reference_implementation(A, B, C=None, alpha=1., beta=1., transA=0,
                                  transB=0):  # type: (np.ndarray, np.ndarray, Optional[np.ndarray], float, float, int, int) -> np.ndarray
    A = A if transA == 0 else A.T
    B = B if transB == 0 else B.T
    C = C if C is not None else np.array(0)

    Y = alpha * np.dot(A, B) + beta * C

    return Y


class Gemm(Base):

    @staticmethod
    def export_default_zero_bias():  # type: () -> None
        node = onnx.helper.make_node(
            'Gemm',
            inputs=['a', 'b', 'c'],
            outputs=['y']
        )
        a = np.random.ranf([3, 5]).astype(np.float32)
        b = np.random.ranf([5, 4]).astype(np.float32)
        c = np.zeros([1, 4]).astype(np.float32)
        y = gemm_reference_implementation(a, b, c)
        expect(node, inputs=[a, b, c], outputs=[y],
               name='test_gemm_default_zero_bias')

    @staticmethod
    def export_default_no_bias():  # type: () -> None
        node = onnx.helper.make_node(
            'Gemm',
            inputs=['a', 'b'],
            outputs=['y']
        )
        a = np.random.ranf([2, 10]).astype(np.float32)
        b = np.random.ranf([10, 3]).astype(np.float32)
        y = gemm_reference_implementation(a, b)
        expect(node, inputs=[a, b], outputs=[y],
               name='test_gemm_default_no_bias')

    @staticmethod
    def export_default_scalar_bias():  # type: () -> None
        node = onnx.helper.make_node(
            'Gemm',
            inputs=['a', 'b', 'c'],
            outputs=['y']
        )
        a = np.random.ranf([2, 3]).astype(np.float32)
        b = np.random.ranf([3, 4]).astype(np.float32)
        c = np.array(3.14).astype(np.float32)
        y = gemm_reference_implementation(a, b, c)
        expect(node, inputs=[a, b, c], outputs=[y],
               name='test_gemm_default_scalar_bias')

    @staticmethod
    def export_default_single_elem_vector_bias():  # type: () -> None
        node = onnx.helper.make_node(
            'Gemm',
            inputs=['a', 'b', 'c'],
            outputs=['y']
        )
        a = np.random.ranf([3, 7]).astype(np.float32)
        b = np.random.ranf([7, 3]).astype(np.float32)
        c = np.random.ranf([1]).astype(np.float32)
        y = gemm_reference_implementation(a, b, c)
        expect(node, inputs=[a, b, c], outputs=[y],
               name='test_gemm_default_single_elem_vector_bias')

    @staticmethod
    def export_default_vector_bias():  # type: () -> None
        node = onnx.helper.make_node(
            'Gemm',
            inputs=['a', 'b', 'c'],
            outputs=['y']
        )
        a = np.random.ranf([2, 7]).astype(np.float32)
        b = np.random.ranf([7, 4]).astype(np.float32)
        c = np.random.ranf([1, 4]).astype(np.float32)
        y = gemm_reference_implementation(a, b, c)
        expect(node, inputs=[a, b, c], outputs=[y],
               name='test_gemm_default_vector_bias')

    @staticmethod
    def export_default_matrix_bias():  # type: () -> None
        node = onnx.helper.make_node(
            'Gemm',
            inputs=['a', 'b', 'c'],
            outputs=['y']
        )
        a = np.random.ranf([3, 6]).astype(np.float32)
        b = np.random.ranf([6, 4]).astype(np.float32)
        c = np.random.ranf([3, 4]).astype(np.float32)
        y = gemm_reference_implementation(a, b, c)
        expect(node, inputs=[a, b, c], outputs=[y],
               name='test_gemm_default_matrix_bias')

    @staticmethod
    def export_transposeA():  # type: () -> None
        node = onnx.helper.make_node(
            'Gemm',
            inputs=['a', 'b', 'c'],
            outputs=['y'],
            transA=1
        )
        a = np.random.ranf([6, 3]).astype(np.float32)
        b = np.random.ranf([6, 4]).astype(np.float32)
        c = np.zeros([1, 4]).astype(np.float32)
        y = gemm_reference_implementation(a, b, c, transA=1)
        expect(node, inputs=[a, b, c], outputs=[y],
               name='test_gemm_transposeA')

    @staticmethod
    def export_transposeB():  # type: () -> None
        node = onnx.helper.make_node(
            'Gemm',
            inputs=['a', 'b', 'c'],
            outputs=['y'],
            transB=1
        )
        a = np.random.ranf([3, 6]).astype(np.float32)
        b = np.random.ranf([4, 6]).astype(np.float32)
        c = np.zeros([1, 4]).astype(np.float32)
        y = gemm_reference_implementation(a, b, c, transB=1)
        expect(node, inputs=[a, b, c], outputs=[y],
               name='test_gemm_transposeB')

    @staticmethod
    def export_alpha():  # type: () -> None
        node = onnx.helper.make_node(
            'Gemm',
            inputs=['a', 'b', 'c'],
            outputs=['y'],
            alpha=0.5
        )
        a = np.random.ranf([3, 5]).astype(np.float32)
        b = np.random.ranf([5, 4]).astype(np.float32)
        c = np.zeros([1, 4]).astype(np.float32)
        y = gemm_reference_implementation(a, b, c, alpha=0.5)
        expect(node, inputs=[a, b, c], outputs=[y],
               name='test_gemm_alpha')

    @staticmethod
    def export_beta():  # type: () -> None
        node = onnx.helper.make_node(
            'Gemm',
            inputs=['a', 'b', 'c'],
            outputs=['y'],
            beta=0.5
        )
        a = np.random.ranf([2, 7]).astype(np.float32)
        b = np.random.ranf([7, 4]).astype(np.float32)
        c = np.random.ranf([1, 4]).astype(np.float32)
        y = gemm_reference_implementation(a, b, c, beta=0.5)
        expect(node, inputs=[a, b, c], outputs=[y],
               name='test_gemm_beta')

    @staticmethod
    def export_all_attributes():  # type: () -> None
        node = onnx.helper.make_node(
            'Gemm',
            inputs=['a', 'b', 'c'],
            outputs=['y'],
            alpha=0.25,
            beta=0.35,
            transA=1,
            transB=1
        )
        a = np.random.ranf([4, 3]).astype(np.float32)
        b = np.random.ranf([5, 4]).astype(np.float32)
        c = np.random.ranf([1, 5]).astype(np.float32)
        y = gemm_reference_implementation(a, b, c, transA=1, transB=1, alpha=0.25, beta=0.35)
        expect(node, inputs=[a, b, c], outputs=[y],
               name='test_gemm_all_attributes')
