# -*- coding: utf-8 -*-
# Copyright (C) 2018-2024 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

"""Factory functions for ops added to openvino opset16."""
from functools import partial

from openvino.runtime.opset_utils import _get_node_factory

_get_node_factory_opset16 = partial(_get_node_factory, "opset16")

# -------------------------------------------- ops ------------------------------------------------
