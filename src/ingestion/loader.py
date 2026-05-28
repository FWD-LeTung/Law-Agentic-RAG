import os
import sys
from dotenv import load_dotenv
import polars as pl

load_dotenv()
HF_DATASET_PATH = os.getenv("HF-dataset")

df = pl.read_parquet(f"hf://datasets/{HF_DATASET_PATH}/data/metadata.parquet")
df = pl.read_parquet(f"hf://datasets/{HF_DATASET_PATH}/data/relationships.parquet")
df = pl.read_parquet(f"hf://datasets/{HF_DATASET_PATH}/data/content.parquet")

