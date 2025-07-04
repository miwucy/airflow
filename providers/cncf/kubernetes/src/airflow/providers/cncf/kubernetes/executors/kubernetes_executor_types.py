# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
from __future__ import annotations

from typing import TYPE_CHECKING, Any

ADOPTED = "adopted"
if TYPE_CHECKING:
    from collections.abc import Sequence

    from airflow.models.taskinstance import TaskInstanceKey
    from airflow.utils.state import TaskInstanceState

    # TODO: Remove after Airflow 2 support is removed
    CommandType = Sequence[str]

    # TaskInstance key, command, configuration, pod_template_file
    KubernetesJobType = tuple[TaskInstanceKey, CommandType, Any, str | None]

    # key, pod state, pod_name, namespace, resource_version
    KubernetesResultsType = tuple[TaskInstanceKey, TaskInstanceState | str | None, str, str, str]

    # pod_name, namespace, pod state, annotations, resource_version
    KubernetesWatchType = tuple[str, str, TaskInstanceState | str | None, dict[str, str], str]

ALL_NAMESPACES = "ALL_NAMESPACES"
POD_EXECUTOR_DONE_KEY = "airflow_executor_done"

POD_REVOKED_KEY = "airflow_pod_revoked"
"""Label to indicate pod revoked by executor.

When executor the executor revokes a task, the pod deletion is the result of
the revocation.  So we don't want it to process that as an external deletion.
So we want events on a revoked pod to be ignored.

:meta private:
"""
