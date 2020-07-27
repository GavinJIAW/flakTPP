from flask import Flask

from apps.apis import init_api
from exts import db, cors, cache
from settings import DevelopmentConfig

config = {
    'CACHE_TYPE': 'redis',
    'CACHE_REDIS_HOST': '115.28.139.69',
    'CACHE_REDIS_POST': 6379,
    'PASSWORD':None
}


def create_app():
    app = Flask(__name__, static_folder='../static')
    app.config.from_object(DevelopmentConfig)
    db.init_app(app=app)
    cors.init_app(app=app, support_credentials=True)  # 支持证书
    cache.init_app(app=app, config=config)
    init_api(app=app)
    return app
