#
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

"""Example DAG demonstrating the usage of the ShortCircuitOperator."""
from airflow import DAG
from airflow.models.baseoperator import chain
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import ShortCircuitOperator
from airflow.utils import dates

with DAG(
    dag_id='example_short_circuit_operator',
    start_date=dates.days_ago(2),
    tags=['example'],
) as dag:

    cond_true = ShortCircuitOperator(
        task_id='condition_is_True',
        python_callable=lambda: True,
    )

    cond_false = ShortCircuitOperator(
        task_id='condition_is_False',
        python_callable=lambda: False,
    )

    ds_true = [DummyOperator(task_id='true_' + str(i)) for i in [1, 2]]
    ds_false = [DummyOperator(task_id='false_' + str(i)) for i in [1, 2]]

    chain(cond_true, *ds_true)
    chain(cond_false, *ds_false)
