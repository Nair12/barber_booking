import unittest
import datetime
from unittest import TestCase


from django.core.files.uploadedfile import SimpleUploadedFile


from apps.core.models import Admin, Barber, BarbersPoint, Booking, PointImages
from apps.users.models import CustomUser


class ModelsUnittest(unittest.TestCase):

    def setUp(self):

        self.user1 = CustomUser.objects.create_user(username='barber1', password='pass123', role='barber')
        self.user2 = CustomUser.objects.create_user(username='admin1', password='pass123', role='admin')


        self.point = BarbersPoint.objects.create(address="Test Street 123", phone_number="+38084928828")


        self.barber = Barber.objects.create(
            user=self.user1,
            exp=5,
            phone="+380838922077",
            salary=1000.50,
            pict_url=SimpleUploadedFile(name='barber.jpg', content=b'', content_type='image/jpeg'),
            point=self.point
        )


        self.admin = Admin.objects.create(
            user=self.user2,
            patronymic="Admin1",
        )


        self.booking = Booking.objects.create(
            date_time=datetime.datetime.now(),
            user_phone="+22222222",
            name="Client Name",
            point=self.point,
            barber=self.barber
        )


        self.point_image = PointImages.objects.create(
            point_id=self.point,
            image=SimpleUploadedFile(name='point.jpg', content=b'', content_type='image/jpeg')
        )

    def test_barber_creation(self):
        barber = Barber.objects.get(id=self.barber.id)
        self.assertEqual(barber.user.username, self.user1.username)
        self.assertEqual(barber.exp, self.barber.exp)
        self.assertEqual(barber.point, self.point)

    def test_admin_creation(self):
        admin = Admin.objects.get(id=self.admin.id)
        self.assertEqual(admin.user.username, self.user2.username)
        self.assertEqual(admin.patronymic, self.admin.patronymic)

    def test_booking_creation(self):
        booking = Booking.objects.get(id=self.booking.id)
        self.assertEqual(booking.barber, self.barber)
        self.assertEqual(booking.point, self.point)
        self.assertEqual(booking.name, self.booking.name)

    def test_point_image_creation(self):
        img = PointImages.objects.get(id=self.point_image.id)
        self.assertEqual(img.point_id, self.point)

    def test_barberspoint_creation(self):
        point = BarbersPoint.objects.get(id=self.point.id)
        self.assertEqual(point.address, self.point.address)
        self.assertEqual(point.phone_number, self.point.phone_number)

    def test_update_barber(self):

        self.barber.phone = "+38084928828"
        self.barber.exp = 10
        self.barber.save()

        updated_barber = Barber.objects.get(id=self.barber.id)
        self.assertEqual(updated_barber.phone, "+38084928828")
        self.assertEqual(updated_barber.exp, 10)

    def test_delete_barber(self):
        barber_id = self.barber.id
        self.barber.delete()
        with self.assertRaises(Barber.DoesNotExist):
            Barber.objects.get(id=barber_id)



    def tearDown(self):
        Booking.objects.all().delete()
        PointImages.objects.all().delete()
        Barber.objects.all().delete()
        Admin.objects.all().delete()
        BarbersPoint.objects.all().delete()
        CustomUser.objects.all().delete()


if __name__ == "__main__":
    unittest.main()
