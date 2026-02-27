# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import typing

from digitalhub.entities.task._base.entity import Task

if typing.TYPE_CHECKING:
    from digitalhub.entities._base.entity.metadata import Metadata

    from digitalhub_runtime_openinference.entities.task.build.spec import TaskSpecOpeninferenceBuild
    from digitalhub_runtime_openinference.entities.task.build.status import TaskStatusOpeninferenceBuild


class TaskOpeninferenceBuild(Task):
    """
    TaskOpeninferenceBuild class.
    """

    def __init__(
        self,
        project: str,
        uuid: str,
        kind: str,
        metadata: Metadata,
        spec: TaskSpecOpeninferenceBuild,
        status: TaskStatusOpeninferenceBuild,
        user: str | None = None,
    ) -> None:
        super().__init__(project, uuid, kind, metadata, spec, status, user)

        self.spec: TaskSpecOpeninferenceBuild
        self.status: TaskStatusOpeninferenceBuild
