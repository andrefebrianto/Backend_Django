from django.conf.urls import url, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'datapelanggan', PelangganViewSet, base_name="DataPelanggan")
router.register(r'pembayaran', PembayaranViewSet)
router.register(r'daftarpesanan', PesananViewSet, base_name="PesananUser")
router.register(r'barangpesanan', BarangPesananViewSet)
router.register(r'provinsi', ProvinsiViewSet, base_name="ListProvinsi")
router.register(r'alamatpengguna', AlamatViewSet)
router.register(r'detilproduk', ProdukViewSet, base_name="DetilProduk")
router.register(r'produkbykategori', ProdukByKategoriViewSet, base_name="ProdukByKategori")
router.register(r'produkbymerek', ProdukByMerekViewSet, base_name="ProdukByMerek")
router.register(r'daftarkeinginan', DaftarKeinginanViewSet, base_name="Wishlist")
router.register(r'barangkeinginan', BarangKeinginanViewSet)
router.register(r'kategori', KategoriViewSet)
router.register(r'merek', MerekViewSet)

urlpatterns = [
	url(r'^docs/', include('rest_framework_docs.urls')),
	url(r'^(?P<pk>[0-9]+)/detail$', ProdukViewSet),
]
urlpatterns += router.urls