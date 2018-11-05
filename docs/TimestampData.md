# TimestampData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_id** | **int** | 0: Bitcoin | [optional] 
**private_key** | **str** | The private key represents the top hash in the Merkle Tree (see https://en.wikipedia.org/wiki/Merkle_tree ) or the hash of all hashes in the transaction. | [optional] 
**submit_status** | **int** | The submit status of the hash:   0: the hash was not broadcasted yet  1: the hash was included into a transaction and broadcasted to the network, but not included into a block  2: the transaction was included into the latest block  3: the timestamp for your hash was successfully created. | [optional] 
**timestamp** | **int** | The date is returned in the following format: [ms] since 1.1.1970 (unix epoch), timezone: UTC. This is a true timestamp. | [optional] 
**transaction** | **str** | If available: the transaction hash of the timestamp. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


