#!/usr/bin/env bash

./scripts/wait-for-it.sh -q db:3307 -- ./scripts/start_server.sh
