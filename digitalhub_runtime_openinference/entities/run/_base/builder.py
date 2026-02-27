# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities.run._base.builder import RunBuilder

from digitalhub_runtime_openinference.entities._base.runtime_entity.builder import RuntimeEntityBuilderOpeninference
from digitalhub_runtime_openinference.entities._commons.enums import EntityKinds
from digitalhub_runtime_openinference.entities.run._base.entity import RunOpeninferenceRun
from digitalhub_runtime_openinference.entities.run._base.spec import RunSpecOpeninferenceRun, RunValidatorOpeninferenceRun
from digitalhub_runtime_openinference.entities.run._base.status import RunStatusOpeninferenceRun


class RunOpeninferenceRunBuilder(RunBuilder, RuntimeEntityBuilderOpeninference):
    """
    RunOpeninferenceRunBuilder runer.
    """

    ENTITY_CLASS = RunOpeninferenceRun
    ENTITY_SPEC_CLASS = RunSpecOpeninferenceRun
    ENTITY_SPEC_VALIDATOR = RunValidatorOpeninferenceRun
    ENTITY_STATUS_CLASS = RunStatusOpeninferenceRun
    ENTITY_KIND = EntityKinds.RUN_OPENINFERENCE.value
