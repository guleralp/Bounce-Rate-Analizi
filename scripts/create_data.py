import pandas as pd
import numpy as np
import os

# Klasör oluştur
os.makedirs('data', exist_ok=True)

# Sabit tohum
np.random.seed(42)

# Sayfalar ve ziyaret sayısı
pages = ['Homepage', 'Pricing', 'About', 'Contact', 'Blog', 'Login', 'Signup', 'Dashboard']
n_visits = 1000

# Veri oluştur
data = {
    'user_id': np.random.randint(1000, 2000, n_visits),
    'page': np.random.choice(pages, n_visits, p=[0.25, 0.1, 0.1, 0.05, 0.2, 0.1, 0.1, 0.1]),
    'visit_duration_seconds': np.round(np.random.exponential(scale=30, size=n_visits), 1),
    'device': np.random.choice(['desktop', 'mobile'], n_visits),
    'page_load_time_sec': np.round(np.random.normal(loc=2.5, scale=1.0, size=n_visits), 2),
    'user_type': np.random.choice(['new', 'returning'], n_visits, p=[0.6, 0.4])
}

# DataFrame oluştur
df = pd.DataFrame(data)

# Bounce değerlerini hesapla
def generate_bounce(row):
    prob = 0.05  # taban oran
    if row['page_load_time_sec'] > 3:
        prob += 0.3  # Yavaş yüklenen sayfalarda bounce olasılığı yüksek
    if row['device'] == 'mobile':
        prob += 0.2  # Mobil cihazlarda bounce olasılığı yüksek
    if row['user_type'] == 'new':
        prob += 0.2  # Yeni kullanıcılarda bounce olasılığı yüksek
    if row['visit_duration_seconds'] < 10:
        prob += 0.4  # Kısa ziyaretlerde bounce olasılığı çok yüksek
    return np.random.rand() < prob

# Bounce değerlerini ekle
np.random.seed(42)  # Tekrarlanabilirlik için
df['is_bounce'] = df.apply(generate_bounce, axis=1).astype(int)

# CSV olarak kaydet
df.to_csv('data/yeni_veri.csv', index=False)

print("Veri oluşturuldu ve 'yeni_veri.csv' olarak kaydedildi. İlk 5 satır:")
print(df.head()) 