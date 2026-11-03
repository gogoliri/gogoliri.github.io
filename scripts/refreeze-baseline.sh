#!/bin/sh
# Rebuild the site and make it the tests' baseline: copy the pages the tests
# compare (Home, CV, every paper page) into tests/baseline/.
# Run after an intentional change to what a page shows, then review
# `git diff tests/baseline` and commit it with the change.
set -eu
ROOT=$(cd "$(dirname "$0")/.." && pwd)
"$ROOT/scripts/build.sh"
B="$ROOT/tests/baseline"
rm -rf "$B"
mkdir -p "$B/cv" "$B/papers"
cp "$ROOT/_site/index.html" "$B/index.html"
cp "$ROOT/_site/cv/index.html" "$B/cv/index.html"
for f in "$ROOT"/_papers/*.md; do
  slug=$(basename "$f" .md)
  cp "$ROOT/_site/papers/$slug.html" "$B/papers/$slug.html"
done
echo "Baseline refrozen: $(find "$B" -type f | wc -l) pages in tests/baseline/"
