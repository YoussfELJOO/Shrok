from motor.motor_asyncio import AsyncIOMotorClient

from config import MONGO_DB_URI

from ..logging import LOGGER

LOGGER("𝐘𝐎𝐔𝐒𝐅_𝐄𝐋𝐉𝐎𝐎").info("جـارِ الاتصـال بقاعـدة البيانـات . . .")
try:
    _mongo_async_ = AsyncIOMotorClient(MONGO_DB_URI)
    mongodb = _mongo_async_.Elhyba
    LOGGER("1𝐐𝐘𝐎𝐔𝐒𝐅_𝐄𝐋𝐐𝐉𝐎𝐎").info("تم الاتصـال بقاعـدة البيانـات ...✓")
except:
    LOGGER(__name__).error("حدث خطأ اثناء الاتصال بقاعدة البيانات.")
    exit()
