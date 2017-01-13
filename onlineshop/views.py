from onlineshop.models import *
from onlineshop.serializers import *
from rest_framework import viewsets, generics

class HistoryHargaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Historyharga.objects.all()
    serializer_class = HargaSerializer


class HistoryDiskonViewSet(viewsets.ModelViewSet):
    queryset = Historydiskon.objects.all()
    serializer_class = DiskonSerializer


class ProdukViewSet(viewsets.ModelViewSet):
    queryset = Produk.objects.all()
    serializer_class = ProdukSerializer


class PelangganViewSet(viewsets.ModelViewSet):
    queryset = Pelanggan.objects.all()
    serializer_class = PelangganSerializer


class PembayaranViewSet(viewsets.ModelViewSet):
    queryset = Pembayaran.objects.all()
    serializer_class = PembayaranSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class PesananViewSet(viewsets.ModelViewSet):
    serializer_class = PesananSerializer

    def get_queryset(self):
        queryset = Pesanan.objects.all()
        kode_pesanan = self.request.query_params.get('kode_pesanan', None)
        pemesan = self.request.query_params.get('email_pemesan', None)
        if kode_pesanan is not None:
            queryset = queryset.filter(kode_pesanan=kode_pesanan)
        if pemesan is not None:
            queryset = queryset.filter(email=pemesan)
        return queryset


class BarangPesananViewSet(viewsets.ModelViewSet):
    queryset = Barangpesanan.objects.all()
    serializer_class = BarangPesananSerializer


class KotaViewSet(viewsets.ModelViewSet):
    queryset = Kota.objects.all()
    serializer_class = KotaSerializer


class KecamatanViewSet(viewsets.ModelViewSet):
    queryset = Kecamatan.objects.all()
    serializer_class = KecamatanSerializer


class ProvinsiViewSet(viewsets.ModelViewSet):   
    serializer_class = ProvinsiSerializer

    def get_queryset(self):
        queryset = Provinsi.objects.all()
        nama_provinsi = self.request.query_params.get('nama_provinsi', None)
        if nama_provinsi is not None:
            queryset = queryset.filter(nama_provinsi=nama_provinsi)
        return queryset


class AlamatViewSet(viewsets.ModelViewSet):
    queryset = Alamat.objects.all()
    serializer_class = AlamatSerializer


class ProdukByMerekViewSet(viewsets.ModelViewSet):
    serializer_class = ProdukByMerekSerializer

    def get_queryset(self):
        queryset = Merek.objects.all()
        nama_merek = self.request.query_params.get('nama_merek', None)
        kode_merek = self.request.query_params.get('kode_merek', None)
        if nama_merek is not None:
            queryset = queryset.filter(nama_merek=nama_merek)
        if kode_merek is not None:
            queryset = queryset.filter(kode_merek=kode_merek)
        return queryset


class ProdukByKategoriViewSet(viewsets.ModelViewSet):
    serializer_class = ProdukByKategoriSerializer

    def get_queryset(self):
        queryset = Kategori.objects.all()
        kode_kategori = self.request.query_params.get('kode_kategori', None)
        nama_kategori = self.request.query_params.get('nama_kategori', None)
        if kode_kategori is not None:
            queryset = queryset.filter(kode_kategori=kode_kategori)
        if nama_kategori is not None:
            queryset = queryset.filter(nama_kategori=nama_kategori)
        return queryset


class KategoriViewSet(viewsets.ModelViewSet):
    queryset = Kategori.objects.all()
    serializer_class = KategoriSerializer


class MerekViewSet(viewsets.ModelViewSet):
    queryset = Merek.objects.all()
    serializer_class = MerekSerializer

class DaftarKeinginanViewSet(viewsets.ModelViewSet):    
    serializer_class = DaftarKeinginanSerializer

    def get_queryset(self):
        queryset = DaftarKeinginan.objects.all()
        user = self.request.query_params.get('email_pengguna', None)
        if user is not None:
            queryset = queryset.filter(email=user)
        return queryset