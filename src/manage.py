#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import subprocess
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.dev")

    if sys.argv[1].lower() == "test":
        print("NOTE: Running black formatter")
        subprocess.run(["black", "--config", ".black.toml", "."])
        subprocess.run(["isort", "."])

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()

#
# IaaS - infrastructure as a service
# PaaS - platform as a service (logging, database, cache ..., RDS, CloudWatch)
# SaaS - software as a service
#
#
# КВт/год - 1,68
#
# чайник (1кВат) -> годину -> КВт/год 1,68
# 100 Ват x 10 год = 1,68
#
#
# Потужність - Джоулі
#
# А - сила струму
# В - напруга
# Ом - опір
#
#
# 1 - 1 - 1 - 1 - 1 = 1
# 1 - 1 - 1 - 1 - 2 = 2
# 2 - 1 - 1 - 1 - 2 = 4
# 2 - 1 - 10 - 1 - 2 = 40
#
# # fF728&X'PSM=+ds5drQ.2*Ng
# # lmselemesovic@gmail.com
#
# """Free tier: In your first year includes 750 hours of t2.micro (or t3.micro in
# the Regions in which t2.micro is unavailable) instance usage on free tier AMIs per month,
#  30 GiB of EBS storage, 2 million IOs, 1 GB of snapshots, and 100 GB of bandwidth to the internet."""
#
# 750/2 =375.0
# 75