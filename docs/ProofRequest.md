# ProofRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **int** | 0: Bitcoin | 
**hash_string** | **str** | Hash in HEX representation for which the proof should be created. We allow the use of SHA-256. Note: We handle the hashes in lower-case. | 
**proof_type** | **int** | Specifies which type of file should be returned. Possible value(s):  0: proof with a seed file (txt) or proof with a merkle tree (xml) 1: proof with a PDF file   Other formats will follow. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


