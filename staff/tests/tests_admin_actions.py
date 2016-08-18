from django.core import mail
from django.test import Client, TestCase
from django.urls import reverse

from django.contrib.auth.models import User
from django.contrib import messages

from django.utils.translation import ugettext_lazy as _

class SendFillformMail(TestCase):
    fixtures = ['ophasebase.json', 'staff.json', 'students.json', 'persons.json']

    def setUp(self):
        # Create the testuser
        self.__testuser = 'testuser'
        self.__testpw = 'test'

        u = User.objects.create_superuser(username=self.__testuser,
                                     password=self.__testpw,
                                     email='test@example.com')

        u.save()

    def test_send_fillform_email(self):
        """Sends Fillform information to a set of users"""
        c = Client()

        # login returns True on success
        self.assertTrue(c.login(username=self.__testuser, password=self.__testpw))

        # the url of the view
        change_url = reverse('admin:staff_person_changelist')

        self.assertEquals(len(mail.outbox), 0)
        recipient = [5,6,7]
        response = c.post(change_url, {'action': 'send_fillform_mail',
                                       '_selected_action': recipient},
                          follow=True)

        # If the post work we get back to the view via a redirect
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, change_url)

        # One email per recipient was sent
        self.assertEquals(len(mail.outbox), len(recipient))
        # Registerview url is in the email message body
        self.assertTrue(reverse('staff:registration') in mail.outbox[0].body)

        # that the message was displayed to the admin
        msgs = list(response.context['messages'])
        self.assertEquals(len(msgs), 1)
        self.assertEquals(msgs[0].level, messages.SUCCESS)