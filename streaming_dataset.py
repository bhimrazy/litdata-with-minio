from litdata import StreamingDataset, StreamingDataLoader

# Remote path where full dataset is stored
input_dir = "s3://my-bucket/my_optimized_dataset"

# Create the Streaming Dataset
dataset = StreamingDataset(input_dir, shuffle=True)

# Access any elements of the dataset
sample = dataset[50]
img = sample["image"]
cls = sample["class"]
print("Sample", sample)

# Create dataLoader and iterate over it to train your AI models.
dataloader = StreamingDataLoader(dataset, batch_size=32, num_workers=4)
