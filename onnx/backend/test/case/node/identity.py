# SPDX-License-Identifier: Apache-2.0

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import numpy as np

import onnx
from ..base import Base
from . import expect


class Identity(Base):

    @staticmethod
    def export():  # type: () -> None
        node = onnx.helper.make_node(
            'Identity',
            inputs=['x'],
            outputs=['y'],
        )

        data = np.array([[[
            [1, 2],
            [3, 4],
        ]]], dtype=np.float32)

        expect(node, inputs=[data], outputs=[data],
               name='test_identity')

    @staticmethod
    def export_sequence():  # type: () -> None
        node = onnx.helper.make_node(
            'Identity',
            inputs=['x'],
            outputs=['y'],
        )

        data = [
            np.array([[[
                [1, 2],
                [3, 4],
            ]]], dtype=np.float32),
            np.array([[[
                [2, 3],
                [1, 5],
            ]]], dtype=np.float32)]

        expect(node, inputs=[data], outputs=[data], name='test_identity_sequence')

    @staticmethod
    def export_identity_opt():  # type: () -> None
        ten_in_tp = onnx.helper.make_tensor_type_proto(onnx.TensorProto.FLOAT, shape=[5])
        seq_in_tp = onnx.helper.make_sequence_type_proto(ten_in_tp)
        opt_in_tp = onnx.helper.make_optional_type_proto(seq_in_tp)

        identity_node = onnx.helper.make_node(
            'Identity',
            inputs=['opt_in'],
            outputs=['opt_out']
        )

        x = [np.array([1, 2, 3, 4, 5]).astype(np.float32)]

        expect(identity_node, inputs=[x], outputs=[x], name='test_identity_opt',
               opset_imports=[onnx.helper.make_opsetid("", 16)],
               input_type_protos=[opt_in_tp],
               output_type_protos=[opt_in_tp])
