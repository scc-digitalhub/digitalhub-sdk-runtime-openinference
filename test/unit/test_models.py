# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import pytest
from pydantic import ValidationError

from digitalhub_runtime_openinference.entities.function.openinference.models import (
    TensorDatatype,
    TensorValidator,
)


class TestTensorDatatype:
    """Unit tests for the TensorDatatype enum."""

    def test_all_values_present(self):
        expected = {
            "BOOL", "BYTES",
            "UINT8", "INT8",
            "UINT16", "INT16",
            "UINT32", "INT32",
            "UINT64", "INT64",
            "FP16", "FP32", "FP64",
        }
        actual = {member.value for member in TensorDatatype}
        assert actual == expected

    def test_access_by_name(self):
        assert TensorDatatype.BOOL.value == "BOOL"
        assert TensorDatatype.FP32.value == "FP32"
        assert TensorDatatype.INT64.value == "INT64"

    def test_access_by_value(self):
        assert TensorDatatype("BOOL") is TensorDatatype.BOOL
        assert TensorDatatype("FP64") is TensorDatatype.FP64

    def test_invalid_value_raises(self):
        with pytest.raises(ValueError):
            TensorDatatype("INVALID")


class TestTensorValidator:
    """Unit tests for the TensorValidator Pydantic model."""

    def test_default_values(self):
        tensor = TensorValidator(name="input")
        assert tensor.name == "input"
        assert tensor.shape == []
        assert tensor.datatype == TensorDatatype.FP32.value

    def test_explicit_values(self):
        tensor = TensorValidator(name="output", shape=[1, 3, 224, 224], datatype="INT32")
        assert tensor.name == "output"
        assert tensor.shape == [1, 3, 224, 224]
        assert tensor.datatype == "INT32"

    def test_all_datatypes_accepted(self):
        for dtype in TensorDatatype:
            tensor = TensorValidator(name="x", datatype=dtype.value)
            assert tensor.datatype == dtype.value

    def test_enum_instance_coerced_to_value(self):
        """use_enum_values=True means enum members are stored as their .value."""
        tensor = TensorValidator(name="x", datatype=TensorDatatype.FP16)
        assert tensor.datatype == "FP16"
        assert isinstance(tensor.datatype, str)

    def test_empty_shape_by_default(self):
        tensor = TensorValidator(name="t")
        assert tensor.shape == []

    def test_invalid_datatype_raises(self):
        with pytest.raises(ValidationError):
            TensorValidator(name="bad", datatype="NOT_A_TYPE")

    def test_shape_must_be_list_of_ints(self):
        with pytest.raises(ValidationError):
            TensorValidator(name="bad", shape=["a", "b"])

    def test_name_defaults_to_none(self):
        tensor = TensorValidator()
        assert tensor.name is None
