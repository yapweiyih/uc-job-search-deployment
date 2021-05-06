import json
import logging
import os
import sys
import traceback

from sentence_transformers import SentenceTransformer

logger = logging.getLogger()
logger.setLevel(logging.INFO)
model = SentenceTransformer("model/")


def lambda_handler(event, context):
    logger.error(event)

    try:
        sentences = event["body"]["sentence"]
        logging.info(sentences)
        emb = model.encode(sentences)
        logging.info(emb)

    except Exception:
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
