from litdata import StreamingDataset, StreamingDataLoader
from config import load_config


def main():
    """Main function to run the streaming dataset example."""
    print("Loading configuration...")
    config = load_config()

    # Remote path where full dataset is stored
    input_dir = f"s3://{config.minio.bucket}/{config.data.optimized_dir}"
    print("Input directory:", input_dir)

    # Create the Streaming Dataset
    dataset = StreamingDataset(input_dir)

    print(f"The dataset contains {len(dataset)} items.")

    # Access a sample from the dataset
    sample = dataset[50]
    print("Sample 50:", sample)

    # Create a DataLoader to iterate over the dataset
    dataloader = StreamingDataLoader(dataset, batch_size=32, num_workers=4)

    print("\nIterating through the DataLoader...")
    for i, batch in enumerate(dataloader):
        print(f"Batch {i}:", batch)
        # We'll just look at the first batch for this example
        break


if __name__ == "__main__":
    main()
