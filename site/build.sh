#!/usr/bin/env bash
# Build the site from literature/.   site/build.sh          -> site/public/
#                                     site/build.sh --serve  -> also preview at http://localhost:8080/quant-alex/
set -euo pipefail
SITE="$(cd "$(dirname "$0")" && pwd)"
CONTENT="${CONTENT_DIR:-${TMPDIR:-/tmp}/quant-alex-site-content}"
python3 "$SITE/prepare_content.py" "$CONTENT"
cd "$SITE"
[ -d node_modules ] || npm ci
npx quartz build -d "$CONTENT"
cp home/index.html public/index.html          # the library map is the home page
if [ "${1:-}" = "--serve" ]; then
  python3 "$SITE/serve.py" "$SITE/public" "${PORT:-8080}"
fi
