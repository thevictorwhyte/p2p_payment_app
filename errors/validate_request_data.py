from typing import Union

def validate_request_data(data: dict, required_fields: list) -> Union[None, str]:
  for field in required_fields:
    if field not in data:
      return f"{field} is required"
  return None