from materio.methods.direktor.home_page import direc_inspection
from materio.models import chetdan_buyurtma


def get_storage_order(request, params):
    result = direc_inspection(request)
    if not result['status']:
        return result

    return {
        "result": [x.chetdan_buyurtma_format() for x in chetdan_buyurtma.objects.all()]
    }
