import copy


def extract_in_data(extracted_data):
    extracted_request_data = []
    for data in extracted_data:
        extracted_request_data.append({'data': copy.deepcopy(data)})
    return extracted_request_data
