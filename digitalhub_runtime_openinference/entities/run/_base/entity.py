# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import time
import typing

from digitalhub.entities._commons.enums import State
from digitalhub.entities._commons.utils import get_entity_type_from_key
from digitalhub.entities.run._base.entity import Run
from digitalhub.factory.entity import entity_factory
from digitalhub.utils.logger import LOGGER

from digitalhub_runtime_openinference.entities._commons.enums import Actions
from digitalhub_runtime_openinference.entities.run._base.utils import get_getter_for_material

if typing.TYPE_CHECKING:
    from digitalhub_runtime_openinference.entities.run._base.spec import RunSpecOpeninferenceRun
    from digitalhub_runtime_openinference.entities.run._base.status import RunStatusOpeninferenceRun


class RunOpeninferenceRun(Run):
    """
    RunOpeninferenceRun class.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.spec: RunSpecOpeninferenceRun
        self.status: RunStatusOpeninferenceRun

    def _setup_execution(self) -> None:
        """
        Setup run execution.
        """
        self.refresh()

    def wait(self, log_info: bool = True) -> Run:
        """
        Wait for run to finish.

        Parameters
        ----------
        log_info : bool
            If True, log information.

        Returns
        -------
        Run
            Run object.
        """
        task_kind = self.spec.task.split("://")[0]
        action = entity_factory.get_action_from_task_kind(self.kind, task_kind)

        if action == Actions.SERVE.value:
            serve_timeout = 300
            start = time.time()

            while time.time() - start < serve_timeout:
                if log_info:
                    LOGGER.info(f"Waiting for run {self.id} to deploy service.")

                self.refresh()
                if self.status.service is not None:
                    if log_info:
                        msg = f"Run {self.id} service deployed."
                        LOGGER.info(msg)
                    return self

                elif self.status.state == State.ERROR.value:
                    if log_info:
                        msg = f"Run {self.id} serving failed."
                        LOGGER.info(msg)
                    return self

                time.sleep(5)

            if log_info:
                msg = f"Waiting for run {self.id} service timed out. Check logs for more information."
                LOGGER.info(msg)

            return self

        return super().wait(log_info=log_info)