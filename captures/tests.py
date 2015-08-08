from django.core.urlresolvers import reverse
from django.test import TestCase, Client
from django.contrib.auth.models import User, Permission
from django.core.files.uploadedfile import SimpleUploadedFile

from .models import Capture

class TestCaptureViews(TestCase):
    def setUp(self):
        self.admin_user = User.objects.create_user('admin', 'myemail@test.com', 'admin')

        # Give admin user all permissions.
        # Use this instead of creating a superuser, that way the permissions used in the
        # view must exist in the permission table
        for permission in Permission.objects.all():
            self.admin_user.user_permissions.add(permission)

        self.testfile1 = open('captures/test_data/smtp.pcap', mode='rb').read()
        self.testfile2 = open('captures/test_data/dhcp.pcap', mode='rb').read()
        self.capture1 = Capture.objects.create(
            name="Test capture 1",
            #filename='smtp.pcap',
            #filesize=1000,
            description='Some data from a fake pcap file',
            file=SimpleUploadedFile('smtp.txt', self.testfile1)
        )
        self.capture2 = Capture.objects.create(
            name="Test capture 2",
            #filename='mysecond_pcapfile.pcap',
            #filesize=1000,
            description='Some data from a fake pcap file',
            file=SimpleUploadedFile('dhcp.txt', self.testfile2)
        )
        self.client = Client()

    def assert_responses(self, expected_code, url_names, kwargs={}, prefix_urls='', suffix_urls=''):
        """
        Helper function to test a bunch of pages with specific kwargs

        :param expected_code: expected http response code (e.g. 200 or 302)
        :param url_names: List of url names (e.g. ['classname-edit', 'classname-delete', 'classname-detail'] )
        :param kwargs: dict e.g. {'pk': 1}
        :param prefix_urls: 'appname:'
        :param suffix_urls: query string, does not get evaluated '?parameter=value'
        :return:
        """
        for page in url_names:
            response = self.client.get(
                '{}{}'.format(reverse('{}{}'.format(prefix_urls, page), kwargs=kwargs), suffix_urls))
            self.assertEqual(response.status_code, expected_code,
                             'expected {} for {}, got {}'.format(expected_code, page, response.status_code))

    def test_all_pages(self):
        # TODO: when login in app is mandatory test it also:
        #response = self.client.post(reverse('login'), {'username': 'admin', 'password': 'admin'})
        #self.assertEqual(response.status_code, 302)

        # Pages without parameters
        self.assert_responses(
            expected_code=200,
            url_names=['capture-list','capture-add'],
            prefix_urls='captures:',
        )

        # Pages with parameter
        self.assert_responses(
            expected_code=200,
            url_names=['capture-detail', 'capture-edit', 'capture-delete'],
            prefix_urls='captures:',
            kwargs={'pk': self.capture1.pk},
        )

    def test_create_capture(self):
        with open('captures/test_data/smtp.pcap', mode='rb') as fp:
            response = self.client.post(reverse('captures:capture-add'),
                                    {'name':'SMTP', 'description':'My Own Upload', 'file':fp})
            print(response.content)
            self.assertEqual(response.status_code, 302)

