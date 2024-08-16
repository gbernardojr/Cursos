Solução do Desafio - Configurar uma rede do Google Cloud: laboratório com desafio

Dentro da VM da empresa Antern, por SSH, rodar os comandos:

```shell
sudo su
```

```
apt install postgresql-13-pglogical
```

```
sudo su - postgres -c "gsutil cp gs://cloud-training/gsp918/pg_hba_append.conf ."
sudo su - postgres -c "gsutil cp gs://cloud-training/gsp918/postgresql_append.conf ."
sudo su - postgres -c "cat pg_hba_append.conf >> /etc/postgresql/13/main/pg_hba.conf"
sudo su - postgres -c "cat postgresql_append.conf >> /etc/postgresql/13/main/postgresql.conf"
sudo systemctl restart postgresql@13-main
```

