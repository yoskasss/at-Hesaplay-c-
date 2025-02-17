# RC Uçaktan Yük Bırakma Simülasyonu

Bu proje, bir RC uçağından yük bırakma simülasyonunu gerçekleştiren bir Python uygulamasıdır. Uçak, belirli bir yükseklikten bir yük bırakır ve yükün rüzgar, sürüklenme kuvveti ve yerçekimi etkisiyle yere düşme hareketi simüle edilir. Simülasyon sonucunda yükün yere düştüğü noktaya ulaşmak için uçaktan ne kadar önce bırakılması gerektiği hesaplanır.

## İçindekiler
- [Proje Hakkında](#proje-hakkında)
- [Kurulum](#kurulum)
- [Kullanım](#kullanım)
- [Parametreler](#parametreler)
- [Çıktılar](#çıkılar)


## Proje Hakkında

Bu simülasyon, uçaktan bırakılan bir yükün hareketini ve bu yükün yere düşme sürecini modellemektedir. Simülasyon fiziksel parametreler (yerçekimi, rüzgar hızı, sürüklenme katsayısı vb.) ve başlangıç koşulları (uçak hızı, yükseklik) ile gerçekleştirilir. 

### Özellikler:
- 2D ve 3D görselleştirmeler
- Yükün yere düştüğü an ve uçaktan bırakılması gereken konum hesaplamaları
- Sürüklenme kuvveti ve rüzgar etkilerinin modellenmesi

## Kurulum

Proje, aşağıdaki Python kütüphanelerini kullanmaktadır:
- `numpy`
- `matplotlib`
- `scipy`

Gerekli bağımlılıkları kurmak için terminal üzerinden aşağıdaki komutu çalıştırabilirsiniz:

```bash
pip install numpy matplotlib scipy
```
## Kullanım

  Simülasyonu çalıştırmak için Python dosyasını (simulasyon.py) çalıştırabilirsiniz.
    Çalıştırma sonrasında uçak rotası, yükün yolu ve yükün yere düşme noktası görselleştirilir.
    Simülasyon sonuçları, yükün yere düşme zamanı ve uçaktan ne kadar önce bırakılması gerektiği bilgilerini içerir.

```bash
python main.py
```
## Parametreler

Aşağıdaki parametreler, simülasyonun başlangıç koşullarını belirler:
```
    g: Yerçekimi ivmesi (m/s²) - Varsayılan: 9.81 m/s²
    m: Yük kütlesi (kg) - Varsayılan: 0.5 kg
    Cd: Sürüklenme katsayısı - Varsayılan: 0.5
    rho: Havanın yoğunluğu (kg/m³) - Varsayılan: 1.225 kg/m³
    A: Yükün kesit alanı (m²) - Varsayılan: 0.1 m²
    r: Rüzgar hızı (m/s) - Varsayılan: [-2, 0] (X ve Y yönünde)
    V_plane: Uçağın hızı (m/s) - Varsayılan: 20 m/s
    h: Bırakma yüksekliği (m) - Varsayılan: 100 m
```

## Çıktılar

Simülasyon, yükün yere düştüğü noktayı ve uçağın hangi noktada yükü bırakması gerektiğini hesaplar. Ayrıca, 2D ve 3D grafiklerle uçak rotası ve yükün hareketi görselleştirilir. Aşağıdaki çıktılar üretilir:

  rc_plane_drop.mp4: Uçağın ve yükün hareketini gösteren bir animasyon.
    Yükün yere düştüğü konum ve uçağın ne kadar önce yükü bırakması gerektiği bilgisi.
