# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import pytest
from pydantic import ValidationError

from digitalhub_runtime_openinference.entities.function.openinference.models import TensorValidator
from digitalhub_runtime_openinference.entities.function.openinference.spec import (
    FunctionSpecOpeninference,
    FunctionValidatorOpeninference,
)


class TestFunctionSpecOpeninference:
    """Unit tests for FunctionSpecOpeninference constructor and attributes."""

    def test_defaults_to_none(self):
        spec = FunctionSpecOpeninference()
        assert spec.image is None
        assert spec.base_image is None
        assert spec.python_version is None
        assert spec.requirements is None
        assert spec.source is None

    def test_image_set(self):
        spec = FunctionSpecOpeninference(image="my-registry/my-image:latest")
        assert spec.image == "my-registry/my-image:latest"

    def test_base_image_set(self):
        spec = FunctionSpecOpeninference(base_image="python:3.11-slim")
        assert spec.base_image == "python:3.11-slim"

    def test_python_version_set(self):
        spec = FunctionSpecOpeninference(python_version="PYTHON3_11")
        assert spec.python_version == "PYTHON3_11"

    def test_requirements_set(self):
        reqs = ["numpy>=1.24", "torch==2.0.0"]
        spec = FunctionSpecOpeninference(requirements=reqs)
        assert spec.requirements == reqs

    def test_source_set(self):
        src = {"source": "src/handler.py", "handler": "predict"}
        spec = FunctionSpecOpeninference(source=src)
        assert spec.source == src

    def test_all_params(self):
        spec = FunctionSpecOpeninference(
            source={"source": "src/main.py"},
            image="myimage:1.0",
            base_image="python:3.10",
            python_version="PYTHON3_10",
            requirements=["scikit-learn"],
        )
        assert spec.image == "myimage:1.0"
        assert spec.base_image == "python:3.10"
        assert spec.python_version == "PYTHON3_10"
        assert spec.requirements == ["scikit-learn"]
        assert spec.source == {"source": "src/main.py"}


class TestFunctionValidatorOpeninference:
    """Unit tests for FunctionValidatorOpeninference Pydantic validator."""

    _BASE_VALID = {
        "source": {"source": "src/handler.py", "handler": "predict"},
        "python_version": "PYTHON3_11",
    }

    def test_optional_fields_default_to_none(self):
        validator = FunctionValidatorOpeninference(**self._BASE_VALID)
        assert validator.image is None
        assert validator.base_image is None
        assert validator.requirements is None
        assert validator.model_name is None

    def test_inputs_outputs_default_to_empty_list(self):
        validator = FunctionValidatorOpeninference(**self._BASE_VALID)
        assert validator.inputs == []
        assert validator.outputs == []

    def test_with_image(self):
        data = {**self._BASE_VALID, "image": "myimage:latest"}
        validator = FunctionValidatorOpeninference(**data)
        assert validator.image == "myimage:latest"

    def test_with_requirements(self):
        data = {**self._BASE_VALID, "requirements": ["numpy", "pandas"]}
        validator = FunctionValidatorOpeninference(**data)
        assert validator.requirements == ["numpy", "pandas"]

    def test_with_model_name(self):
        data = {**self._BASE_VALID, "model_name": "my-model"}
        validator = FunctionValidatorOpeninference(**data)
        assert validator.model_name == "my-model"

    def test_with_tensor_inputs_outputs(self):
        tensor = {"name": "input0", "shape": [1, 3, 224, 224], "datatype": "FP32"}
        data = {
            **self._BASE_VALID,
            "inputs": [tensor],
            "outputs": [{"name": "output0", "shape": [1, 1000], "datatype": "FP32"}],
        }
        validator = FunctionValidatorOpeninference(**data)
        assert len(validator.inputs) == 1
        assert len(validator.outputs) == 1
        assert isinstance(validator.inputs[0], TensorValidator)
        assert validator.inputs[0].name == "input0"
        assert validator.inputs[0].shape == [1, 3, 224, 224]

    def test_invalid_python_version_raises(self):
        with pytest.raises(ValidationError):
            FunctionValidatorOpeninference(
                source={"source": "src/handler.py", "handler": "predict"},
                python_version="NOT_VALID",
            )
