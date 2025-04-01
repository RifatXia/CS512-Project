import connexion
import six

from swagger_server import util
from flask import send_file, request as flask_request


def table_extract_post(file=None):
    file_name = file.filename
    # file_data = file.read()
    file.save(f"temp_{file_name}")
    query_params = connexion.request.query_params

    for query, value in query_params.items():
        print(query, value)

    output_file_path = "lab01_dataset_2.csv"
    return send_file(output_file_path,
                     as_attachment=True,
                     download_name='generated_file.csv')
