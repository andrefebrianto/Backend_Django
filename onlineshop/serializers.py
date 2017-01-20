from onlineshop.models import *
from rest_framework import serializers
from django.db.models import Max


class MerekSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merek
        fields = '__all__'


class PelangganSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pelanggan
        fields = '__all__'


class KecamatanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Kecamatan
        fields = '__all__'


class KotaSerializer(serializers.ModelSerializer):
    kecamatan = KecamatanSerializer(many=True, read_only=True)

    class Meta:
        model = Kota
        fields = '__all__'


class ProvinsiSerializer(serializers.ModelSerializer):
    kota  = KotaSerializer(many=True, read_only=True)
    
    class Meta:
        model = Provinsi
        fields = '__all__'


class AlamatSerializer(serializers.ModelSerializer):
    #kode_kecamatan = KecamatanSerializer(read_only=True)

    class Meta:
        model =  Alamat
        fields = '__all__'


class DiskonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historydiskon
        fields = ('kode_produk', 'besar_diskon')


class HargaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historyharga
        fields = ('kode_produk', 'harga')


class ProdukSerializer(serializers.ModelSerializer):
    hargabarang = serializers.SerializerMethodField('get_latest_harga')
    diskon = serializers.SerializerMethodField('get_latest_diskon')
    kode_merek = MerekSerializer(read_only=True)
    
    class Meta:
        model = Produk
        fields = '__all__'

    def get_latest_harga(self, kode_produk):
        return Produk.objects.values('hargabarang__kode_produk').annotate(latest_date=Max('hargabarang__waktuharga')).filter(kode_produk = kode_produk.kode_produk).annotate(latest_harga= Max('hargabarang__harga'))

    def get_latest_diskon(self, kode_produk):
        return Produk.objects.values('diskon__kode_produk').annotate(latest_date=Max('diskon__waktu_diskon')).filter(kode_produk = kode_produk.kode_produk).annotate(latest_diskon = Max('diskon__besar_diskon'))


class MetaProdukSerializer(serializers.ModelSerializer):
    hargabarang = serializers.SerializerMethodField('get_latest_harga')
    diskon = serializers.SerializerMethodField('get_latest_diskon')

    class Meta:
        model = Produk
        fields = ('kode_produk','nama_produk', 'hargabarang', 'diskon', 'gambar', 'stok')

    def get_latest_harga(self, kode_produk):
        return Produk.objects.values('hargabarang__kode_produk').annotate(latest_date=Max('hargabarang__waktuharga')).filter(kode_produk = kode_produk.kode_produk).annotate(latest_harga= Max('hargabarang__harga'))

    def get_latest_diskon(self, kode_produk):
        return Produk.objects.values('diskon__kode_produk').annotate(latest_date=Max('diskon__waktu_diskon')).filter(kode_produk = kode_produk.kode_produk).annotate(latest_diskon = Max('diskon__besar_diskon'))


class BarangPesananSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barangpesanan
        fields = '__all__'


class DetilBarangPesananSerializer(serializers.ModelSerializer):
    kode_produk = MetaProdukSerializer(read_only=True)

    class Meta:
        model = Barangpesanan
        fields = '__all__'


class PesananSerializer(serializers.ModelSerializer):
    barangpesanan = DetilBarangPesananSerializer(many=True, read_only=True)

    class Meta:
        model = Pesanan
        fields = '__all__'


class DaftarKeinginanSerializer(serializers.ModelSerializer):
    kode_produk = MetaProdukSerializer(read_only=True)
    #kode_produk = serializers.PrimaryKeyRelatedField(queryset=Produk.objects.all())

    class Meta:
        model = DaftarKeinginan
        fields = '__all__'


class BarangKeinginanSerializer(serializers.ModelSerializer):    

    class Meta:
        model = DaftarKeinginan
        fields = '__all__'


class PembayaranSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pembayaran
        fields = '__all__'


class PengirimanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pengiriman
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ProdukByMerekSerializer(serializers.ModelSerializer):
    produk = MetaProdukSerializer(many=True, read_only=True)

    class Meta:
        model = Merek
        fields = '__all__'


class KategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategori
        fields = '__all__'


class DikategorikanSerializer(serializers.ModelSerializer):
    kode_produk = MetaProdukSerializer(read_only=True)

    class Meta:
        model = Dikategorikan
        fields = ('kode_kategori', 'kode_produk')

class ProdukByKategoriSerializer(serializers.ModelSerializer):
    daftarbarang = DikategorikanSerializer(read_only=True, many=True)

    class Meta:
        model = Kategori
        fields = '__all__'