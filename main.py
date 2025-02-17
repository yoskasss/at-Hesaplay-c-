import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.integrate import solve_ivp
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FFMpegWriter

# Fiziksel parametreler
g = 9.81  # Yerçekimi ivmesi (m/s^2)
m = 0.5  # Yük kütlesi (kg)
Cd = 0.5  # Sürüklenme katsayısı (drag coefficient)
rho = 1.225  # Havanın yoğunluğu (kg/m^3)
A = 0.10  # Yükün kesit alanı (m^2)
r = np.array([-2, 0])  # Rüzgar hızı (x, y) m/s

# Uçağın başlangıç hız ve yükseklik değerleri
V_plane = 20  # Uçağın hızı (m/s)
h = 100  # Yük bırakma yüksekliği (m)

# Başlangıç değerlerini ekrana yazdırma
print("Simülasyon Başlangıç Değerleri:")
print(f"Yerçekimi ivmesi: {g} m/s^2")
print(f"Yük kütlesi: {m} kg")
print(f"Sürüklenme katsayısı: {Cd}")
print(f"Havanın yoğunluğu: {rho} kg/m^3")
print(f"Yükün kesit alanı: {A} m^2")
print(f"Rüzgar hızı: {r} m/s")
print(f"Uçağın hızı: {V_plane} m/s")
print(f"Bırakma yüksekliği: {h} m")

# Diferansiyel denklem sistemi tanımlanıyor
def dynamics(t, y):
    """Yükün hareket denklemleri."""
    vx, vy, x, y = y  # Mevcut hız ve konum değerleri alınıyor
    v = np.array([vx, vy]) - r  # Rüzgarın etkisi göz önünde bulundurularak hız vektörü hesaplanıyor
    v_mag = np.linalg.norm(v)  # Hızın büyüklüğü hesaplanıyor
    
    # Sürüklenme kuvveti hesaplanıyor (Newton’un hareket denklemleri kullanılarak)
    drag = 0.5 * rho * Cd * A * v_mag**2 / m * (-v / v_mag) if v_mag != 0 else np.array([0, 0])
    
    # İvme hesaplanıyor (Newton’un ikinci yasası)
    ax, ay = drag[0], drag[1] - g
    
    return [ax, ay, vx, vy]  # Diferansiyel denklemlerin türevleri döndürülüyor

# İlk koşullar (uçaktan bırakıldığı anki hız ve konum)
y0 = [V_plane, 0, 0, h]

# Simülasyon süresi (0 ile 10 saniye arasında hesaplanacak)
time_span = (0, 10)
t_eval = np.linspace(0, 10, 1000)  # 1000 zaman adımında çözüm bulunacak

# Diferansiyel denklemler çözülüyor
sol = solve_ivp(dynamics, time_span, y0, t_eval=t_eval, method='RK45')

# Uçağın rotasını belirle (x ekseni boyunca ilerleme)
x_plane = V_plane * sol.t
z_plane = np.full_like(sol.t, h)  # Uçağın yükseklik değeri sabit kalır

# Yükün yere düştüğü anı bul
idx_hit = np.where(sol.y[3] <= 0)[0][0]  # Y yere düştüğünde indisi bul

t_hit = sol.t[idx_hit]  # Yükün yere düştüğü zaman
y_hit = sol.y[2][idx_hit]  # Yükün yere düştüğü x konumu

# Uçaktan yükün bırakılması gereken konumu hesapla
x_release = y_hit - (V_plane * t_hit)
print(f"Yük, hedefe ulaşması için {x_release:.2f} metre önceden bırakılmalıdır.")

print("Video oluşturuluyor...")

# 2D Grafik çizimi
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(x_plane, z_plane, '--', label='Uçak Rotası', color='blue')  # Uçağın rotası
ax.plot(sol.y[2], sol.y[3], label='Yükün Yolu', color='orange')  # Yükün hareket yolu
ax.axhline(0, color='black', lw=1)  # Yere düşme çizgisi
ax.scatter([sol.y[2][-1]], [sol.y[3][-1]], color='red', label='İniş Noktası')  # Yükün yere düştüğü nokta
ax.set_xlabel('X Konumu (m)')
ax.set_ylabel('Y Konumu (m)')
ax.set_title('RC Uçaktan Yük Bırakma Simülasyonu (2D)')
ax.legend()
ax.grid()

# 3D Grafik çizimi
fig_3d = plt.figure(figsize=(10, 6))
ax_3d = fig_3d.add_subplot(111, projection='3d')
ax_3d.plot(x_plane, np.zeros_like(x_plane), z_plane, '--', label='Uçak Rotası', color='blue')  # Uçağın rotası
ax_3d.plot(sol.y[2], np.zeros_like(sol.y[2]), sol.y[3], label='Yükün Yolu', color='orange')  # Yükün hareket yolu
ax_3d.scatter([sol.y[2][-1]], [0], [sol.y[3][-1]], color='red', label='İniş Noktası')  # Yükün yere düştüğü nokta
ax_3d.scatter([0], [0], [h], color='blue', label='Uçak Konumu')  # Uçağın başlangıç noktası
ax_3d.set_xlabel('X Konumu (m)')
ax_3d.set_ylabel('Y Konumu (m)')
ax_3d.set_zlabel('Yükseklik (m)')
ax_3d.set_title('RC Uçaktan Yük Bırakma Simülasyonu (3D)')
ax_3d.legend()

# Animasyon oluştur
fig_anim, ax_anim = plt.subplots(figsize=(10, 5))
ax_anim.set_xlim(0, max(sol.y[2]) + 10)
ax_anim.set_ylim(0, h + 10)
ax_anim.set_xlabel('X Konumu (m)')
ax_anim.set_ylabel('Yükseklik (m)')
ax_anim.set_title('RC Uçaktan Yük Bırakma Simülasyonu (Animasyon)')
ax_anim.grid()

plane_line, = ax_anim.plot([], [], 'b--', label='Uçak Rotası')
load_line, = ax_anim.plot([], [], 'orange', label='Yükün Yolu')
plane_point, = ax_anim.plot([], [], 'bo', markersize=5, label='Uçak')
load_point, = ax_anim.plot([], [], 'ro', markersize=5, label='Yük')
ax_anim.legend()

def update(frame):
    if frame < len(sol.t):
        plane_line.set_data(x_plane[:frame], z_plane[:frame])
        load_line.set_data(sol.y[2][:frame], sol.y[3][:frame])
        plane_point.set_data([x_plane[frame]], [z_plane[frame]])  # Tek elemanlı liste
        load_point.set_data([sol.y[2][frame]], [sol.y[3][frame]])  # Tek elemanlı liste
    return plane_line, load_line, plane_point, load_point

ani = animation.FuncAnimation(fig_anim, update, frames=len(sol.t), interval=10, blit=True)

# MP4 olarak kaydetme
writer = FFMpegWriter(fps=30, metadata=dict(artist='Me'), bitrate=1800)
ani.save("rc_plane_drop.mp4", writer=writer)
plt.show()
