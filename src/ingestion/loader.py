import os
import sys
from dotenv import load_dotenv
import polars as pl
from langchain_core.documents import Document

load_dotenv()
def load_documentS(metadata, content):
    HF_DATASET_PATH = os.getenv("HF-dataset")
    metadata = pl.read_parquet(f"hf://datasets/{HF_DATASET_PATH}/data/metadata.parquet")
    content = pl.read_parquet(f"hf://datasets/{HF_DATASET_PATH}/data/content.parquet")

    df_merged = content.join(metadata.cast({"id":pl.String}), on="id", how="left")

    docs = []
    for row in df_merged:
        doc_id = str(row.get("id",""))

        metadata = {
            "doc_id": doc_id,
            "title": row.get("title", ""),
            "doc_type": row.get("loai_van_ban", ""),
            "authority": row.get("co_quan_ban_hanh", ""),
            "issue_date": row.get("ngay_ban_hanh", ""),
            "effective_date": row.get("ngay_co_hieu_luc", ""),
            "status": row.get("tinh_trang_hieu_luc", "")
        }

        docs.append(Document(
            page_content=row.get("content_html", ""),
            metadata=metadata
        ))
    return docs