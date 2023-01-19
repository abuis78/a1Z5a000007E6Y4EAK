def excel_to_json(vault_id=None, container_id=None, **kwargs):
    """
    Args:
        vault_id
        container_id
    
    Returns a JSON-serializable object that implements the configured data paths:
        
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    import pandas
    from json import dumps
    
    outputs = {}
    # Write your custom code here...
    def lower_dict(d):
        new_dict = dict((k.lower(), v) for k, v in d.items())
        return new_dict    
    
    
    
    success, message, info = phantom.vault_info(vault_id=vault_id, container_id=container_id)
    phantom.debug(info[0]["path"])
    phantom.debug(info[0]["name"])
    file = info[0]["path"]
    phantom.debug(file)
    
    excel_data_df = pandas.read_excel(file, sheet_name='Sheet1')
    json_str = excel_data_df.to_json(orient='records')
    phantom.debug(json_str[0])

    phantom.debug(lower_dict(json_str[0]))

    
    
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
