# 1. 라이브러리 가져오기
import matplotlib.pyplot as plt
from astropy.wcs import WCS
from astropy.io import fits
from astropy.utils.data import get_pkg_data_filename
import numpy as np
from astropy.visualization import simple_norm

# 2. 데이터 불러오기
your_file_name = "IC1805"
data = fits.getdata(your_file_name) # Load FITS(Flexible Image Transport System)
filename = get_pkg_data_filename(your_file_name)
hdu = fits.open(filename)[1]
wcs = WCS(hdu.header)   # World Coordinate System
fig = plt.figure(figsize=(18, 12))  # 그래프 사이즈 지정

# 3. 그래프 표시
plt.subplot(projection=wcs)
plt.grid(color="white", linestyle="--") # 그래프 스타일
bar = plt.imshow(hdu.data, origin="lower", cmap="inferno", vmin=0, vmax=1000)
plt.colorbar(bar, label="Herschel 250"r"$\mu$m (MJy/sr)")
plt.xlabel("RA")    # 그래프 x축 (적경)
plt.ylabel("Dec")   # 그래프 y축 (적위)
plt.title(f"{your_file_name} dust continuum map(250"r"$\mu$m)", size=15)
levelinter = np.linspace(0,850,3)
plt.contour(hdu.data, linewidths=2, colors="white", linestyles="--", levels=levelinter)
print(hdu.header)

norm = simple_norm(data, "sqrt", percent=99)
plt.imshow(data,origin="lower", cmap="inferno", norm=norm)
plt.colorbar()
plt.show()