<div align="center">
  <h1>Use LitData with MinIO</h1>
  <img src="https://github.com/bhimrazy/litdata-with-minio/assets/46085301/49e34dc3-8176-4395-b628-99c315f5e7c2" alt="LitData with MinIO" width="640" height="360">
   <br/>
</div>


LitData empowers efficient data optimization and distributed training across cloud storage environments, supporting diverse data types like images, text, and video. Pairing seamlessly with MinIO—a high-performance, S3-compatible object store designed for large-scale AI/ML, data lakes, and databases—this integration exemplifies streamlined, scalable data handling for modern applications.

## Prerequisites

1. **Start MinIO Server**:
   Start a MinIO server using Docker Compose with the provided configuration:

   ```bash
   docker-compose up -d
   ```

   Access MinIO at [http://localhost:9001](http://localhost:9001) with default credentials:

   - Username: `MINIO_ROOT_USER`
   - Password: `MINIO_ROOT_PASSWORD`

2. **Install Required Packages**:
   Install Python dependencies listed in `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Step 1: Setup AWS Configuration

You can configure AWS credentials for MinIO access either via environment variables or by creating a `~/.aws/{credentials,config}` file.

**Using Environment Variables:**

```bash
export AWS_ACCESS_KEY_ID=access_key
export AWS_SECRET_ACCESS_KEY=secret_key
export AWS_ENDPOINT_URL=http://localhost:9000
```

**Using `~/.aws/{credentials,config}` File:**

```bash
mkdir -p ~/.aws && \
cat <<EOL >> ~/.aws/credentials
[default]
aws_access_key_id = access_key
aws_secret_access_key = secret_key
EOL

cat <<EOL >> ~/.aws/config
[default]
endpoint_url = http://localhost:9000
EOL
```

### Step 2: Prepare Data

Prepare your data using Python script `prepare_data.py`:

```bash
python prepare_data.py
```

### Step 3: Upload Data to MinIO

Ensure the bucket exists or create it if necessary, then upload your data:

```bash
# Create the bucket if it does not exist
aws s3 mb s3://my-bucket

# List buckets to verify
aws s3 ls

# Upload data to the bucket
aws s3 cp --recursive my_optimized_dataset s3://my-bucket/my_optimized_dataset
```

### Step 4: Use StreamingDataset

Utilize `streaming_dataset.py` to work with data as a streaming dataset:

```bash
python streaming_dataset.py
```

## Conclusion

This example illustrates how to integrate litdata with MinIO for efficient data management. Similar approaches can be applied to other S3-compatible object stores.

## References

- [Litdata](https://github.com/Lightning-AI/litdata)
- [MinIO Docker Compose Configuration](https://github.com/minio/minio/blob/master/docs/orchestration/docker-compose/docker-compose.yaml)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Authors

- [Bhimraj Yadav](https://github.com/bhimrazy)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
