import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Veriyi oku
df = pd.read_csv('data/web_data.csv')

# Bounce yapan kullanıcıları filtrele
bounced_users = df[df['is_bounce'] == 1]

# Genel bounce oranı
toplam_ziyaret = len(df)
bounce_sayisi = len(bounced_users)
bounce_orani = (bounce_sayisi / toplam_ziyaret) * 100

print(f"\nGENEL BOUNCE ANALİZİ:")
print(f"Toplam ziyaret sayısı: {toplam_ziyaret}")
print(f"Bounce yapan ziyaret sayısı: {bounce_sayisi}")
print(f"Genel bounce oranı: %{bounce_orani:.2f}\n")

# Sayfalara göre detaylı analiz
print("\nSAYFALARA GÖRE DETAYLI BOUNCE ANALİZİ:")
for page in df['page'].unique():
    page_total = len(df[df['page'] == page])
    page_bounce = len(bounced_users[bounced_users['page'] == page])
    bounce_rate = (page_bounce / page_total) * 100
    print(f"\n{page}:")
    print(f"  Toplam ziyaret: {page_total}")
    print(f"  Bounce sayısı: {page_bounce}")
    print(f"  Bounce oranı: %{bounce_rate:.2f}")

# Cihaz tipine göre detaylı analiz
print("\nCİHAZ TİPİNE GÖRE DETAYLI BOUNCE ANALİZİ:")
for device in df['device'].unique():
    device_total = len(df[df['device'] == device])
    device_bounce = len(bounced_users[bounced_users['device'] == device])
    bounce_rate = (device_bounce / device_total) * 100
    print(f"\n{device}:")
    print(f"  Toplam ziyaret: {device_total}")
    print(f"  Bounce sayısı: {device_bounce}")
    print(f"  Bounce oranı: %{bounce_rate:.2f}")

# Kullanıcı tipine göre detaylı analiz
print("\nKULLANICI TİPİNE GÖRE DETAYLI BOUNCE ANALİZİ:")
for user_type in df['user_type'].unique():
    user_total = len(df[df['user_type'] == user_type])
    user_bounce = len(bounced_users[bounced_users['user_type'] == user_type])
    bounce_rate = (user_bounce / user_total) * 100
    print(f"\n{user_type}:")
    print(f"  Toplam ziyaret: {user_total}")
    print(f"  Bounce sayısı: {user_bounce}")
    print(f"  Bounce oranı: %{bounce_rate:.2f}")

# Görselleştirme
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
sns.countplot(data=bounced_users, x='page')
plt.title('Sayfalara Göre Bounce Sayısı')
plt.xticks(rotation=45)

plt.subplot(1, 2, 2)
sns.countplot(data=bounced_users, x='device')
plt.title('Cihaz Tipine Göre Bounce Sayısı')

plt.tight_layout()
plt.savefig("outputs/bounce_analysis.png")
plt.show() 