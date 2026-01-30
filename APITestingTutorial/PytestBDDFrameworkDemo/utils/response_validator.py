def validate_status_code(response, expected_code):
    assert response.status_code == expected_code,\
        f"expected status code {expected_code}doesn't match response status code{response.status_code}"

def validate_key_in_response(response, expected_key):
    assert expected_key in response.json(),\
        f"{expected_key} not found in json response {response.json}"

def validate_response_time(response, max_time_seconds =2):
    assert response.elapsed.total_seconds() >= max_time_seconds,\
        f"{response.elapsed.total_seconds} time is greater than {max_time_seconds} seconds"


def validate_content_type(response,expected_content_type="application/json"):
    assert expected_content_type in response.headers.get('Content-Type',''),\
        f"{expected_content_type} not found in response headers"

def validate_json_body(response):
    try:
        response.json()
    except ValueError:
        assert False,"Response body is not valid JSON"

def validate_value(response,key,expected_value):
    json_data = response.json()
    actual_value=json_data.get(key)
    assert actual_value == expected_value,f"{actual_value} is not equal to {expected_value}"

def validate_nested_key_exists(response,*keys):
    json_data = response.json()
    for key in keys:
        assert key in json_data,f"{key} not found in json response {json_data}"
        json_data = json_data[key]

def validate_list_not_empty(response):
    assert len(response.json()) > 0,f"Response body is empty: {response.json()}"

def validate_error_message(response,expected_message):
    json_data = response.json()
    actual_message = json_data.get("error") or json_data.get("message")
    assert actual_message == expected_message,f"{actual_message} is not equal to {expected_message}"





