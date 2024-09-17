from fastapi.exceptions import HTTPException

unauthorized = HTTPException(400, detail="Unauthorized")
