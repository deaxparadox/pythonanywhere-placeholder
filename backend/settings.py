import os


print("\nChecking environment...")

if os.getenv("PRODUCTION", 0):
    print("Production environment.\nLoading Production settings.\n")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings.production')
else:
    print("Local environment.\nLoading Local settings.\n")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings.local')

__all__ = []