# Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# Licensed under the Apache License, Version 2.0 https://aws.amazon.com/apache-2-0/

from api.state_table_dynamodb import StateTableDDB


def state_table_manager(state_table_service, state_table_config, tasks_state_table_name, region=None):

    state_table_config = state_table_config.replace("'", "\"")

    if state_table_service == "DynamoDB":
        return StateTableDDB(state_table_config, tasks_state_table_name, region)

    else:
        raise NotImplementedError()
