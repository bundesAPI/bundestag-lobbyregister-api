# bundestag_lobbyregister.DefaultApi

All URIs are relative to *https://www.lobbyregister.bundestag.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**suche_detail_json**](DefaultApi.md#suche_detail_json) | **GET** /sucheDetailJson | Search through all registrations


# **suche_detail_json**
> DetailedSearchResults suche_detail_json()

Search through all registrations

### Example


```python
import time
from deutschland import bundestag_lobbyregister
from deutschland.bundestag_lobbyregister.api import default_api
from deutschland.bundestag_lobbyregister.model.detailed_search_results import DetailedSearchResults
from deutschland.bundestag_lobbyregister.model.sort_order import SortOrder
from pprint import pprint
# Defining the host is optional and defaults to https://www.lobbyregister.bundestag.de
# See configuration.py for a list of all supported configuration parameters.
configuration = bundestag_lobbyregister.Configuration(
    host = "https://www.lobbyregister.bundestag.de"
)


# Enter a context with an instance of the API client
with bundestag_lobbyregister.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    q = "q_example" # str | The text to search for. Will search in all text fields.  Leave empty to retrieve all registrations (optional)
    sort = SortOrder("REGISTRATION_DESC") # SortOrder |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search through all registrations
        api_response = api_instance.suche_detail_json(q=q, sort=sort)
        pprint(api_response)
    except bundestag_lobbyregister.ApiException as e:
        print("Exception when calling DefaultApi->suche_detail_json: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| The text to search for. Will search in all text fields.  Leave empty to retrieve all registrations | [optional]
 **sort** | **SortOrder**|  | [optional]

### Return type

[**DetailedSearchResults**](DetailedSearchResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All matching registrations |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

