<div align="center">
  <h1>Use LitData with MinIO</h1>
  <img src="https://github.com/bhimrazy/litdata-with-minio/assets/46085301/49e34dc3-8176-4395-b628-99c315f5e7c2" alt="LitData with MinIO" width="640" height="360">
   <br/>
</div>

LitData empowers efficient data optimization and distributed training across cloud storage environments. Pairing it with MinIO—a high-performance, S3-compatible object store—exemplifies a streamlined and scalable data handling workflow for modern AI applications.

This guide provides two ways to get started: a fast, automated setup using `make` (recommended) and a detailed manual setup.

## Prerequisites

- **Docker and Docker Compose**: Ensure Docker is running on your system.
- **Python**: Python 3.10+ is recommended.
- **cURL**: Used for downloading the `uv` installer.

## Getting Started

### Step 1: Clone the Repository

```bash
git clone https://github.com/bhimrazy/litdata-with-minio.git
cd litdata-with-minio
```

### Step 2: Configure Environment Variables

Create a `.env` file from the provided template. This file will hold your configuration, keeping secrets out of your code.

```bash
cp .env.example .env
```

You can customize the settings in `.env` if needed, but the defaults are configured to work with the local MinIO instance.

### Step 3: Setup and Installation

Choose one of the following methods to set up the environment and install dependencies.

---

### Option A: Automated Setup with `make` (Recommended)

This is the fastest way to get up and running.

1.  **Install Dependencies & Create Virtual Environment**:
    This single command installs `uv`, creates a virtual environment, and installs all required Python packages.

    ```bash
    make install
    ```

2.  **Start MinIO Server**:

    ```bash
    make up
    ```

    You can access the MinIO console at **http://127.0.0.1:9001**.

3.  **Configure AWS Credentials**:
    This command configures the `aws` CLI to connect to your local MinIO server, using the credentials from your `.env` file.
    ```bash
    make setup-credentials
    ```

---

### Option B: Manual Setup

Follow these steps if you prefer a manual approach or do not have `make`.

1.  **Install [`uv`](https://docs.astral.sh/uv/) Package Manager**:
    `uv` is a fast, modern Python package manager.

    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

    After installation, follow the instructions on your screen to add `uv` to your `PATH`.

2.  **Create Virtual Environment and Install Dependencies**:

    ```bash
    # Create the virtual environment
    uv venv --python=3.12

    # Activate the virtual environment
    source .venv/bin/activate

    # Install packages
    uv sync
    ```

3.  **Start MinIO Server**:

    ```bash
    docker-compose up -d
    ```

    You can access the MinIO console at **http://127.0.0.1:9001**.

4.  **Configure AWS Credentials**:
    You can configure credentials in two ways.

    **Option 1: Manually create AWS config files.**

    Create or update your `~/.aws/credentials` and `~/.aws/config` files to match the following, using the values from your `.env` file.

    **`~/.aws/credentials`**:

    ```ini
    [default]
    aws_access_key_id = minioadmin
    aws_secret_access_key = minioadmin
    ```

    **`~/.aws/config`**:

    ```ini
    [default]
    region = us-east-1
    output = json
    endpoint_url = http://127.0.0.1:9000
    ```

    **Option 2: Use the AWS CLI.**

    Ensure your virtual environment is activated (`source .venv/bin/activate`) and run the following commands:

    ```bash
    # Set credentials and configuration
    aws configure set aws_access_key_id minioadmin
    aws configure set aws_secret_access_key minioadmin
    aws configure set region us-east-1
    aws configure set output json
    aws configure set endpoint_url http://127.0.0.1:9000
    ```

    Alternatively, you can run `aws configure` for an interactive prompt.

---

## Usage

Once the setup is complete, you can prepare your data, upload it to MinIO, and run the streaming dataset example.

### Using `make`

1.  **Prepare Data**:
    ```bash
    make prepare-data
    ```
2.  **Upload to MinIO**:
    ```bash
    make upload-data
    ```
3.  **Stream Data**:
    ```bash
    make stream-data
    ```

### Manual Usage

Ensure your virtual environment is activated (`source .venv/bin/activate`).

1.  **Prepare Data**:
    ```bash
    python prepare_data.py
    ```
2.  **Upload to MinIO**:

    ```bash
    # Create the bucket (if it doesn't exist)
    aws s3 mb s3://my-bucket

    # Copy the data
    aws s3 cp --recursive my_optimized_dataset s3://my-bucket/my_optimized_dataset
    ```

3.  **Stream Data**:
    ```bash
    python streaming_dataset.py
    ```

## Makefile Commands

The `Makefile` provides several convenient commands:

- `make install`: Sets up `uv` and installs all dependencies.
- `make up`: Starts the MinIO Docker container.
- `make down`: Stops the MinIO container.
- `make setup-credentials`: Configures AWS CLI for MinIO.
- `make prepare-data`: Runs the data preparation script.
- `make upload-data`: Uploads the optimized dataset to MinIO.
- `make stream-data`: Runs the streaming dataset example.
- `make clean`: Removes generated data and the virtual environment.

## References

- [Litdata](https://github.com/Lightning-AI/litdata)
- [MinIO Docker Compose Configuration](https://github.com/minio/minio/blob/master/docs/orchestration/docker-compose/docker-compose.yaml)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Authors

- [Bhimraj Yadav](https://github.com/bhimrazy)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
