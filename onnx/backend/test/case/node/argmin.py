# SPDX-License-Identifier: Apache-2.0

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import numpy as np

import onnx
from ..base import Base
from . import expect


def argmin_use_numpy(data, axis=0, keepdims=1):  # type: (np.ndarray, int, int) -> (np.ndarray)
    result = np.argmin(data, axis=axis)
    if (keepdims == 1):
        result = np.expand_dims(result, axis)
    return result.astype(np.int64)


def argmin_use_numpy_select_last_index(data, axis=0, keepdims=True):  # type: (np.ndarray, int, int) -> (np.ndarray)
    data = np.flip(data, axis)
    result = np.argmin(data, axis=axis)
    result = data.shape[axis] - result - 1
    if keepdims:
        result = np.expand_dims(result, axis)
    return result.astype(np.int64)


class ArgMin(Base):

    @staticmethod
    def export_no_keepdims():  # type: () -> None
        data = np.array([[2, 1], [3, 10]], dtype=np.float32)
        axis = 1
        keepdims = 0
        node = onnx.helper.make_node(
            'ArgMin',
            inputs=['data'],
            outputs=['result'],
            axis=axis,
            keepdims=keepdims)
        # The content of result is : [[1, 0]]
        result = argmin_use_numpy(data, axis=axis, keepdims=keepdims)
        expect(node, inputs=[data], outputs=[result], name='test_argmin_no_keepdims_example')

        data = np.random.uniform(-10, 10, [2, 3, 4]).astype(np.float32)
        # result's shape: [2, 4]
        result = argmin_use_numpy(data, axis=axis, keepdims=keepdims)
        expect(node, inputs=[data], outputs=[result], name='test_argmin_no_keepdims_random')

    @staticmethod
    def export_keepdims():  # type: () -> None
        data = np.array([[2, 1], [3, 10]], dtype=np.float32)
        axis = 1
        keepdims = 1
        node = onnx.helper.make_node(
            'ArgMin',
            inputs=['data'],
            outputs=['result'],
            axis=axis,
            keepdims=keepdims)
        # The content of result is : [[1], [0]]
        result = argmin_use_numpy(data, axis=axis, keepdims=keepdims)
        expect(node, inputs=[data], outputs=[result], name='test_argmin_keepdims_example')

        data = np.random.uniform(-10, 10, [2, 3, 4]).astype(np.float32)
        # result's shape: [2, 1, 4]
        result = argmin_use_numpy(data, axis=axis, keepdims=keepdims)
        expect(node, inputs=[data], outputs=[result], name='test_argmin_keepdims_random')

    @staticmethod
    def export_default_axes_keepdims():  # type: () -> None
        data = np.array([[2, 1], [3, 10]], dtype=np.float32)
        keepdims = 1
        node = onnx.helper.make_node(
            'ArgMin',
            inputs=['data'],
            outputs=['result'],
            keepdims=keepdims)

        # The content of result is : [[0], [0]]
        result = argmin_use_numpy(data, keepdims=keepdims)
        expect(node, inputs=[data], outputs=[result], name='test_argmin_default_axis_example')

        data = np.random.uniform(-10, 10, [2, 3, 4]).astype(np.float32)
        # result's shape: [1, 3, 4]
        result = argmin_use_numpy(data, keepdims=keepdims)
        expect(node, inputs=[data], outputs=[result], name='test_argmin_default_axis_random')

    @staticmethod
    def export_negative_axis_keepdims():  # type: () -> None
        data = np.array([[2, 1], [3, 10]], dtype=np.float32)
        axis = -1
        keepdims = 1
        node = onnx.helper.make_node(
            'ArgMin',
            inputs=['data'],
            outputs=['result'],
            axis=axis,
            keepdims=keepdims)
        # The content of result is : [[1], [0]]
        result = argmin_use_numpy(data, axis=axis, keepdims=keepdims)
        expect(node, inputs=[data], outputs=[result], name='test_argmin_negative_axis_keepdims_example')

        data = np.random.uniform(-10, 10, [2, 3, 4]).astype(np.float32)
        # result's shape: [2, 3, 1]
        result = argmin_use_numpy(data, axis=axis, keepdims=keepdims)
        expect(node, inputs=[data], outputs=[result], name='test_argmin_negative_axis_keepdims_random')

    @staticmethod
    def export_no_keepdims_select_last_index():  # type: () -> None
        data = np.array([[2, 2], [3, 10]], dtype=np.float32)
        axis = 1
        keepdims = 0
        node = onnx.helper.make_node(
            'ArgMin',
            inputs=['data'],
            outputs=['result'],
            axis=axis,
            keepdims=keepdims,
            select_last_index=True)
        # result: [[1, 0]]
        result = argmin_use_numpy_select_last_index(data, axis=axis, keepdims=keepdims)
        expect(node, inputs=[data], outputs=[result], name='test_argmin_no_keepdims_example_select_last_index')

        data = np.random.uniform(-10, 10, [2, 3, 4]).astype(np.float32)
        # result's shape: [2, 4]
        result = argmin_use_numpy_select_last_index(data, axis=axis, keepdims=keepdims)
        expect(node, inputs=[data], outputs=[result], name='test_argmin_no_keepdims_random_select_last_index')

    @staticmethod
    def export_keepdims_select_last_index():  # type: () -> None
        data = np.array([[2, 2], [3, 10]], dtype=np.float32)
        axis = 1
        keepdims = 1
        node = onnx.helper.make_node(
            'ArgMin',
            inputs=['data'],
            outputs=['result'],
            axis=axis,
            keepdims=keepdims,
            select_last_index=True)
        # result: [[1], [0]]
        result = argmin_use_numpy_select_last_index(data, axis=axis, keepdims=keepdims)
        expect(node, inputs=[data], outputs=[result], name='test_argmin_keepdims_example_select_last_index')

        data = np.random.uniform(-10, 10, [2, 3, 4]).astype(np.float32)
        # result's shape: [2, 1, 4]
        result = argmin_use_numpy_select_last_index(data, axis=axis, keepdims=keepdims)
        expect(node, inputs=[data], outputs=[result], name='test_argmin_keepdims_random_select_last_index')

    @staticmethod
    def export_default_axes_keepdims_select_last_index():  # type: () -> None
        data = np.array([[2, 2], [3, 10]], dtype=np.float32)
        keepdims = 1
        node = onnx.helper.make_node(
            'ArgMin',
            inputs=['data'],
            outputs=['result'],
            keepdims=keepdims,
            select_last_index=True)

        # result: [[0, 0]]
        result = argmin_use_numpy_select_last_index(data, keepdims=keepdims)
        expect(node, inputs=[data], outputs=[result], name='test_argmin_default_axis_example_select_last_index')

        data = np.random.uniform(-10, 10, [2, 3, 4]).astype(np.float32)
        # result's shape: [1, 3, 4]
        result = argmin_use_numpy_select_last_index(data, keepdims=keepdims)
        expect(node, inputs=[data], outputs=[result], name='test_argmin_default_axis_random_select_last_index')

    @staticmethod
    def export_negative_axis_keepdims_select_last_index():  # type: () -> None
        data = np.array([[2, 2], [3, 10]], dtype=np.float32)
        axis = -1
        keepdims = 1
        node = onnx.helper.make_node(
            'ArgMin',
            inputs=['data'],
            outputs=['result'],
            axis=axis,
            keepdims=keepdims,
            select_last_index=True)
        # result: [[1], [0]]
        result = argmin_use_numpy_select_last_index(data, axis=axis, keepdims=keepdims)
        expect(node, inputs=[data], outputs=[result], name='test_argmin_negative_axis_keepdims_example_select_last_index')

        data = np.random.uniform(-10, 10, [2, 3, 4]).astype(np.float32)
        # result's shape: [2, 3, 1]
        result = argmin_use_numpy_select_last_index(data, axis=axis, keepdims=keepdims)
        expect(node, inputs=[data], outputs=[result], name='test_argmin_negative_axis_keepdims_random_select_last_index')
