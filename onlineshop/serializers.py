from onlineshop.models import *
from rest_framework import serializers


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
    kode_kecamatan = KecamatanSerializer(read_only=True)

    class Meta:
        model =  Alamat
        fields = '__all__'


class BarangPesananSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barangpesanan
        fields = '__all__'


class PesananSerializer(serializers.ModelSerializer):
    barangpesanan = BarangPesananSerializer(many=True, read_only=True)

    class Meta:
        model = Pesanan
        fields = '__all__'


class DiskonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historydiskon
        fields = ('__all__')


class HargaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historyharga
        fields = ('__all__')


class ProdukSerializer(serializers.ModelSerializer):
    hargabarang = HargaSerializer(many=True, read_only=True)
    diskon = DiskonSerializer(many=True, read_only=True)
    
    class Meta:
        model = Produk
        fields = '__all__'


class MetaProdukSerializer(serializers.ModelSerializer):
    hargabarang = HargaSerializer(many=True, read_only=True)
    diskon = DiskonSerializer(many=True, read_only=True)

    class Meta:
        model = Produk
        fields = ('kode_produk','nama_produk', 'hargabarang', 'diskon', 'stok')


class DaftarKeinginanSerializer(serializers.ModelSerializer):
    kode_produk = MetaProdukSerializer(read_only=True)

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