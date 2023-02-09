from flask import Blueprint

spc_api_blueprint = Blueprint('spc_api', __name__)

from . import routes