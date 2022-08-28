SELECT
 ms_pelanggan.kode_pelanggan,
 ms_pelanggan.nama_pelanggan,
 SUM(tr_penjualan_detail.qty*tr_penjualan_detail.harga_satuan) AS total_harga
FROM ms_pelanggan
INNER JOIN tr_penjualan
ON ms_pelanggan.kode_pelanggan = tr_penjualan.kode_pelanggan
INNER JOIN tr_penjualan_detail
ON tr_penjualan.kode_transaksi = tr_penjualan_detail.kode_transaksi
GROUP BY 
 ms_pelanggan.kode_pelanggan, 
 ms_pelanggan.nama_pelanggan
ORDER BY total_harga DESC LIMIT 1;