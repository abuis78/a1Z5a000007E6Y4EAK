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
    in_dict = {}
    json_str = {}
    # Write your custom code here...
    phantom.debug(type(json_str))

    
    
    success, message, info = phantom.vault_info(vault_id=vault_id, container_id=container_id)
    file = info[0]["path"]
    phantom.debug(file)
    
    excel_data_df = pandas.read_excel(file, sheet_name='Sheet1')
    j = excel_data_df.to_json(orient='records')
    json_str = json.loads(j)
    phantom.debug(type(json_str))
    
    def lower_key(json_str):
        if type(in_dict) is dict:
            out_dict = {}
            for key, item in in_dict.items():
                out_dict[key.lower()] = lower_key(item)
            phantom.debug("Ausgabe {}".format(out_dict))
        elif type(in_dict) is list:
            phantom.debug([lower_key(obj) for obj in in_dict])
        else:
            phantom.debug("Ausgabe {}".format(in_dict))
            
    lower_key(json_str)
    

    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
