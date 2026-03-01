# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

from digitalhub_runtime_openinference.entities.run._base.spec import (
    RunSpecOpeninferenceRun,
    RunValidatorOpeninferenceRun,
)

TASK_REF = "openinference+serve://projects/my-project/functions/openinference/my-fn:v1"


class TestRunSpecOpeninferenceRun:
    """Unit tests for RunSpecOpeninferenceRun."""

    def test_task_stored(self):
        spec = RunSpecOpeninferenceRun(task=TASK_REF)
        assert spec.task == TASK_REF

    def test_optional_fields_default_to_none(self):
        spec = RunSpecOpeninferenceRun(task=TASK_REF)
        assert spec.function is None
        assert spec.source is None
        assert spec.image is None
        assert spec.base_image is None
        assert spec.python_version is None
        assert spec.requirements is None
        assert spec.service_type is None
        assert spec.service_name is None
        assert spec.replicas is None
        assert spec.instructions is None
        assert spec.inputs is None
        assert spec.parameters is None
        assert spec.init_parameters is None

    def test_source_set(self):
        src = {"source": "src/handler.py", "handler": "predict"}
        spec = RunSpecOpeninferenceRun(task=TASK_REF, source=src)
        assert spec.source == src

    def test_image_set(self):
        spec = RunSpecOpeninferenceRun(task=TASK_REF, image="myimage:1.0")
        assert spec.image == "myimage:1.0"

    def test_requirements_set(self):
        reqs = ["numpy", "torch"]
        spec = RunSpecOpeninferenceRun(task=TASK_REF, requirements=reqs)
        assert spec.requirements == reqs

    def test_replicas_set(self):
        spec = RunSpecOpeninferenceRun(task=TASK_REF, replicas=5)
        assert spec.replicas == 5

    def test_inputs_set(self):
        inputs = {"input0": "store://projects/p/dataitems/d:v0"}
        spec = RunSpecOpeninferenceRun(task=TASK_REF, inputs=inputs)
        assert spec.inputs == inputs

    def test_parameters_set(self):
        params = {"threshold": 0.5, "batch_size": 32}
        spec = RunSpecOpeninferenceRun(task=TASK_REF, parameters=params)
        assert spec.parameters == params

    def test_init_parameters_set(self):
        init_params = {"model_path": "/models/v1"}
        spec = RunSpecOpeninferenceRun(task=TASK_REF, init_parameters=init_params)
        assert spec.init_parameters == init_params

    def test_instructions_set(self):
        spec = RunSpecOpeninferenceRun(task=TASK_REF, instructions={"step": "build"})
        assert spec.instructions == {"step": "build"}


class TestRunValidatorOpeninferenceRun:
    """Unit tests for RunValidatorOpeninferenceRun Pydantic validator."""

    def test_valid_minimal(self):
        v = RunValidatorOpeninferenceRun(task=TASK_REF)
        assert v.task == TASK_REF

    def test_optional_fields_default_to_none(self):
        v = RunValidatorOpeninferenceRun(task=TASK_REF)
        assert v.source is None
        assert v.image is None
        assert v.base_image is None
        assert v.python_version is None
        assert v.requirements is None
        assert v.service_type is None
        assert v.service_name is None
        assert v.replicas is None
        assert v.instructions is None
        assert v.inputs is None
        assert v.parameters is None
        assert v.init_parameters is None

    def test_image_accepted(self):
        v = RunValidatorOpeninferenceRun(task=TASK_REF, image="myimage:2.0")
        assert v.image == "myimage:2.0"

    def test_requirements_accepted(self):
        v = RunValidatorOpeninferenceRun(task=TASK_REF, requirements=["scikit-learn"])
        assert v.requirements == ["scikit-learn"]

    def test_replicas_accepted(self):
        v = RunValidatorOpeninferenceRun(task=TASK_REF, replicas=3)
        assert v.replicas == 3
