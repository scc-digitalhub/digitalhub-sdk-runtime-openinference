# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import pytest

from digitalhub_runtime_openinference.runtimes.runtime import RuntimeOpeninference


class TestRuntimeOpeninference:
    """Unit tests for RuntimeOpeninference."""

    def _make_runtime(self) -> RuntimeOpeninference:
        return RuntimeOpeninference(project="test-project")

    def _make_run(self, task_kind: str) -> dict:
        return {"spec": {"task": f"{task_kind}://projects/p/functions/openinference/fn:v1"}}

    def test_run_raises_not_implemented_for_build(self):
        runtime = self._make_runtime()
        with pytest.raises(NotImplementedError, match="build"):
            runtime.run(self._make_run("openinference+build"))

    def test_run_raises_not_implemented_for_serve(self):
        runtime = self._make_runtime()
        with pytest.raises(NotImplementedError, match="serve"):
            runtime.run(self._make_run("openinference+serve"))

    def test_run_raises_not_implemented_for_arbitrary_kind(self):
        runtime = self._make_runtime()
        with pytest.raises(NotImplementedError):
            runtime.run(self._make_run("unknown-task"))

    def test_error_message_contains_task_kind(self):
        runtime = self._make_runtime()
        task_kind = "openinference+build"
        with pytest.raises(NotImplementedError) as exc_info:
            runtime.run(self._make_run(task_kind))
        assert task_kind in str(exc_info.value)
