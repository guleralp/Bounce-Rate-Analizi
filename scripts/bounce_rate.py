import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Veriyi okuma:
df = pd.read_csv('data/yeni_veri.csv')

# Grafik : Sayfa bazında bounce oranı
page_bounce = df.groupby('page')['is_bounce'].mean().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(x=page_bounce.values, y=page_bounce.index, palette="Reds_r")
plt.title("Sayfa Bazında Bounce Oranı")
plt.xlabel("Bounce Oranı")
plt.ylabel("Sayfa")
plt.tight_layout()
plt.savefig("outputs/page_bounce_rate.png")
plt.show()

# Grafik :Her sayfa için toplam ziyaret ve bounce sayısı
page_stats = df.groupby("page").agg(
    total_visits=('is_bounce', 'count'),
    total_bounces=('is_bounce', 'sum')
).reset_index()

plt.figure(figsize=(12,6))
page_stats_sorted = page_stats.sort_values(by="total_visits", ascending=False)
sns.barplot(data=page_stats_sorted, x="page", y="total_visits", color="lightblue", label="Ziyaret")
sns.barplot(data=page_stats_sorted, x="page", y="total_bounces", color="red", label="Bounce")

plt.xticks(rotation=45)
plt.legend()
plt.title("Sayfa Bazlı Ziyaret ve Bounce Sayısı")
plt.ylabel("Adet")
plt.xlabel("Sayfa")
plt.tight_layout()
plt.savefig("outputs/total_visits_bounce_rate.png")
plt.show()

# Grafik : Cihaza göre bounce oranı
device_bounce = df.groupby('device')['is_bounce'].mean()

plt.figure(figsize=(6, 4))
sns.barplot(x=device_bounce.index, y=device_bounce.values, palette="Blues_d")
plt.title("Cihaza Göre Bounce Oranı")
plt.ylabel("Bounce Oranı")
plt.tight_layout()
plt.savefig("outputs/bounce_rate_by_device.png")
plt.show()

# Grafik : Sayfa yüklenme süresi ile bounce ilişkisi
plt.figure(figsize=(8, 6))
sns.regplot(x='page_load_time_sec', y='is_bounce', data=df, scatter_kws={'alpha': 0.2}, line_kws={"color": "red"})
plt.title("Yükleme Süresi ile Bounce Oranı")
plt.xlabel("Sayfa Yükleme Süresi (sn)")
plt.ylabel("Bounce (1 = Evet)")
plt.tight_layout()
plt.savefig("outputs/load_time_and_bounce_rate.png")
plt.show()

# İstatistiksel Analizler
from scipy.stats import ttest_ind, chi2_contingency

# T-testi
group1 = df[df["is_bounce"] == 1]["page_load_time_sec"]
group2 = df[df["is_bounce"] == 0]["page_load_time_sec"]
t_stat, p_value = ttest_ind(group1, group2, equal_var=False)

print("\nT-testi Sonucu")
print(f"Test istatistiği: {t_stat:.3f}")
print(f"P-değeri: {p_value:.5f}")
if p_value < 0.05:
    print("Yüklenme süresi ile bounce arasında istatistiksel olarak anlamlı fark var.")
else:
    print("Yüklenme süresi ile bounce arasında anlamlı fark yok.")

# Ki-Kare Testi
contingency_table = pd.crosstab(df["user_type"], df["is_bounce"])
chi2, p, dof, expected = chi2_contingency(contingency_table)

print("\nKi-Kare Testi Sonucu")
print(f"Chi2 değeri: {chi2:.3f}")
print(f"P-değeri: {p:.5f}")
if p < 0.05:
    print("Kullanıcı tipi ile bounce arasında anlamlı ilişki var.")
else:
    print("Kullanıcı tipi ile bounce arasında anlamlı ilişki yok.")

# Korelasyon Matrisi
df_corr = df[['visit_duration_seconds', 'page_load_time_sec', 'is_bounce']]
plt.figure(figsize=(8, 6))
sns.heatmap(df_corr.corr(), annot=True, cmap='coolwarm')
plt.title("Korelasyon Matrisi")
plt.tight_layout()
plt.savefig("outputs/Correlation_Matrix.png")
plt.show()

