#!/usr/bin/env bash

flask db upgrade
uwsgi app.ini