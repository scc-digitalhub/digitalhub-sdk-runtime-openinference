# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities._base.runtime_entity.builder import RuntimeEntityBuilder
from digitalhub.entities._commons.utils import map_actions

from digitalhub_runtime_openinference.entities._commons.enums import Actions, EntityKinds


class RuntimeEntityBuilderOpeninference(RuntimeEntityBuilder):
    EXECUTABLE_KIND = EntityKinds.FUNCTION_OPENINFERENCE.value
    TASKS_KINDS = map_actions(
        [
            (
                EntityKinds.TASK_OPENINFERENCE_BUILD.value,
                Actions.BUILD.value,
            ),
            (
                EntityKinds.TASK_OPENINFERENCE_SERVE.value,
                Actions.SERVE.value,
            ),
        ]
    )
    RUN_KINDS = map_actions(
        [
            (
                EntityKinds.RUN_OPENINFERENCE_BUILD.value,
                Actions.BUILD.value,
            ),
            (
                EntityKinds.RUN_OPENINFERENCE_SERVE.value,
                Actions.SERVE.value,
            ),
        ]
    )
