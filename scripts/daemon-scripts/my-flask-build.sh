#!/bin/bash

APP_PATH="/opt/APP_DIR"
DAEMON=$APP_PATH"/app/app.py"


PIDFILE="/var/run/my-flask-app.pid"
USER="root"


case "$1" in
  start)
    echo "Starting Flask Server as Daemon"

    export PYTHONPATH=$APP_PATH
    /sbin/start-stop-daemon --start --pidfile $PIDFILE --user $USER --group $USER -b --make-pidfile --exec $DAEMON
    ;;
  stop)
    echo "Stopping server"
    /sbin/start-stop-daemon --stop --pidfile $PIDFILE --verbose
    ;;
  *)
    echo "Usage: $0 {start|stop}"
    exit 1
    ;;
esac

exit 0
