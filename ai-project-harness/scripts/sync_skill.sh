#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
NAME="ai-project-harness"

CODEX_DIR="${CODEX_HOME:-$HOME/.codex}/skills/${NAME}"
CLAUDE_DIR="${CLAUDE_HOME:-$HOME/.claude}/skills/${NAME}"

sync_to() {
  local target="$1"
  rm -rf "$target"
  mkdir -p "$(dirname "$target")"
  cp -R "$ROOT" "$target"
  chmod +x "$target/scripts/"*.py "$target/scripts/"*.sh 2>/dev/null || true
  echo "synced -> $target"
}

sync_to "$CODEX_DIR"
sync_to "$CLAUDE_DIR"
