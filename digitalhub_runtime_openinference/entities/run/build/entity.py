# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import typing

from digitalhub_runtime_openinference.entities.run._base.entity import RunOpeninferenceRun

if typing.TYPE_CHECKING:
    from digitalhub.entities._base.entity.metadata import Metadata

    from digitalhub_runtime_openinference.entities.run.build.spec import RunSpecOpeninferenceRunBuild
    from digitalhub_runtime_openinference.entities.run.build.status import RunStatusOpeninferenceRunBuild


class RunOpeninferenceRunBuild(RunOpeninferenceRun):
    """
    RunOpeninferenceRunBuild class.
    """

    def __init__(
        self,
        project: str,
        uuid: str,
        kind: str,
        metadata: Metadata,
        spec: RunSpecOpeninferenceRunBuild,
        status: RunStatusOpeninferenceRunBuild,
        user: str | None = None,
    ) -> None:
        super().__init__(project, uuid, kind, metadata, spec, status, user)

        self.spec: RunSpecOpeninferenceRunBuild
        self.status: RunStatusOpeninferenceRunBuild
