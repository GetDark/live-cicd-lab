#!/usr/bin/env bash
# Called by GitHub Actions deploy job via SSH
set -euo pipefail

IMAGE="${1:-live-cicd-lab:latest}"
SHA="${2:-local}"
NOW=$(date '+%Y-%m-%d %H:%M')

cd /root/live-cicd-lab

sed -i "s|^LAST_DEPLOY=.*|LAST_DEPLOY=${NOW}|" .env
sed -i "s|^CURRENT_IMAGE=.*|CURRENT_IMAGE=${IMAGE}|" .env
sed -i "s|^GIT_SHA=.*|GIT_SHA=${SHA}|" .env

APP_IMAGE="${IMAGE}" docker compose pull app 2>/dev/null || true
APP_IMAGE="${IMAGE}" docker compose up -d --no-deps app
