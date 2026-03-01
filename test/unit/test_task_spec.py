# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import pytest
from pydantic import ValidationError

from digitalhub_runtime_openinference.entities.task.build.spec import (
    TaskSpecOpeninferenceBuild,
    TaskValidatorOpeninferenceBuild,
)
from digitalhub_runtime_openinference.entities.task.serve.spec import (
    TaskSpecOpeninferenceServe,
    TaskValidatorOpeninferenceServe,
)

FUNCTION_REF = "store://projects/my-project/functions/openinference/my-fn:v1"


class TestTaskSpecOpeninferenceBuild:
    """Unit tests for TaskSpecOpeninferenceBuild."""

    def test_function_ref_stored(self):
        spec = TaskSpecOpeninferenceBuild(function=FUNCTION_REF)
        assert spec.function == FUNCTION_REF

    def test_instructions_defaults_to_none(self):
        spec = TaskSpecOpeninferenceBuild(function=FUNCTION_REF)
        assert spec.instructions is None

    def test_instructions_set(self):
        instructions = ["pip install torch", "pip install numpy"]
        spec = TaskSpecOpeninferenceBuild(function=FUNCTION_REF, instructions=instructions)
        assert spec.instructions == instructions

    def test_optional_fields_default_to_none(self):
        spec = TaskSpecOpeninferenceBuild(function=FUNCTION_REF)
        assert spec.volumes is None
        assert spec.resources is None
        assert spec.envs is None
        assert spec.secrets is None
        assert spec.profile is None


class TestTaskValidatorOpeninferenceBuild:
    """Unit tests for TaskValidatorOpeninferenceBuild Pydantic validator."""

    def test_valid_minimal(self):
        v = TaskValidatorOpeninferenceBuild(function=FUNCTION_REF)
        assert v.function == FUNCTION_REF
        assert v.instructions is None

    def test_instructions_accepted(self):
        v = TaskValidatorOpeninferenceBuild(function=FUNCTION_REF, instructions=["apt-get update"])
        assert v.instructions == ["apt-get update"]

    def test_instructions_must_be_list_of_strings(self):
        with pytest.raises(ValidationError):
            TaskValidatorOpeninferenceBuild(function=FUNCTION_REF, instructions=[1, 2, 3])


class TestTaskSpecOpeninferenceServe:
    """Unit tests for TaskSpecOpeninferenceServe."""

    def test_function_ref_stored(self):
        spec = TaskSpecOpeninferenceServe(function=FUNCTION_REF)
        assert spec.function == FUNCTION_REF

    def test_optional_fields_default_to_none(self):
        spec = TaskSpecOpeninferenceServe(function=FUNCTION_REF)
        assert spec.replicas is None
        assert spec.service_type is None
        assert spec.service_name is None

    def test_replicas_set(self):
        spec = TaskSpecOpeninferenceServe(function=FUNCTION_REF, replicas=3)
        assert spec.replicas == 3

    def test_service_type_set(self):
        spec = TaskSpecOpeninferenceServe(function=FUNCTION_REF, service_type="NodePort")
        assert spec.service_type == "NodePort"

    def test_service_name_set(self):
        spec = TaskSpecOpeninferenceServe(function=FUNCTION_REF, service_name="my-svc")
        assert spec.service_name == "my-svc"


class TestTaskValidatorOpeninferenceServe:
    """Unit tests for TaskValidatorOpeninferenceServe Pydantic validator."""

    def test_valid_minimal(self):
        v = TaskValidatorOpeninferenceServe(function=FUNCTION_REF)
        assert v.function == FUNCTION_REF
        assert v.replicas is None
        assert v.service_type is None
        assert v.service_name is None

    def test_replicas_accepted(self):
        v = TaskValidatorOpeninferenceServe(function=FUNCTION_REF, replicas=2)
        assert v.replicas == 2

    def test_replicas_must_be_at_least_one(self):
        with pytest.raises(ValidationError):
            TaskValidatorOpeninferenceServe(function=FUNCTION_REF, replicas=0)

    def test_negative_replicas_raises(self):
        with pytest.raises(ValidationError):
            TaskValidatorOpeninferenceServe(function=FUNCTION_REF, replicas=-1)

    def test_service_name_accepted(self):
        v = TaskValidatorOpeninferenceServe(function=FUNCTION_REF, service_name="inference-svc")
        assert v.service_name == "inference-svc"
