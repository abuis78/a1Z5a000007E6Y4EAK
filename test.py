"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'filter_1' block
    filter_1(container=container)

    return

@phantom.playbook_block()
def filter_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("filter_1() called")

    # collect filtered artifact ids and results for 'if' condition 1
    matched_artifacts_1, matched_results_1 = phantom.condition(
        container=container,
        conditions=[
            ["artifact:*.name", "==", "Vault Artifact"]
        ],
        name="filter_1:condition_1")

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_1 or matched_results_1:
        excel_to_json_2(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_1, filtered_results=matched_results_1)

    return


@phantom.playbook_block()
def endpoint(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("endpoint() called")

    template = """/servicesNS/nobody/soar/storage/collections/data/kokoloris/batch_save"""

    # parameter list for template variable replacement
    parameters = []

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.format(container=container, template=template, parameters=parameters, name="endpoint")

    payload(container=container)

    return


@phantom.playbook_block()
def payload(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("payload() called")

    template = """{0}"""

    # parameter list for template variable replacement
    parameters = [
        "excel_to_json_2:custom_function_result.data.j_dict"
    ]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.format(container=container, template=template, parameters=parameters, name="payload")

    debug_1(container=container)

    return


@phantom.playbook_block()
def post_data_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("post_data_1() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    excel_to_json_2__result = phantom.collect2(container=container, datapath=["excel_to_json_2:custom_function_result.data.j_dict"])
    endpoint = phantom.get_format_data(name="endpoint")

    parameters = []

    # build parameters list for 'post_data_1' call
    for excel_to_json_2__result_item in excel_to_json_2__result:
        if endpoint is not None:
            parameters.append({
                "body": excel_to_json_2__result_item[0],
                "headers": "{ \"Content-Type\": \"application/json\" }",
                "location": endpoint,
            })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("post data", parameters=parameters, name="post_data_1", assets=["splunk_rest"])

    return


@phantom.playbook_block()
def delete_data_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("delete_data_1() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    endpoint = phantom.get_format_data(name="endpoint")

    parameters = []

    if endpoint is not None:
        parameters.append({
            "headers": "{ \"Content-Type\": \"application/json\" }",
            "location": endpoint,
        })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("delete data", parameters=parameters, name="delete_data_1", assets=["splunk_rest"])

    return


@phantom.playbook_block()
def excel_to_json_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("excel_to_json_2() called")

    id_value = container.get("id", None)
    filtered_artifact_0_data_filter_1 = phantom.collect2(container=container, datapath=["filtered-data:filter_1:condition_1:artifact:*.cef.vaultId","filtered-data:filter_1:condition_1:artifact:*.id"])

    parameters = []

    # build parameters list for 'excel_to_json_2' call
    for filtered_artifact_0_item_filter_1 in filtered_artifact_0_data_filter_1:
        parameters.append({
            "vault_id": filtered_artifact_0_item_filter_1[0],
            "container_id": id_value,
        })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="a1Z5a000007E6Y4EAK/excel_to_json", parameters=parameters, name="excel_to_json_2", callback=endpoint)

    return


@phantom.playbook_block()
def debug_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("debug_1() called")

    excel_to_json_2__result = phantom.collect2(container=container, datapath=["excel_to_json_2:custom_function_result.data.j_dict"])

    excel_to_json_2_data_j_dict = [item[0] for item in excel_to_json_2__result]

    parameters = []

    parameters.append({
        "input_1": excel_to_json_2_data_j_dict,
        "input_2": None,
        "input_3": None,
        "input_4": None,
        "input_5": None,
        "input_6": None,
        "input_7": None,
        "input_8": None,
        "input_9": None,
        "input_10": None,
    })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="community/debug", parameters=parameters, name="debug_1")

    return


@phantom.playbook_block()
def on_finish(container, summary):
    phantom.debug("on_finish() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # This function is called after all actions are completed.
    # summary of all the action and/or all details of actions
    # can be collected here.

    # summary_json = phantom.get_summary()
    # if 'result' in summary_json:
        # for action_result in summary_json['result']:
            # if 'action_run_id' in action_result:
                # action_results = phantom.get_action_results(action_run_id=action_result['action_run_id'], result_data=False, flatten=False)
                # phantom.debug(action_results)

    ################################################################################
    ## Custom Code End
    ################################################################################

    return