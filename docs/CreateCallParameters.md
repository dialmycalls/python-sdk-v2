# CreateCallParameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | (Required)  Name the broadcast. | [optional] 
**callerid_id** | **str** | (Required)  The caller id that the message should be sent from. | [optional] 
**recording_id** | **str** | (Required)  The recording id of the message that should be played. | [optional] 
**machine_recording_id** | **str** | The recording id of the message that should be played on answering machines.  If not supplied the recording_id will be used.  use_amd must be true in order for this feature to work. | [optional] 
**send_at** | **str** | When the broadcast should be sent. | [optional] 
**send_immediately** | **bool** | Should the broadcast go out immediately? | [optional] 
**use_amd** | **bool** | Using answering machine detection? | [optional] 
**send_email** | **bool** | Also send an email to the contacts? | [optional] 
**accessaccount_id** | **str** | Schedule this broadcast as an access account. | [optional] 
**contacts** | [**list[ContactAttributes]**](ContactAttributes.md) | (Required)  List of contact information that should be sent the broadcast. | [optional] 
**add_ons** | [**list[PushToListenAgain]**](PushToListenAgain.md) | A list of feature add-ons for the calls. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


