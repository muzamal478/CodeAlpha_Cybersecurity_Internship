# Snort Setup Guide
1. Install Snort: `sudo apt install snort`
2. Add rules to `/etc/snort/rules/`
3. Run: `sudo snort -A console -q -c /etc/snort/snort.conf`