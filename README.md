# 1. 필요한 라이브러리 불러오기

- matplotlib → 그림 그리는 도구
- astropy.io.fits → FITS 파일 열기
- astropy.wcs.WCS → 천문학 좌표계(RA, Dec) 정보 사용
- numpy → 수치 계산
- simple_norm → 색깔 범위 자동 조정

# 2. 데이터 읽기

fits.getdata()로 FITS 안의 실제 이미지 데이터 배열만 불러옵니다.

fits.open()으로 파일 전체를 열고, [1] 인덱스로 두 번째 HDU(Header Data Unit)을 선택합니다.

이렇게 얻은 hdu.header는 천문 좌표계 정보(WCS 등)를 담고 있고, hdu.data는 이미지 데이터(픽셀 값)입니다.

# 3. WCS 좌표 설정

WCS(hdu.header)로 WCS 객체를 생성합니다.

나중에 plt.subplot(projection=wcs)로 설정하면, 그래프의 축이 단순한 픽셀 좌표가 아니라 RA(적경), Dec(적위) 단위로 표시됩니다.

# 4. 기본 이미지 출력

plt.imshow(hdu.data, origin='lower', cmap='inferno', vmin=0, vmax=1000)
→ 이미지를 ‘inferno’ 컬러맵으로 표시합니다.

plt.colorbar()로 오른쪽에 색깔 막대를 붙이고, 단위를 'Herschel 250 μm (MJy/sr)'로 달아줍니다.

plt.xlabel('RA'), plt.ylabel('Dec')로 축 레이블을 달고, 제목도 추가합니다.

# 5. 등고선 표시

np.linspace(0,850,3) → 0부터 850까지 균등한 값 3개 생성

plt.contour(hdu.data, …, levels=levelinter) → 데이터 위에 하얀색 점선 등고선을 얹습니다.

# 6. 정규화해서 다시 시각화

simple_norm(data, 'sqrt', percent=99)
→ 데이터 값을 제곱근 스케일로 정규화, 상하위 1% 잘라내고 색깔 대비를 자동 조정

이 정규화를 적용해서 plt.imshow(data, origin='lower', cmap='inferno', norm=norm)으로 다시 표시

# 7. 결과 확인

print(hdu.header)로 FITS 헤더의 주요 정보(WCS 좌표, 픽셀 크기 등)를 출력

마지막에 plt.show()로 완성된 그래프 띄우기