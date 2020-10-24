medida = float(input('Digite uma distância em metros: '))
km = medida/1000
hm = medida/100
dam = medida/10
m = medida*1
dm = medida*10
cm = medida*100
mm = medida*1000
print('A medida de {} corresponde a {}km, {}hm, {}dam, {}m, {}dm, {}cm, {}mm.'.format(medida, km, hm, dam, m, dm, cm, mm))