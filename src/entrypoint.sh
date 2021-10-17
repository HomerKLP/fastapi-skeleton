#!/bin/bash
# No more than 100 lines of code
wait_for () {
    for _ in `seq 0 100`; do
        (echo > /dev/tcp/$1/$2) >/dev/null 2>&1
        if [[ $? -eq 0 ]]; then
            echo "$1:$2 accepts connections!"
            break
        fi
        sleep 1
    done
}
populate_env_variables () {
  if [ -f .env ]
  then
    export "$(cat .env | sed 's/#.*//g' | xargs)"
  fi
  echo "env variables are populated!"
}
populate_env_variables
case "$PROCESS" in
"LINT")
    black . --check && flake8 .
    ;;
"DEV")
    aerich upgrade
    uvicorn main:app --reload --host 0.0.0.0
    ;;
"TEST")
    pytest -v --cov
    ;;
"PROD")
    aerich upgrade
    gunicorn -c gunicorn.py main:app
    ;;
*)
    echo "NO PROCESS SPECIFIED!"
    exit 1
    ;;
esac
