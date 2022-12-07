import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "16179045"))
    API_HASH = os.environ.get("API_HASH", "dc99c86a0b38365fd6c8b35ae9c577b9")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5051175427:AAEIJdwr1PMWBm6A6x0I09DBC_DdRRP4JjA")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOJQBu1nCLu6VUQuG7U8MqXRKPL7GBekU5xGKV6dbslI0Zk9tLKerBF0PMMEOnAu-Ts6Yaus7fyQl1wQVwKqwljfZukQvYUGJOgh8Rp3EvOymZ_eYT_NuNDcBJdNSuft3Y9x58tVFKvO35S6IGRBlh_Cj1FhDpB3G5fUCxxbOVfc10QRocGF7ZT76lvHnm7xasyCakCN-23IZgZd-SLw5AzxLay4zbMNdzQHUE5GZMjevUsl9lpjE3RmGjLD4lzt5_9MAcrrvp6E0HoW1TK59nFJzWTXu0U3c8N1O5PB7JTKQCoOhapPT-_jMTlpwXgsQ3jdhkjImWYNXlYIcKWY2yqol6Ys=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "ruangdiskusikami") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "ruangprojects") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "2067099647")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
