# Azure

## Resource Manager

- [(Overview on MSLearn)](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/overview)
- [Deployment What If (on MSLearn)](https://learn.microsoft.com/en-us/rest/api/resources/deployments/what-if?view=rest-resources-2025-04-01&tabs=HTTP) deployment validation
- [Python library](https://learn.microsoft.com/en-us/python/api/overview/azure/resources?view=azure-python)
    - Least documented library on GitHub I've seen from a large company in some time [(codebase on GitHub/Azure/azure-sdk-for-python)](https://github.com/Azure/azure-sdk-for-python)
- Azure Resource Manager Test Toolkit (arm-ttk) ([MSLearn](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/test-toolkit) | [GitHub](https://github.com/Azure/arm-ttk))
    - Using the arm-ttk in a GitHub action to test your arm template ([dev.to link](https://dev.to/omiossec/using-arm-ttk-in-github-to-test-azure-arm-template-3jfi))

## Python Kusto Module
This is not very well documented. I genuinely had to go back to the code on GitHub and spend time reverse engineering it in order to even get this far (and there's more that I've used, but not documented).
### Module list
- [azure-kusto-data](https://pypi.org/project/azure-kusto-data/)
- [azure-kusto-ingest](https://pypi.org/project/azure-kusto-ingest/)

### Interface Sample
Authentication
```python
from azure.kusto.data import KustoConnectionStringBuilder

cluster_url = "contoso.kusto.windows.net"
# Use a browser to prompt user to log in to cluster, this will not require an AppID this way
# ->This pattern is intended for development use only
conn = KustoConnectionStringBuilder.with_interactive_login(cluster_url)
```

Make Requests
```python
from azure.kusto.data import KustoClient
database = "Contoso_customer"
query = "Customers | order by Name asc | take 10"
with KustoClient(conn) as client:
    resp = client.execute(database, query)
resp_table = resp.tables[1]
```

When making requests, you can also submit data the same way, but `.tables` will probably have a length of 0.

## Notes
Unfortunately, you may end up in scenarios where Data Explorer can't complete requests without sending you more data than requested. It's worth noting that you may end up in a situation where you could have to recreate some of the filters.
