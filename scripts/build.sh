#!/bin/sh
# Build the site with GitHub Pages' own Jekyll (github-pages gem) in Docker.
# Usage: scripts/build.sh [SRC_DIR]     default SRC_DIR: the repository root
# Output goes to SRC_DIR/_site. Gems are cached between runs.
set -eu
SRC=$(cd "${1:-$(dirname "$0")/..}" && pwd)
GEMS="${XDG_CACHE_HOME:-$HOME/.cache}/personal-web-gems"
mkdir -p "$GEMS"
exec docker run --rm --network host --user "$(id -u):$(id -g)" -e HOME=/tmp -e BUNDLE_PATH=/gems \
  -v "$GEMS:/gems" -v "$SRC:/srv/site" -w /srv/site ruby:3.3 \
  sh -c 'bundle install --quiet && bundle exec jekyll build'
