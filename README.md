# systemcheck
Simple scripts for checking system functions

Check Samba Status:
What: Verify if Samba (smbd) is running and accessible.
Why: Ensures your share (/home/amherscher/Desktop/shared) is live—vital for SMB file access.

Fetch Public IP:
What: Get the linuxserver’s public IP (e.g., 68.57.233.165 or 136.144.19.222 with VPN).
Why: Tracks network state—key for remote Samba (smb://68.57.233.165/Shared).

Monitor Disk Space:
What: Check free space on critical directories (e.g., /home, /).
Why: Prevents server issues—SMBs need proactive monitoring.

Test Network Connectivity:
What: Ping a known host (e.g., 8.8.8.8) and your Deco router (192.168.68.1).
Why: Confirms network health—essential for sysadmin diagnostics.

Report System Load:
What: Get CPU and memory usage stats.
Why: Spots performance bottlenecks—keeps linuxserver reliable post-install.

Verify Firewall Rules:
What: List active firewall settings (e.g., 445/tcp for Samba).
Why: Ensures security and access—critical for your remote setup.
