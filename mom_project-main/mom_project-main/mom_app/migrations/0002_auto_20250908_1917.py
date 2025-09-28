from django.db import migrations

def create_demo_users(apps, schema_editor):
    User = apps.get_model("mom_app", "User")
    demo_users = [
        ("faculty1", "faculty"),
        ("coursecoord", "course_coordinator"),
        ("modulecoord", "module_coordinator"),
        ("pacmember", "pac"),
        ("dfbmember", "dfb"),
        ("cdcchair", "cdc"),
    ]
    for username, role in demo_users:
        if not User.objects.filter(username=username).exists():
            User.objects.create_user(
                username=username,
                password="password123",
                role=role
            )

def delete_demo_users(apps, schema_editor):
    User = apps.get_model("mom_app", "User")
    User.objects.filter(username__in=[
        "faculty1", "coursecoord", "modulecoord", "pacmember", "dfbmember", "cdcchair"
    ]).delete()

class Migration(migrations.Migration):
    dependencies = [
        ("mom_app", "0001_initial"),
    ]
    operations = [
        migrations.RunPython(create_demo_users, delete_demo_users),
    ]

