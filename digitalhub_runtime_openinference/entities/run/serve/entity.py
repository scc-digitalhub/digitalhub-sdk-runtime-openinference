# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import typing

from digitalhub_runtime_openinference.entities.run._base.entity import RunOpeninferenceRun

if typing.TYPE_CHECKING:
    from digitalhub_runtime_openinference.entities.run.serve.spec import RunSpecOpeninferenceRunServe
    from digitalhub_runtime_openinference.entities.run.serve.status import RunStatusOpeninferenceRunServe


class RunOpeninferenceRunServe(RunOpeninferenceRun):
    """
    RunOpeninferenceRunServe class.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.spec: RunSpecOpeninferenceRunServe
        self.status: RunStatusOpeninferenceRunServe