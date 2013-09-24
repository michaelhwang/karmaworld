#!/usr/bin/env python
# -*- coding:utf8 -*-
# Copyright (C) 2012  FinalsClub Foundation
""" Dummy S3 bucket conf. file (for pushing static files """

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_ACCESS_KEY_ID = 'access_id'
AWS_SECRET_ACCESS_KEY = 'access_key'
AWS_STORAGE_BUCKET_NAME = 'bucket'
S3_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
STATIC_URL = S3_URL