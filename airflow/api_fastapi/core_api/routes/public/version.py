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

import airflow
from airflow.api_fastapi.common.router import AirflowRouter
from airflow.api_fastapi.core_api.datamodels.version import VersionInfo
from airflow.utils.platform import get_airflow_git_version

version_router = AirflowRouter(tags=["Version"], prefix="/version")


@version_router.get("")
def get_version() -> VersionInfo:
    """Get version information."""
    airflow_version = airflow.__version__
    git_version = get_airflow_git_version()
    version_info = VersionInfo(version=airflow_version, git_version=git_version)
    return version_info
