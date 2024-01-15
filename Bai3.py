import arcpy
import os
# trả về kết quả dạng số thực (float) thay vì số nguyên (int) khi cả hai toán hạng đều là số nguyên
from __future__ import division

# Dẫn tới folder chứa dữ liệu ảnh vệ tinh
arcpy.env.workspace = "path/to/Data"

# lấy danh sách ảnh vệ tinh
raster_list = arcpy.ListRasters()

# tạo folder Indices để lưu kết quả
if not os.path.exists("path/to/Indices"):
    os.makedirs("path/to/Indices")

# Tạo vòng lặp for chạy trong danh sách ảnh vệ tinh
for raster in raster_list:

# nếu tên của ảnh có tiền tố là H thì tiếp tục chạy
    if os.path.basename(raster)[0] == "H":
        continue

# Tính chỉ số NDVI
    b5_raster = arcpy.sa.Float(arcpy.sa.Raster(raster + "_B5"))
    b4_raster = arcpy.sa.Float(arcpy.sa.Raster(raster + "_B4"))
    ndvi_raster = (b5_raster - b4_raster) / ((b5_raster + b4_raster))
# Lưu raster NDVI vừa tính được vào folder Indices
    ndvi_raster.save("path/to/Indices/" + os.path.basename(raster) + "_NDVI.tif")

#tính chỉ số NDBI 
    b6_raster = arcpy.sa.Float(arcpy.sa.Raster(raster + "_B6"))
    ndbi_raster = (b6_raster - b5_raster) / ((b6_raster + b5_raster))
# lưu file NDBI vào folder Indices	
    ndbi_raster.save("path/to/Indices/" + os.path.basename(raster) + "_NDBI.tif")

# Lọc ra các khu vực có NDVI (0.6 - 1) và lưu thành shp
    ndvi_mask = arcpy.sa.ExtractByAttributes(ndvi_raster, "VALUE >= 0.6 AND VALUE <= 1")
    ndvi_mask.save("path/to/Indices/" + os.path.basename(raster) + "_NDVI_mask.tif")
    arcpy.RasterToPolygon_conversion(ndvi_mask, "path/to/Indices/" + os.path.basename(raster) + "_NDVI_mask.shp")