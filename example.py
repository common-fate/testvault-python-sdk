from testvault.client import Client

c = Client(team_name="common-fate-test")

c.add_member_to_vault("prod-secrets-vault", "chris@commonfate.io")
c.remove_member_from_vault("prod-secrets-vault", "chris@commonfate.io")
