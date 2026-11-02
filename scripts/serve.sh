#!/bin/sh
# Preview the site at http://localhost:4000 with GitHub Pages' own Jekyll.
# Host networking: the container serves straight on the host port, and it
# sidesteps a Docker bridge DNS failure seen on this machine.
# Rebuilds on save; restart after editing _config.yml. Ctrl-C to stop.
set -eu
SRC=$(cd "$(dirname "$0")/.." && pwd)
GEMS="${XDG_CACHE_HOME:-$HOME/.cache}/personal-web-gems"
mkdir -p "$GEMS"
TTY=""; [ -t 0 ] && TTY="-it"
exec docker run --rm $TTY --network host --user "$(id -u):$(id -g)" -e HOME=/tmp -e BUNDLE_PATH=/gems \
  -v "$GEMS:/gems" -v "$SRC:/srv/site" -w /srv/site ruby:3.3 \
  sh -c 'bundle install --quiet && bundle exec jekyll serve --host 0.0.0.0'
