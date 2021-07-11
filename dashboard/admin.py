from django.contrib import admin
from .models.user import User
from .models.booking import Booking
from .models.payment_type import PaymentType
from .models.payment import Payment
from .models.receptionist import Receptionist
from .models.reservation import Reservation
from .models.room_status import RoomStatus
from .models.room_type import RoomType
from .models.room import Room
from .models.checking import Checking


admin.site.register((User, Booking, Checking, PaymentType, Payment, Receptionist, Reservation, RoomStatus, RoomType, Room))
