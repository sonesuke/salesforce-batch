

```bash
docker-compose build
```

```bash
docker-compose up proc1
```

```bash
docker-compose logs -t proc1
```

```bash
docker-compose run proc1 bash
```


Credential
----------

Put the followings to `.env` file.
```text
SF_USERNAME=<Salesforce username>
SF_PASSWORD=<Salesforce password>
SF_CLIENT_ID=<Salesfroce consumer key>
SF_CLIENT_SECRET=<Salesforce consumer secret>
SF_SECURITY_TOKEN=<Salesforce security token>
```
