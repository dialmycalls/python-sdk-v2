# CreateTextParameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | (Required)  Name the broadcast. | [optional] 
**keyword_id** | **str** | (Required)  The keyword id that should be associated with this broadcast. | [optional] 
**messages** | **list[str]** | (Required)  List of messages to send (up to 10). | [optional] 
**send_at** | **str** | When the broadcast should be sent. | [optional] 
**send_immediately** | **bool** | Should the broadcast go out immediately? | [optional] 
**send_email** | **bool** | Also send an email to the contacts? | [optional] 
**accessaccount_id** | **str** | Schedule this broadcast as an access account. | [optional] 
**shortcode_id** | **str** | The shortcode id that the broadcast will be sent from. | [optional] 
**concatenate_sms** | **bool** | Combine all SMS messages into 1 message on the end users device. | [optional] 
**contacts** | [**list[ContactAttributes]**](ContactAttributes.md) | (Required)  List of contact information that should be sent the broadcast. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


