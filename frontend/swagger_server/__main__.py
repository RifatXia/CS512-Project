#!/usr/bin/env python3

from connexion import FlaskApp

from swagger_server import encoder


def main():
    app = FlaskApp(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Table Extraction Service'}, pythonic_params=True)
    app.run(port=8085)


if __name__ == '__main__':
    main()
