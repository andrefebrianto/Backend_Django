# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Alamat(models.Model):
    email = models.ForeignKey('Pelanggan', models.DO_NOTHING, db_column='EMAIL', primary_key=True)  # Field name made lowercase.
    kode_kota = models.ForeignKey('Kota', models.DO_NOTHING, db_column='KODE_KOTA')  # Field name made lowercase.
    kode_provinsi = models.ForeignKey('Provinsi', models.DO_NOTHING, db_column='KODE_PROVINSI')  # Field name made lowercase.
    kode_kecamatan = models.ForeignKey('Kecamatan', models.DO_NOTHING, db_column='KODE_KECAMATAN')  # Field name made lowercase.
    alamat_lengkap = models.CharField(db_column='ALAMAT_LENGKAP', max_length=150)  # Field name made lowercase.
    kode_pos = models.CharField(db_column='KODE_POS', max_length=5)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'alamat'

    def __str__(self):
        return '%s, %s, %s' % (self.alamat_lengkap, kode_kota)


class Barangpesanan(models.Model):
    id_barang_pesanan = models.AutoField(primary_key=True)
    kode_pesanan = models.ForeignKey('Pesanan', models.DO_NOTHING, db_column='KODE_PESANAN')  # Field name made lowercase.
    kode_produk = models.ForeignKey('Produk', models.DO_NOTHING, db_column='KODE_PRODUK')  # Field name made lowercase.
    kuantitas = models.DecimalField(db_column='KUANTITAS', max_digits=8, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'barangpesanan'
        unique_together = (('kode_pesanan', 'kode_produk'),)

    def __str__(self):
        return '%s, %s - %s' % (self.kode_pesanan, kode_produk, kuantitas)


class DaftarKeinginan(models.Model):
    id_daftar_keinginan = models.AutoField(primary_key=True)
    email = models.ForeignKey('Pelanggan', models.DO_NOTHING, db_column='EMAIL')  # Field name made lowercase.
    kode_produk = models.ForeignKey('Produk', models.DO_NOTHING, db_column='KODE_PRODUK')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'daftar_keinginan'
        unique_together = (('email', 'kode_produk'),)

    def __str__(self):
        return self.kode_produk


class Dikategorikan(models.Model):
    id_pengategorian = models.AutoField(primary_key=True)
    kode_kategori = models.ForeignKey('Kategori', models.DO_NOTHING, db_column='KODE_KATEGORI')  # Field name made lowercase.
    kode_produk = models.ForeignKey('Produk', models.DO_NOTHING, db_column='KODE_PRODUK')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dikategorikan'
        unique_together = (('kode_kategori', 'kode_produk'),)

    def __str__(self):
        return '%s - %s' % (self.kode_kategori, kode_produk)


class Historydiskon(models.Model):
    id_diskon = models.AutoField(primary_key=True)
    kode_produk = models.ForeignKey('Produk', models.DO_NOTHING, db_column='KODE_PRODUK')  # Field name made lowercase.
    waktu_diskon = models.DateTimeField(db_column='WAKTU_DISKON')  # Field name made lowercase.
    besar_diskon = models.DecimalField(db_column='BESAR_DISKON', max_digits=8, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'historydiskon'
        unique_together = (('kode_produk', 'waktu_diskon'),)

    def  __str__(self):
        return '%s - %s' % (self.kode_produk, besar_diskon)


class Historyharga(models.Model):
    id_harga = models.AutoField(primary_key=True)
    kode_produk = models.ForeignKey('Produk', models.DO_NOTHING, db_column='KODE_PRODUK')  # Field name made lowercase.
    waktuharga = models.DateTimeField(db_column='WAKTUHARGA')  # Field name made lowercase.
    harga = models.DecimalField(db_column='HARGA', max_digits=8, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'historyharga'
        unique_together = (('kode_produk', 'waktuharga'),)

    def __str__(self):
        return '%s - %s' % (self.kode_produk, harga)


class Kategori(models.Model):
    kode_kategori = models.CharField(db_column='KODE_KATEGORI', primary_key=True, max_length=5)  # Field name made lowercase.
    nama_kategori = models.CharField(db_column='NAMA_KATEGORI', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kategori'

    def __str__(self):
        return self.nama_kategori


class Kecamatan(models.Model):
    kode_kecamatan = models.IntegerField(db_column='KODE_KECAMATAN', primary_key=True)  # Field name made lowercase.
    nama_kecamatan = models.CharField(db_column='NAMA_KECAMATAN', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kecamatan'

    def __str__(self):
        return self.nama_kecamatan


class Kota(models.Model):
    kode_kota = models.IntegerField(db_column='KODE_KOTA', primary_key=True)  # Field name made lowercase.
    nama_kota = models.CharField(db_column='NAMA_KOTA', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kota'

    def __str__(self):
        return self.nama_kota


class Merek(models.Model):
    kode_merek = models.CharField(db_column='KODE_MEREK', primary_key=True, max_length=5)  # Field name made lowercase.
    nama_merek = models.CharField(db_column='NAMA_MEREK', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'merek'

    def __str__(self):
        return self.nama_merek


class Pelanggan(models.Model):
    nama_lengkap = models.CharField(db_column='NAMA_LENGKAP', max_length=50)  # Field name made lowercase.
    tanggal_lahir = models.DateField(db_column='TANGGAL_LAHIR')  # Field name made lowercase.
    nomor_hp = models.CharField(db_column='NOMOR_HP', max_length=12)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', primary_key=True, max_length=50)  # Field name made lowercase.
    kata_sandi = models.CharField(db_column='KATA_SANDI', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pelanggan'

    def __str__(self):
        return self.nama_lengkap + ' -- ' + self.email


class Pembayaran(models.Model):
    kode_pembayaran = models.CharField(db_column='KODE_PEMBAYARAN', primary_key=True, max_length=12)  # Field name made lowercase.
    kode_pesanan = models.ForeignKey('Pesanan', models.DO_NOTHING, db_column='KODE_PESANAN')  # Field name made lowercase.
    waktu_pembayaran = models.DateTimeField(db_column='WAKTU_PEMBAYARAN')  # Field name made lowercase.
    total_belanja = models.DecimalField(db_column='TOTAL_BELANJA', max_digits=8, decimal_places=0)  # Field name made lowercase.
    status_pembayaran = models.IntegerField(db_column='STATUS_PEMBAYARAN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pembayaran'

    def __str__(self):
        return '%s - %s' % (self.kode_pembayaran, kode_pesanan)


class Pesanan(models.Model):
    kode_pesanan = models.CharField(db_column='KODE_PESANAN', primary_key=True, max_length=15)  # Field name made lowercase.
    kode_pembayaran = models.ForeignKey(Pembayaran, models.DO_NOTHING, db_column='KODE_PEMBAYARAN', blank=True, null=True)  # Field name made lowercase.
    email = models.ForeignKey(Pelanggan, models.DO_NOTHING, db_column='EMAIL')  # Field name made lowercase.
    waktu_pesanan = models.DateTimeField(db_column='WAKTU_PESANAN')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pesanan'

    def __str__(self):
        return self.kode_produk + ' ' + self.waktu_pesanan


class Produk(models.Model):
    kode_produk = models.CharField(db_column='KODE_PRODUK', primary_key=True, max_length=10)  # Field name made lowercase.
    kode_merek = models.ForeignKey(Merek, models.DO_NOTHING, db_column='KODE_MEREK')  # Field name made lowercase.
    nama_produk = models.CharField(db_column='NAMA_PRODUK', max_length=50)  # Field name made lowercase.
    material = models.CharField(db_column='MATERIAL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    deskripsi_produk = models.CharField(db_column='DESKRIPSI_PRODUK', max_length=500, blank=True, null=True)  # Field name made lowercase.
    negara_pemroduksi = models.CharField(db_column='NEGARA_PEMRODUKSI', max_length=30, blank=True, null=True)  # Field name made lowercase.
    gambar = models.TextField(db_column='GAMBAR', blank=True, null=True)  # Field name made lowercase.
    stok = models.DecimalField(db_column='STOK', max_digits=8, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'produk'

    def __str__(self):
        return self.kode_produk + ' ' + self.nama_produk


class Provinsi(models.Model):
    kode_provinsi = models.IntegerField(db_column='KODE_PROVINSI', primary_key=True)  # Field name made lowercase.
    nama_provinsi = models.CharField(db_column='NAMA_PROVINSI', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'provinsi'

    def __str__(self):
        return self.nama_provinsi


class Review(models.Model):
    id_review = models.AutoField(primary_key=True)
    kode_produk = models.ForeignKey(Produk, models.DO_NOTHING, db_column='KODE_PRODUK')  # Field name made lowercase.
    email_review = models.CharField(db_column='EMAIL_REVIEW', max_length=50)  # Field name made lowercase.
    judul_review = models.CharField(db_column='JUDUL_REVIEW', max_length=100)  # Field name made lowercase.
    isi = models.CharField(db_column='ISI', max_length=300)  # Field name made lowercase.
    rating_kualitas = models.DecimalField(db_column='RATING_KUALITAS', max_digits=8, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    rating_tampilan = models.DecimalField(db_column='RATING_TAMPILAN', max_digits=8, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    rating_harga = models.DecimalField(db_column='RATING_HARGA', max_digits=8, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'review'
        unique_together = (('kode_produk', 'email_review'),)

    def __str__(self):
        return self.kode_produk + ' ' + self.judul_review