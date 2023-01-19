def convertexceintjson(vault_id=None, **kwargs):
    """
    Args:
        vault_id
    
    Returns a JSON-serializable object that implements the configured data paths:
        file_json
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    import excel2json
    
    outputs = {}
    
    # Write your custom code here...
    success, message, info = phantom.vault_info(vault_id=vault_id, file_name=None, container_id=None, trace=False)
    phantom.debug(info)
    
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
