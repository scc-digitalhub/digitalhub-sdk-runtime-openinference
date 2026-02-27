# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import typing

from digitalhub.entities.task._base.entity import Task

if typing.TYPE_CHECKING:
    from digitalhub_runtime_openinference.entities.task.serve.spec import TaskSpecOpeninferenceServe
    from digitalhub_runtime_openinference.entities.task.serve.status import TaskStatusOpeninferenceServe


class TaskOpeninferenceServe(Task):
    """
    TaskOpeninferenceServe class.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.spec: TaskSpecOpeninferenceServe
        self.status: TaskStatusOpeninferenceServe
