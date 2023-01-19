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
    import json
    
    outputs = {}
    # Write your custom code here...

    
    
    success, message, info = phantom.vault_info(vault_id=vault_id, container_id=container_id)
    file = info[0]["path"]
    phantom.debug(file)
    
    excel_data_df = pandas.read_excel(file, sheet_name='Sheet1')
    j = excel_data_df.to_json(orient='records')
    json_str = json.loads(j)
    phantom.debug(type(json_str))
    
    y = dict((k.lower(), v) for k, v in json_str.iteritems())
    

    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
