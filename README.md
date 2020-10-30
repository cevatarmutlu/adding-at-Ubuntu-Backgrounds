
## Girizgâh
Muhtemelen bu yazıyı benden başka kimse okumayacak. Okusa bile beni takip eden bir kaç kişi olacak ve belki de "bu çocuk yine saçma sapan şeylerle uğraşıyor" diyecekler. Bilmiyorum.

__Projenin Çıkıs Noktası__

Bir Linux dağıtımı olan Ubuntu' nun 20.04 sürümüne geçtim. Sürümün varsayılan olarak gelen temasını gerçekten beğendim. Sürümle beraber gelen duvar kağıtlarını da beğendim. 

Kendi indirdiğim duvar kağıtları da varsayılan duvar kağıtlarıyla beraber görünse - ayrı bir yerde görünüyorlar- ve hepsi varsayılan slideshow' a -gerçek adını bilmiyorum. Belli süre sonra başka wallpaper' a geçmek- eklense diye içimden geçirdim.

Bu satırları okuduğunuza göre -yani umarım- bu isteği gerçekleştirmeye çalışmışım demektir.

<br/>

## Projenin yapılması ile ilgili bilgiler

Ubuntu' da ekrana sağ tıklayıp `Change Background` tuşuna tıkladığınız zaman görünen wallpaperlar aşağıdaki `XML` dosyasında tutulur.

    /usr/share/gnome-background-properties/focal-wallpapers.xlm 

Bu dosyaya elle ekleme yaparak kendinizde bu işi yapabilirsiniz.

---

Benim slideshow dediğim şeyin bulunduğu `XML` dosyası aşağıdaki yoldadır.

```bash
    /usr/share/backgrounds/contest/focal.xml

    /usr/share/backgrounds/ # bu dosya yolunda default wallpaperlar bulunmaktadır
```

Bu dosyaları açarsanız ne yapmanız gerektiğini anlarsınız zaten.

## Kurulum

Yapmanız gereken tek şey sadece projeyi indirmek. Ek olarak bir şey kurmanıza gerek yok.


## Kullanım

> Proje dosyasında orjinal XML dosyaları bulunmaktadır. Canınız istediğinde tekrar eski yapıya dönebilirsiniz.

1. Bütün Wallpaper' ların bulunacağı klasör `main.py` dosyadaki `wallpapers_folder_path` değişkenine atayabilirsiniz. Default olarak `~/Pictures/wallpapers/`
2. İndirdiğiniz Wallpaperları bir klasörün içine atın ve klasörün dosya yolunu `main.py` dosyasının içindeki `wallpapers_currrent_path` değişkenine atayın.
3. Daha sonra `main.py` dosyasını çalıştırın.

~~Not: Wallpaperları tuttuğunuz klasörün içine yeni wallpaperlar eklediğinizde öncekilerle beraber yenileri de XML dosyalarına ekleyecektir.~~

<span style='font-size: 20px'>*Gerek görürsem ya da canım isterse geliştirebilirim*</span>