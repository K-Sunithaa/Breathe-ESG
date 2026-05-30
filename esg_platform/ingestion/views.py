from rest_framework.decorators import api_view
from rest_framework.response import Response
from ingestion.services import ingest_file
@api_view(["POST"])
def upload_file(request):
    try:
        file_obj = request.FILES.get("file")
        source_type = request.data.get("source_type")

        print(file_obj)
        print(source_type)

        result = ingest_file(file_obj, source_type)

        return Response(result)

    except Exception as e:
        print("ERROR:", str(e))
        return Response({"error": str(e)}, status=500)