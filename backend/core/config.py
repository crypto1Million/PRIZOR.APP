import redis
import cloudinary
from dotenv import load_dotenv
import os

load_dotenv()

redis_client = redis.Redis(host="localhost", port=6379, db=0)

cloudinary.config(
    cloud_name="dm0ee49uu",
    api_key="844517275869586",
    api_secret="e4UG9xoFr5TNVPcgYhSB6VWI16M"
)    