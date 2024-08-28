import os
import django

# ตั้งค่าการทำงานของ Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api.settings")
django.setup()

from weatherstack.models import apilogin

def test_read_model():
    # ดึงข้อมูลทั้งหมด
    all_entries = apilogin.objects.all()
    for entry in all_entries:
        print(entry.name ,entry.url ,entry.pwd)

    # ดึงข้อมูลตามเงื่อนไข
    # specific_entry = apilogin.objects.filter(name='"weatherstack_current"').first()
    # if specific_entry:
    #     print(specific_entry.name, specific_entry.created_at)

if __name__ == "__main__":
    test_read_model()
