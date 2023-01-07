from mixture import Mixture

m1 = Mixture(100,20)
print(f'm1={m1}')
m2 = Mixture.from_amounts(90,10)
print(f'm2={m2}')
m3 = Mixture.from_salt_ratio(100,0.2)
print(f'm3={m3}')
m4 = Mixture.from_water_amount(100,75)
print(f'm4={m4}')
m5 = Mixture.from_water_ratio(100,0.85)
print(f'm5={m5}')
print(f'm1==m2={m1==m2}')
print(f'm1==m3={m1==m3}') 
m6 = m1 +m2
print(f'm6={m6}')
m7 = m6 * 2 + m4
print(f'm7={m7}')
m8 = m5 / 2
print(f'm8={m8}')

"""Example output
m1=SA:20.00,WA:80.00,SR:0.20,WR:0.80,TOTAL:100.00
m2=SA:10.00,WA:90.00,SR:0.10,WR:0.90,TOTAL:100.00
m3=SA:20.00,WA:80.00,SR:0.20,WR:0.80,TOTAL:100.00
m4=SA:25.00,WA:75.00,SR:0.25,WR:0.75,TOTAL:100.00
m5=SA:15.00,WA:85.00,SR:0.15,WR:0.85,TOTAL:100.00
m1==m2=False
m1==m3=True
m6=SA:30.00,WA:170.00,SR:0.15,WR:0.85,TOTAL:200.00
m7=SA:85.00,WA:415.00,SR:0.17,WR:0.83,TOTAL:500.00
m8=SA:7.50,WA:42.50,SR:0.15,WR:0.85,TOTAL:50.00
"""