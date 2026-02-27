# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0
from digitalhub_runtime_openinference.entities._commons.enums import EntityKinds
from digitalhub_runtime_openinference.entities.function.openinference.builder import FunctionOpeninferenceBuilder
from digitalhub_runtime_openinference.entities.run.serve.builder import RunOpeninferenceRunServeBuilder
from digitalhub_runtime_openinference.entities.task.serve.builder import TaskOpeninferenceServeBuilder

entity_builders = (
    (EntityKinds.FUNCTION_OPENINFERENCE.value, FunctionOpeninferenceBuilder),
    (EntityKinds.TASK_OPENINFERENCE_SERVE.value, TaskOpeninferenceServeBuilder),
    (EntityKinds.RUN_OPENINFERENCE_SERVE.value, RunOpeninferenceRunServeBuilder),
)

try:
    from digitalhub_runtime_openinference.runtimes.builder import RuntimeOpeninferenceBuilder

    runtime_builders = ((kind, RuntimeOpeninferenceBuilder) for kind in [e.value for e in EntityKinds])
except ImportError:
    runtime_builders = tuple()
