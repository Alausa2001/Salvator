#!/usr/bin/env bash
# database backup

sudo mysqldump -uroot salvator_db -p > db_backup.sql
tar -cfz $(date +"%d-%m-%Y".tar.gz) db_backup.sql
git add $(date +"%d-%m-%Y".tar.gz)
git commit -m "database backup"
git push
