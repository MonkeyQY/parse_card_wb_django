import asyncio
import logging
from rest_framework.decorators import api_view
from rest_framework.response import Response

from pasre_wb_cards.handler_api_parse_card import process_numbers, process_file


log = logging.getLogger("API Parse WB Cards")


@api_view(["POST"])
def parse_cards(request):
    if request.method == "POST" and "sku" in request.data:
        log.info("Загружен SKU")

        return asyncio.run(process_numbers(request))
    elif request.method == "POST" and request.FILES["file"]:
        log.info("Загружен файл")

        return process_file(request)
    else:
        return Response({"status": "error", "message": "File not found"})
