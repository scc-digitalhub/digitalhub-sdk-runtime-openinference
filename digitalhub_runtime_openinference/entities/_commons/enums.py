# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from enum import Enum


class EntityKinds(Enum):
    """
    Entity kinds.
    """

    FUNCTION_OPENINFERENCE = "openinference"
    TASK_OPENINFERENCE_BUILD = "openinference+build"
    TASK_OPENINFERENCE_SERVE = "openinference+serve"
    RUN_OPENINFERENCE_BUILD = "openinference+build:run"
    RUN_OPENINFERENCE_SERVE = "openinference+serve:run"


class Actions(Enum):
    """
    Task actions.
    """

    BUILD = "build"
    SERVE = "serve"
