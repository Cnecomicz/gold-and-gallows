#!/bin/bash
set -euo pipefail

pytest --cov=Python/src Python/tests --cov-report html
