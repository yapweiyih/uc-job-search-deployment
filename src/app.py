import json
import logging
import os
import sys
import traceback
from typing import List

import numpy as np
from sentence_transformers import SentenceTransformer

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def get_sentence_emb(sentence: List[str]) -> np.ndarray:
    model = SentenceTransformer("model/")
    emb = model.encode(sentence)
    return emb


def lambda_handler(event, context):
    logger.error(event)
    os.system("uname -a")

    try:
        sentences = event["body"]["sentence"]
        emb = get_sentence_emb(sentences)
        logging.info(emb)

    except Exception as exp:
        exception_type, exception_value, exception_traceback = sys.exc_info()
        traceback_string = traceback.format_exception(exception_type, exception_value, exception_traceback)
        err_msg = json.dumps(
            {"errorType": exception_type.__name__, "errorMessage": str(exception_value), "stackTrace": traceback_string}
        )
        logger.error(err_msg)

    return {
        "statusCode": 200,
        "body": json.dumps({"embedding": emb.tolist()}),
    }
