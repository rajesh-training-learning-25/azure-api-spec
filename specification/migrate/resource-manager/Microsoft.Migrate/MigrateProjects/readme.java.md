## Java

These settings apply only when `--java` is specified on the command line.
Please also specify `--azure-libraries-for-java-folder=<path to the root directory of your azure-libraries-for-java clone>`.

``` yaml $(java)
azure-arm: true
fluent: true
namespace: com.azure.resourcemanager.migration.hub
license-header: MICROSOFT_MIT_NO_CODEGEN
payload-flattening-threshold: 1
output-folder: $(azure-libraries-for-java-folder)/azure-mgmt-migrationhub
```

### Java multi-api

``` yaml $(java) && $(multiapi)
batch:
  - tag: package-2020-05
  - tag: package-2023-01
```

### Tag: package-2020-05 and java

These settings apply only when `--tag=package-2020-05 --java` is specified on the command line.
Please also specify `--azure-libraries-for-java=<path to the root directory of your azure-sdk-for-java clone>`.

``` yaml $(tag) == 'package-2020-05' && $(java) && $(multiapi)
java:
  namespace: com.azure.resourcemanager.migration.hub.v2020_05_01
  output-folder: $(azure-libraries-for-java-folder)/sdk/migrationhub/mgmt-v2020_05_01
regenerate-manager: true
generate-interface: true
```

### Tag: package-2023-01 and java

These settings apply only when `--tag=package-2023-01 --java` is specified on the command line.
Please also specify `--azure-libraries-for-java=<path to the root directory of your azure-sdk-for-java clone>`.

``` yaml $(tag) == 'package-2023-01' && $(java) && $(multiapi)
java:
  namespace: com.azure.resourcemanager.migration.hub.v2023_01_01
  output-folder: $(azure-libraries-for-java-folder)/sdk/migrationhub/mgmt-v2023_01_01
regenerate-manager: true
generate-interface: true
```