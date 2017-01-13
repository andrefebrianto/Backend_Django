from django.conf.urls import url, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'user', PelangganViewSet)
router.register(r'pembayaran', PembayaranViewSet)
router.register(r'pesanan', PesananViewSet, base_name="PesananUser")
router.register(r'barangpesanan', BarangPesananViewSet)
#router.register(r'kota', KotaViewSet)
#router.register(r'kecamatan', KecamatanViewSet)
router.register(r'provinsi', ProvinsiViewSet, base_name="ListProvinsi")
router.register(r'alamatpengguna', AlamatViewSet)
router.register(r'detilproduk', ProdukViewSet)
#router.register(r'kategori', KategoriViewSet)
router.register(r'produkbykategori', ProdukByKategoriViewSet, base_name="ProdukByKategori")
router.register(r'produkbymerek', ProdukByMerekViewSet, base_name="ProdukByMerek")
router.register(r'daftarkeinginan', DaftarKeinginanViewSet, base_name="Wishlist")

urlpatterns = [
	url(r'^docs/', include('rest_framework_docs.urls')),
#	url(r'^produkbykategori/$', ProdukByKategoriViewSet.as_view()),
	url(r'^(?P<pk>[0-9]+)/detail$', ProdukViewSet),
]
urlpatterns += router.urls