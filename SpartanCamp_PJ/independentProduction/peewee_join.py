from database import DetectResult
from database import UploadImages

query = DetectResult.select(
    DetectResult.id,
    UploadImages.image_name,
    DetectResult.count,
    DetectResult.created_date,
).join(UploadImages, on=(DetectResult.uploadImages == UploadImages.id))
print(query)
query_result = query.execute()
for i in query_result:
    print(i.id, i.uploadImages.image_name, i.count)
