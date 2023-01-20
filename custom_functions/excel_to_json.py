def excel_to_json(vault_id=None, container_id=None, remove_domain_field=None, **kwargs):
    """
    Args:
        vault_id
        container_id
        remove_domain_field
    
    Returns a JSON-serializable object that implements the configured data paths:
        j_dict
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    import pandas
    import json
    import re
    
    outputs = {}
    # Write your custom code here...
    r = r'(?:.*\\)(?P<user>[^\\]+)'
    p = re.compile(r)
    def remove_domain(user):
        m = p.match(user)
        if m:
            return m.group('user')
        else:
            return user

    success, message, info = phantom.vault_info(vault_id=vault_id, container_id=container_id)
    file = info[0]["path"]
    excel_data_df = pandas.read_excel(file, sheet_name='Sheet1', converters={remove_domain_field: remove_domain})
    excel_data_df.columns= excel_data_df.columns.str.lower()
    excel_data_df.columns = excel_data_df.columns.str.replace(" ", "")
    column_names = list(excel_data_df.columns.values)
    j_dict = excel_data_df.to_json(orient='records')
    
    outputs["j_dict"] = j_dict
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
