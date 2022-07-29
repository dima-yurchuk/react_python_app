from flask import Blueprint

api_restfull_bp = Blueprint('api_restfull_bp_in', __name__)

from . import view