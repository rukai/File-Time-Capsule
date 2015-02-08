#!/bin/bash
configPath=$(dirname $(readlink -f $0))

sudo nginx -c $configPath/nginx.conf
