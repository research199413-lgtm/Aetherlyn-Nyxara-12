from datetime import datetime, timezone
import pytz

# ======================
# Timezones
# ======================
UTC = pytz.utc
PKT = pytz.timezone("Asia/Karachi")

# ======================
# Expected run time (GitHub Actions uses UTC cron)
# ======================
expected_utc = datetime.now(UTC)

# ======================
# Actual run time (when script executes)
# ======================
actual_utc = datetime.now(UTC)

# Convert to Pakistan Time
expected_pkt = expected_utc.astimezone(PKT)
actual_pkt = actual_utc.astimezone(PKT)

# ======================
# Output
# ======================
print("\n==============================")
print("GitHub Actions Time Check")
print("==============================")

print(f"Expected UTC Time : {expected_utc.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Actual UTC Time   : {actual_utc.strftime('%Y-%m-%d %H:%M:%S')}")

print("\n--- Pakistan Time (PKT) ---")
print(f"Expected PKT Time : {expected_pkt.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Actual PKT Time   : {actual_pkt.strftime('%Y-%m-%d %H:%M:%S')}")

print("\nNOTE:")
print("- GitHub cron runs in UTC")
print("- PKT = UTC +5 hours")
print("==============================\n")
