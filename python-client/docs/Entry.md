# Entry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**client_identity** | **str** | Possible clients this entity is lobbying for.  - &#x60;BOTH&#x60;: Clients include legal entities and  natural persons - &#x60;NATURAL_PERSON&#x60;: Clients are only natural persons - &#x60;ORGANIZATION&#x60;: Clients are only legal entities - &#x60;-&#x60; There is no client, the entity is lobbying for itself  | [optional] 
**employee_count** | [**EntryEmployeeCount**](EntryEmployeeCount.md) |  | [optional] 
**refuse_financial_expenses_information** | **bool** |  | [optional] 
**financial_expenses_euro** | [**EntryFinancialExpensesEuro**](EntryFinancialExpensesEuro.md) |  | [optional] 
**refuse_public_allowance_information** | **bool** |  | [optional] 
**refuse_donation_information** | **bool** |  | [optional] 
**donation_information_required** | **bool** | True, if this entity received more than € 20,000 of donations from a single donor in the last calendar year  | [optional] 
**location_of_report_publication** | **str** |  | [optional] 
**account** | [**EntryAccount**](EntryAccount.md) |  | [optional] 
**activity_description** | **str** |  | [optional] 
**activity_operation_type** | **str** | - &#x60;MANDATE_OPERATED&#x60;: The entity is mandated to lobby for another entity - &#x60;SELF_OPERATED&#x60;: The entity lobbies for itself - &#x60;BOTH&#x60;: The entity lobbies for itself and in the mandate of others.  | [optional] 
**activity** | [**Activity**](Activity.md) |  | [optional] 
**codex_violation** | **bool** |  | [optional] 
**lobbyist_identity** | [**LobbyistIdentity**](LobbyistIdentity.md) |  | [optional] 
**legislative_projects** | [**[LegislativeProject]**](LegislativeProject.md) |  | [optional] 
**donators** | [**Donator**](Donator.md) |  | [optional] 
**fields_of_interest** | [**[FieldOfInterest]**](FieldOfInterest.md) |  | [optional] 
**client_organizations** | [**[ClientOrganization]**](ClientOrganization.md) |  | [optional] 
**client_persons** | [**[NamedEmployee]**](NamedEmployee.md) |  | [optional] 
**register_entry_media** | [**[Media]**](Media.md) |  | [optional] 
**disclosure_requirements_exist** | **bool** |  | [optional] 
**refuse_annual_finance_statement** | **bool** |  | [optional] 
**annual_report_exist** | **bool** |  | [optional] 
**missing_annual_report_reason** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


