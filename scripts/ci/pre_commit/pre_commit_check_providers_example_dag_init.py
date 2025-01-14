#!/usr/bin/env python3
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

import os
import sys
from glob import glob
from typing import List

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, os.pardir))


def check_example_dags_dir_init_file(example_dags_dirs: List[str]) -> None:
    missing_init_dirs = []
    for example_dags_dir in example_dags_dirs:
        if not os.path.exists(example_dags_dir + "__init__.py"):
            missing_init_dirs.append(example_dags_dir)

    if missing_init_dirs:
        with open(os.path.join(ROOT_DIR, "license-templates/LICENSE.txt")) as license:
            license_txt = license.readlines()
        prefixed_licensed_txt = [f"# {line}" if line != "\n" else "#\n" for line in license_txt]

        for missing_init_dir in missing_init_dirs:
            with open(missing_init_dir + "__init__.py", "w") as init_file:
                init_file.write("".join(prefixed_licensed_txt))

        print("No __init__.py file was found in the following provider example_dags directories:")
        print("\n".join(missing_init_dirs))
        print("\nThe missing __init__.py files have been created. Please add these new files to a commit.")
        sys.exit(1)


if __name__ == "__main__":
    all_provider_example_dags_dirs = sorted(
        glob(f"{ROOT_DIR}/airflow/providers/**/example_dags/", recursive=True)
    )
    check_example_dags_dir_init_file(all_provider_example_dags_dirs)
