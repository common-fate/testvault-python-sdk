# testvault-python-sdk

A Python SDK for TestVault. TestVault is a sample service used to demonstrate building Common Fate Access Providers to automate entitlements. TestVault is a fictional password management service similar to 1Password or Lastpass.

Common Fate hosts the TestVault service at `https://prod.testvault.granted.run`.

The source code for the TestVault service can be found at https://github.com/common-fate/testvault.

## Installing

```
pip install testvault
```

## Usage

```py
import testvault

client = testvault.Client(team_name="common-fate-test")

client.add_member_to_vault("prod-secrets-vault", "chris@commonfate.io")
client.remove_member_from_vault("prod-secrets-vault", "chris@commonfate.io")
```
