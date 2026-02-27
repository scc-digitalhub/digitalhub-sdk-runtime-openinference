# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.runtimes.builder import RuntimeBuilder

from digitalhub_runtime_openinference.runtimes.runtime import RuntimeOpeninference


class RuntimeOpeninferenceBuilder(RuntimeBuilder):
    """RuntimeOpeninferenceBuilder class."""

    RUNTIME_CLASS = RuntimeOpeninference
