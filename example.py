import testvault

client = testvault.Client(team_name="common-fate-test")

client.add_member_to_vault("prod-secrets-vault", "chris@commonfate.io")
client.remove_member_from_vault("prod-secrets-vault", "chris@commonfate.io")
