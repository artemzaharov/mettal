#!/bin/bash

docker stop metall-proxy-1;
certbot renew --force-renewal;
cp /etc/letsencrypt/live/spbvtormetlom.ru/* /metall/sert;
docker start metall-proxy-1;
