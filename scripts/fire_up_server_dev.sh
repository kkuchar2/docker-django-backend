#!/usr/bin/env bash

./scripts/wait-for-it.sh -q db:3306 -- ./scripts/start_server.sh
