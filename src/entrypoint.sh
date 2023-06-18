#!/bin/bash

case "$MODE" in
"lint")
    black . --check && flake8 .
    ;;
"dev")
    gunicorn core.main:app --reload
    ;;
"migrate")
    alembic upgrade head && touch /migrations_done
    sleep infinity
    ;;
"prod")
    gunicorn core.main:app
    ;;
*)
    echo "NO MODE SPECIFIED!"
    exit 1
    ;;
esac
