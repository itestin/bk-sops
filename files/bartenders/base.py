# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云PaaS平台社区版 (BlueKing PaaS Community
Edition) available.
Copyright (C) 2017 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at
http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""

from abc import ABCMeta, abstractmethod


class UploadRequestBartender(object, metaclass=ABCMeta):
    def __init__(self, manager):
        self.manager = manager

    @abstractmethod
    def process_request(self, request, *args, **kwargs):
        raise NotImplementedError()

    def post_handle_upload_process(self, data, *args, **kwargs):
        if getattr(self.manager, "record_uploaded_data"):
            getattr(self.manager, "record_uploaded_data")(data, *args, **kwargs)
