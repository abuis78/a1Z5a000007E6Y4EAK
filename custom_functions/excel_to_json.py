def excel_to_json(vault_id=None, container_id=None, **kwargs):
    """
    Args:
        vault_id
        container_id
    
    Returns a JSON-serializable object that implements the configured data paths:
        j_dict
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
    
    excel_data_df = pandas.read_excel(file, sheet_name='Sheet1', names=["pool","virtualmachine", "user"])
    #excel_data_df = pandas.read_excel(file, sheet_name='Sheet1')
    # execl_data_df = excel_data_df.rename(columns = {"Pool":"pool", "User": "user", "Virtual Machine": "virtualmachine"} )
    j_dict = excel_data_df.to_json(orient='records')
    #j_dict = json.loads(j_dict)
    phantom.debug(j_dict)
    phantom.debug(type(j_dict))
    
    outputs["j_dict"] = j_dict
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
