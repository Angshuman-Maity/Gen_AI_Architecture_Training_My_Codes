import pandas as pd
from dotenv import load_dotenv
import os 
import weaviate
from weaviate.classes.init import Auth
from sentence_transformers import SentenceTransformer
import weaviate.classes as wvc
from weaviate.classes.config import Property, DataType, Configure, VectorDistances