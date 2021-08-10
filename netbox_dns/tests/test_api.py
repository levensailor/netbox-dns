from django.urls import reverse
from utilities.testing import APITestCase
from netbox_dns.models import NameServer, Zone


class ZoneAPITestCase(APITestCase):
    """
    Tests for Zone API (format=json)
    """

    def test_view_zone_without_permission(self):
        url = reverse("plugins-api:netbox_dns-api:zone-list")
        response = self.client.get(f"{url}?format=json", **self.header)
        self.assertEqual(response.status_code, 403)

    def test_view_zone_with_permission(self):
        self.add_permissions("netbox_dns.view_zone")
        url = reverse("plugins-api:netbox_dns-api:zone-list")
        response = self.client.get(f"{url}?format=json", **self.header)
        self.assertEqual(response.status_code, 200)

    def test_view_zone_detail_with_permission(self):
        self.add_permissions("netbox_dns.view_zone")

        zone = Zone.objects.create(name="asdf")

        url = reverse("plugins-api:netbox_dns-api:zone-detail", kwargs={"pk": zone.id})
        response = self.client.get(f"{url}?format=json", **self.header)
        self.assertEqual(response.status_code, 200)

    def test_add_zone_with_permission(self):
        self.add_permissions("netbox_dns.add_zone")
        url = reverse("plugins-api:netbox_dns-api:zone-list")
        response = self.client.post(
            f"{url}?format=json", {"name": "Name 1"}, **self.header
        )
        self.assertEqual(response.status_code, 201)

    def test_add_zone_without_permission(self):
        url = reverse("plugins-api:netbox_dns-api:zone-list")
        response = self.client.post(
            f"{url}?format=json", {"name": "Name 1"}, **self.header
        )
        self.assertEqual(response.status_code, 403)

    def test_delete_zone_with_permission(self):
        self.add_permissions("netbox_dns.delete_zone")
        zone = Zone.objects.create(name="asdf")

        url = reverse("plugins-api:netbox_dns-api:zone-detail", kwargs={"pk": zone.id})
        response = self.client.delete(
            f"{url}?format=json", {"name": "Name 1"}, **self.header
        )
        self.assertEqual(response.status_code, 204)

    def test_delete_zone_without_permission(self):
        zone = Zone.objects.create(name="asdf")

        url = reverse("plugins-api:netbox_dns-api:zone-detail", kwargs={"pk": zone.id})
        response = self.client.delete(
            f"{url}?format=json", {"name": "Name 1"}, **self.header
        )
        self.assertEqual(response.status_code, 403)


class NameServerAPITestCase(APITestCase):
    """
    Tests for NameServer API (format=json)
    """

    def test_list_nameserver_without_permission(self):
        url = reverse("plugins-api:netbox_dns-api:nameserver-list")
        response = self.client.get(f"{url}?format=json", **self.header)
        self.assertEqual(response.status_code, 403)

    def test_list_nameserver_with_permission(self):
        self.add_permissions("netbox_dns.view_nameserver")
        url = reverse("plugins-api:netbox_dns-api:nameserver-list")
        response = self.client.get(f"{url}?format=json", **self.header)
        self.assertEqual(response.status_code, 200)

    def test_view_nameserver_detail_with_permission(self):
        self.add_permissions("netbox_dns.view_nameserver")

        nameserver = NameServer.objects.create(name="asdf")

        url = reverse(
            "plugins-api:netbox_dns-api:nameserver-detail", kwargs={"pk": nameserver.id}
        )
        response = self.client.get(f"{url}?format=json", **self.header)
        self.assertEqual(response.status_code, 200)

    def test_add_nameserver_with_permission(self):
        self.add_permissions("netbox_dns.add_nameserver")
        url = reverse("plugins-api:netbox_dns-api:nameserver-list")
        response = self.client.post(
            f"{url}?format=json", {"name": "Name 1"}, **self.header
        )
        self.assertEqual(response.status_code, 201)

    def test_add_nameserver_without_permission(self):
        url = reverse("plugins-api:netbox_dns-api:nameserver-list")
        response = self.client.post(
            f"{url}?format=json", {"name": "Name 1"}, **self.header
        )
        self.assertEqual(response.status_code, 403)

    def test_delete_nameserver_with_permission(self):
        self.add_permissions("netbox_dns.delete_nameserver")
        nameserver = NameServer.objects.create(name="asdf")

        url = reverse(
            "plugins-api:netbox_dns-api:nameserver-detail", kwargs={"pk": nameserver.id}
        )
        response = self.client.delete(
            f"{url}?format=json", {"name": "Name 1"}, **self.header
        )
        self.assertEqual(response.status_code, 204)

    def test_delete_nameserver_without_permission(self):
        nameserver = NameServer.objects.create(name="asdf")

        url = reverse(
            "plugins-api:netbox_dns-api:nameserver-detail", kwargs={"pk": nameserver.id}
        )
        response = self.client.delete(
            f"{url}?format=json", {"name": "Name 1"}, **self.header
        )
        self.assertEqual(response.status_code, 403)
