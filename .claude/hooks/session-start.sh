#!/bin/bash
# Installs project dependencies into .venv for Claude Code cloud sessions,
# so that `make lint` and `make test` work out of the box.
set -euo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

cd "${CLAUDE_PROJECT_DIR:-$(dirname "$0")/../..}"

PYTHON_VERSION="3.14"
VENV_DIR="$PWD/.venv"

if command -v uv >/dev/null 2>&1; then
  if [ ! -x "$VENV_DIR/bin/python" ]; then
    uv venv --python "$PYTHON_VERSION" "$VENV_DIR"
  fi
  VIRTUAL_ENV="$VENV_DIR" uv pip install -r requirements.txt -r resuirements.dev.txt
else
  if [ ! -x "$VENV_DIR/bin/python" ]; then
    "python$PYTHON_VERSION" -m venv "$VENV_DIR" 2>/dev/null || python3 -m venv "$VENV_DIR"
  fi
  "$VENV_DIR/bin/pip" install -r requirements.txt -r resuirements.dev.txt
fi

if [ -n "${CLAUDE_ENV_FILE:-}" ]; then
  echo "export VIRTUAL_ENV=\"$VENV_DIR\"" >> "$CLAUDE_ENV_FILE"
  echo "export PATH=\"$VENV_DIR/bin:\$PATH\"" >> "$CLAUDE_ENV_FILE"
fi
