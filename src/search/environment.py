import os 

class Environment:

  default_storage = os.getenv("ENV_STORAGE", "/db/superinsight/models/private/semantic-search")
  kafka_topic_to_consume = str(os.getenv("ENV_KAFKA_TOPIC_TO_CONSUME", "none"))
  kafka_topic_divide = str(os.getenv("ENV_KAFKA_TOPIC_DIVIDE", "superinsight_ml_search_divide_V0911"))
  kafka_topic_conquer = str(os.getenv("ENV_KAFKA_TOPIC_CONQUER", "superinsight_ml_search_conquer_V0911"))
  kafka_topic_combine = str(os.getenv("ENV_KAFKA_TOPIC_TO_COMBINE", "superinsight_ml_search_combine_V0911"))
  kafka_bootstrap_servers = str(os.getenv("ENV_KAFKA_BOOTSTRAP_SERVERS", "localhost:9092"))
  kafka_group_default = str(os.getenv("ENV_KAFKA_GROUP_DEFAULT", "v30"))
  kafka_group_id_local_disk = str(os.getenv("ENV_KAFKA_GROUP_ID_LOCAL_DISK", "network-drive"))
  semantic_search_model = os.getenv("ENV_SEMANTIC_SEARCH_MODEL", "sentence-transformers/distiluse-base-multilingual-cased-v2")
  host_ml_inference = os.getenv("ENV_ML_INFERENCE", "http://localhost:8084")
  image_classification_model = os.getenv("ENV_IMAGE_CLASSIFICAION_MODEL", "google/vit-large-patch32-384")
  image_to_text_model = os.getenv("ENV_IMAGE_TO_TEXT_MODEL", "nlpconnect/vit-gpt2-image-captioning")
  index_image_to_caption = os.getenv("ENV_IMAGE_TO_CAPTION", "False") == "True"
  index_image_to_label = os.getenv("ENV_IMAGE_TO_LABEL", "False") == "True"