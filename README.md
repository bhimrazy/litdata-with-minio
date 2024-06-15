# Use litdata with MinIO

MinIO is a high-performance, S3 compatible object store. It is built for
large scale AI/ML, data lake and database workloads. It is software-defined
and runs on any cloud or on-premises infrastructure.

In this example, I will show you how to use litdata with MinIO.

## Prerequisites

Start a MinIO server. You can use the following command to start a MinIO server:
`docker-compose.yml` comes with the configuration to start a MinIO server.

Login at: `http://localhost:9001` with the default credentials setup in the `docker-compose.yml` file.:
username: MINIO_ROOT_USER
password: MINIO_ROOT_PASSWORD

```bash
docker compose up -d
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Usage

Step 1. Setup aws configuration
You can use the default `MINIO_ROOT_USER` and `MINIO_ROOT_PASSWORD` as the access key and secret key.
or create a new access key and secret key from the MinIO web interface.

Aws configuration can be done in two ways:

1. Using environment variables

```bash
export AWS_ACCESS_KEY_ID=access_key
export AWS_SECRET_ACCESS_KEY=secret_key
export AWS_ENDPOINT_URL=http://localhost:9000
```

2. Using the `~/.aws/credentials` file

```bash
mkdir -p ~/.aws && \
cat <<EOL >> ~/.aws/credentials
[default]
aws_access_key_id = nPa2gqrlACrwvmUp28mf
aws_secret_access_key = IdcOtazqxXIFcumFLDWi5RRSlbJWhbGNQMAlq7Bo
EOL

cat <<EOL >> ~/.aws/config
[default]
endpoint_url = http://localhost:9000
EOL
```

2. Prepare data

```bash
python prepare_data.py
```

3. Upload data to minio

   ```bash
   # create the bucket if it does not exist
   aws s3 mb s3://my-bucket

   # check the created bucket
    aws s3 ls

   # upload the data to the bucket
   aws s3 cp --recursive my_optimized_dataset s3://my-bucket/my_optimized_dataset
   ```

4. Use StreamingDataset

   ```bash
    python streaming_dataset.py
   ```

## Conclusion

In this example, we have shown how to use litdata with MinIO. You can use the same approach to use litdata with other S3 compatible object stores.

## References

- [Litdata](https://github.com/Lightning-AI/litdata)
- [MinIO Docker Compose](https://github.com/minio/minio/blob/master/docs/orchestration/docker-compose/docker-compose.yaml)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Authors

- [Bhimraj Yadav](https://github.com/bhimrazy)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
