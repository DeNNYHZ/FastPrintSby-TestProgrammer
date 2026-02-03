import hashlib
import logging
import requests
from datetime import datetime

from django.conf import settings

logger = logging.getLogger(__name__)


def fetch_produk():
    now = datetime.now()
    dd = f"{now.day:02d}"
    mm = f"{now.month:02d}"
    yy = f"{now.year % 100:02d}"
    hh = f"{now.hour:02d}"

    username = f"tesprogrammer{dd}{mm}{yy}C{hh}"
    raw_password = f"bisacoding-{dd}-{mm}-{yy}"
    md5_password = hashlib.md5(raw_password.encode()).hexdigest()

    if settings.DEBUG:
        logger.debug("API login: username=%s", username)

    api_url = getattr(settings, "API_URL", "https://recruitment.fastprint.co.id/tes/api_tes_programmer")
    resp = requests.post(
        api_url,
        data={"username": username, "password": md5_password},
        timeout=10,
    )
    resp.raise_for_status()
    data = resp.json()

    if data.get("error") != 0:
        raise Exception(data.get("ket", "Login gagal"))

    return data.get("data", [])
