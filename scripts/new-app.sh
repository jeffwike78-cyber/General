#!/usr/bin/env bash
# Scaffold a new app folder from the launch-kit templates.
# Usage: scripts/new-app.sh <slug> ["Display Name"] [company-id] [support-email]
# Example: scripts/new-app.sh habit-forge "Habit Forge" mystudio support@mystudio.com
set -euo pipefail

SLUG="${1:?Usage: scripts/new-app.sh <slug> [\"Display Name\"] [company-id] [support-email]}"
if [[ ! "$SLUG" =~ ^[a-z0-9][a-z0-9-]*$ ]]; then
  echo "Slug must be lowercase letters, numbers and dashes (e.g. habit-forge)" >&2; exit 1
fi
NAME="${2:-$SLUG}"
COMPANY="${3:-yourcompany}"
EMAIL="${4:-support@yourdomain.com}"

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SRC="$ROOT/app-store-kit/templates"
DEST="$ROOT/apps/$SLUG"
[[ -e "$DEST" ]] && { echo "apps/$SLUG already exists — not overwriting." >&2; exit 1; }

mkdir -p "$DEST"
cp -R "$SRC/." "$DEST/"
cp "$ROOT/app-store-kit/checklists/submission-checklist.md" "$DEST/"
mkdir -p "$DEST/screenshots"

# Bundle IDs can't contain dashes in some tools; use the slug without dashes there.
BUNDLE_SLUG="${SLUG//-/}"
TODAY="$(date +%Y-%m-%d)"
find "$DEST" -type f \( -name '*.md' -o -name 'Appfile' \) -print0 | while IFS= read -r -d '' f; do
  sed -i.bak \
    -e "s|{{APP_NAME}}|$NAME|g" \
    -e "s|com.{{COMPANY}}.{{SLUG}}|com.$COMPANY.$BUNDLE_SLUG|g" \
    -e "s|{{COMPANY}}|$COMPANY|g" \
    -e "s|{{SLUG}}|$SLUG|g" \
    -e "s|{{SUPPORT_EMAIL}}|$EMAIL|g" \
    -e "s|{{DATE}}|$TODAY|g" "$f"
  rm -f "$f.bak"
done

echo "Created apps/$SLUG"
echo "Next: fill in apps/$SLUG/app-brief.md, then build the app."
