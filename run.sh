#!/usr/bin/env bash
echo '🚀 [Trippify] Shutting down last containers'
docker-compose down
echo '🚀 [Trippify] Building and kicking off containers'
docker-compose up -d --build
echo '🚀 [Trippify] Sleeping 5 seconds for letting the DB initializes'
sleep 5
echo '🚀 [Trippify] Creating DDL Base'
docker run -it --rm --network trippify trippify-db psql -h trippify-db -U postgres postgres -f /tmp/create_ddl_base.sql
echo '🚀 [Trippify] DDL Base created'
echo '🚀 [Trippify] Creating DDL Trippify'
docker run -it --rm --network trippify trippify-db psql -h trippify-db -U trippify trippify -f /tmp/create_ddl_trippify.sql
echo '🚀 [Trippify] DDL Trippify created'
echo '🚀 [Trippify] Deployed!'