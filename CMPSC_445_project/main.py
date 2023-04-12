import numpy as np
import pandas as pd
import random as ran

np.set_printoptions(precision=3)
np.set_printoptions(threshold=3)
np.set_printoptions(suppress=True)

df = pd.read_csv('diamonds.csv', index_col=[0])
df.pop('fancy_color_intensity')
df.pop('fancy_color_overtone')
df.pop('fancy_color_secondary_color')
df.pop('fancy_color_dominant_color')
df.pop('fluor_color')
df.pop('fluor_intensity')
df.pop('culet_condition')
df.pop('culet_size')
df.pop('eye_clean')

print(df.columns)
print(df['total_sales_price'])

chosen_idx = np.random.choice(219703, replace=False, size=43000)

df2 = df.iloc[chosen_idx]
df2 = df2.sort_index()

cond = df2.index


df.drop(cond, inplace=True)
df2.reset_index(drop=True,inplace=True)
a = 9999
b = 99999
c = 999999
d = 9999999
#e = 9999999
#f = 5399
#g = 10999

classOne = 0
classTwo = 0
classThree = 0
classFour = 0
#classFive = 0
#classSix = 0
#classSeven = 0
#classEight = 0

for i in df['total_sales_price']:
    if i <= a:
        classOne += 1
    elif i <= b:
        classTwo += 1
    elif i <= c:
        classThree += 1
    elif i <= d:
        classFour += 1
    #elif i <= e:
     #   classFive += 1
    #elif i <= f:
     #   classSix += 1
    #elif i <= g:
     #   classSeven += 1
    #else:
        #classSix += 1
'''
print("class 1: "+str(classOne))
print("class 2: "+str(classTwo))
print("class 3: "+str(classThree))
print("class 4: "+str(classFour))
print("class 5: "+str(classFive))
print("class 6: "+str(classSix))
print("class 7: "+str(classSeven))
print("class 8: "+str(classEight))
'''

df2['chosen_class'] = 'z'
'''def letter_class(i):
    if i <= a:
        return 'a'
    elif i <= b:
        return 'b'
    elif i <= c:
        return 'c'
    elif i <= d:
        return 'd'
    elif i <= e:
        return 'e'
    elif i <= f:
        return 'f'
    elif i <= g:
        return 'g'
    else:
        return 'h'
'''

#df2=df2.assign(actual_class=lambda x: (letter_class(x['total_sales_price'])))
#if x<=f else( 'g' if x<=g else 'h') if x<=e else('f' ) if x<=d else('e')
df2['actual_class']=df2['total_sales_price'].apply(lambda x: 'a' if x<=a else ('b' if x<=b else( 'c' if x<=c else('d' ))))

cutOne = df.loc[df['total_sales_price'].between(0, a, inclusive='both'), 'cut'].value_counts()
cutTwo = df.loc[df['total_sales_price'].between(a, b, inclusive='right'), 'cut'].value_counts()
cutThree = df.loc[df['total_sales_price'].between(b, c, inclusive='right'), 'cut'].value_counts()
cutFour = df.loc[df['total_sales_price'].between(c, d, inclusive='right'), 'cut'].value_counts()
#cutFive = df.loc[df['total_sales_price'].between(d, e, inclusive='right'), 'cut'].value_counts()
#cutSix = df.loc[df['total_sales_price'].between(e, df['total_sales_price'].max(), inclusive='both'), 'cut'].value_counts()
#cutSeven = df.loc[df['total_sales_price'].between(f, g, inclusive='right'), 'cut'].value_counts()
#cutEight = df.loc[df['total_sales_price'].between(g, df['total_sales_price'].max(), inclusive='both'), 'cut'].value_counts()
colorOne = df.loc[df['total_sales_price'].between(0, a, inclusive='both'), 'color'].value_counts()
colorTwo = df.loc[df['total_sales_price'].between(a, b, inclusive='right'), 'color'].value_counts()
colorThree = df.loc[df['total_sales_price'].between(b, c, inclusive='right'), 'color'].value_counts()
colorFour = df.loc[df['total_sales_price'].between(c, d, inclusive='right'), 'color'].value_counts()
#colorFive = df.loc[df['total_sales_price'].between(d, e, inclusive='right'), 'color'].value_counts()
#colorSix = df.loc[df['total_sales_price'].between(e, df['total_sales_price'].max(), inclusive='both'), 'color'].value_counts()
#colorSeven = df.loc[df['total_sales_price'].between(f, g, inclusive='right'), 'color'].value_counts()
#colorEight = df.loc[df['total_sales_price'].between(g, df['total_sales_price'].max(), inclusive='both'), 'color'].value_counts()
clarityOne = df.loc[df['total_sales_price'].between(0, a, inclusive='both'), 'clarity'].value_counts()
clarityTwo = df.loc[df['total_sales_price'].between(a, b, inclusive='right'), 'clarity'].value_counts()
clarityThree = df.loc[df['total_sales_price'].between(b, c, inclusive='right'), 'clarity'].value_counts()
clarityFour = df.loc[df['total_sales_price'].between(c, d, inclusive='right'), 'clarity'].value_counts()
#clarityFive = df.loc[df['total_sales_price'].between(d, e, inclusive='right'), 'clarity'].value_counts()
#claritySix = df.loc[df['total_sales_price'].between(e, df['total_sales_price'].max(), inclusive='both'), 'clarity'].value_counts()
#claritySeven = df.loc[df['total_sales_price'].between(f, g, inclusive='right'), 'clarity'].value_counts()
#clarityEight = df.loc[df['total_sales_price'].between(g, df['total_sales_price'].max(), inclusive='both'), 'clarity'].value_counts()

cut_qualityOne = df.loc[df['total_sales_price'].between(0, a, inclusive='both'), 'cut_quality'].value_counts()
cut_qualityTwo = df.loc[df['total_sales_price'].between(a, b, inclusive='right'), 'cut_quality'].value_counts()
cut_qualityThree = df.loc[df['total_sales_price'].between(b, c, inclusive='right'), 'cut_quality'].value_counts()
cut_qualityFour = df.loc[df['total_sales_price'].between(c, d, inclusive='right'), 'cut_quality'].value_counts()
#cut_qualityFive = df.loc[df['total_sales_price'].between(d, e, inclusive='right'), 'cut_quality'].value_counts()
#cut_qualitySix = df.loc[df['total_sales_price'].between(e, df['total_sales_price'].max(), inclusive='both'), 'cut_quality'].value_counts()
#cut_qualitySeven = df.loc[df['total_sales_price'].between(f, g, inclusive='right'), 'cut_quality'].value_counts()
#cut_qualityEight = df.loc[df['total_sales_price'].between(g, df['total_sales_price'].max(), inclusive='both'), 'cut_quality'].value_counts()
labOne = df.loc[df['total_sales_price'].between(0, a, inclusive='both'), 'lab'].value_counts()
labTwo = df.loc[df['total_sales_price'].between(a, b, inclusive='right'), 'lab'].value_counts()
labThree = df.loc[df['total_sales_price'].between(b, c, inclusive='right'), 'lab'].value_counts()
labFour = df.loc[df['total_sales_price'].between(c, d, inclusive='right'), 'lab'].value_counts()
#labFive = df.loc[df['total_sales_price'].between(d, e, inclusive='right'), 'lab'].value_counts()
#labSix = df.loc[df['total_sales_price'].between(e, df['total_sales_price'].max(), inclusive='both'), 'lab'].value_counts()
#labSeven = df.loc[df['total_sales_price'].between(f, g, inclusive='right'), 'lab'].value_counts()
#labEight = df.loc[df['total_sales_price'].between(g, df['total_sales_price'].max(), inclusive='both'), 'lab'].value_counts()
symmetryOne = df.loc[df['total_sales_price'].between(0, a, inclusive='both'), 'symmetry'].value_counts()
symmetryTwo = df.loc[df['total_sales_price'].between(a, b, inclusive='right'), 'symmetry'].value_counts()
symmetryThree = df.loc[df['total_sales_price'].between(b, c, inclusive='right'), 'symmetry'].value_counts()
symmetryFour = df.loc[df['total_sales_price'].between(c, d, inclusive='right'), 'symmetry'].value_counts()
#symmetryFive = df.loc[df['total_sales_price'].between(d, e, inclusive='right'), 'symmetry'].value_counts()
#symmetrySix = df.loc[df['total_sales_price'].between(e, df['total_sales_price'].max(), inclusive='both'), 'symmetry'].value_counts()
#symmetrySeven = df.loc[df['total_sales_price'].between(f, g, inclusive='right'), 'symmetry'].value_counts()
#symmetryEight = df.loc[df['total_sales_price'].between(g, df['total_sales_price'].max(), inclusive='both'), 'symmetry'].value_counts()
polishOne = df.loc[df['total_sales_price'].between(0, a, inclusive='both'), 'polish'].value_counts()
polishTwo = df.loc[df['total_sales_price'].between(a, b, inclusive='right'), 'polish'].value_counts()
polishThree = df.loc[df['total_sales_price'].between(b, c, inclusive='right'), 'polish'].value_counts()
polishFour = df.loc[df['total_sales_price'].between(c, d, inclusive='right'), 'polish'].value_counts()
#polishFive = df.loc[df['total_sales_price'].between(d, e, inclusive='right'), 'polish'].value_counts()
#polishSix = df.loc[df['total_sales_price'].between(e, df['total_sales_price'].max(), inclusive='both'), 'polish'].value_counts()
#polishSeven = df.loc[df['total_sales_price'].between(f, g, inclusive='right'), 'polish'].value_counts()
#polishEight = df.loc[df['total_sales_price'].between(g, df['total_sales_price'].max(), inclusive='both'), 'polish'].value_counts()
girdle_minOne = df.loc[df['total_sales_price'].between(0, a, inclusive='both'), 'girdle_min'].value_counts()
girdle_minTwo = df.loc[df['total_sales_price'].between(a, b, inclusive='right'), 'girdle_min'].value_counts()
girdle_minThree = df.loc[df['total_sales_price'].between(b, c, inclusive='right'), 'girdle_min'].value_counts()
girdle_minFour = df.loc[df['total_sales_price'].between(c, d, inclusive='right'), 'girdle_min'].value_counts()
#girdle_minFive = df.loc[df['total_sales_price'].between(d, e, inclusive='right'), 'girdle_min'].value_counts()
#girdle_minSix = df.loc[df['total_sales_price'].between(e, df['total_sales_price'].max(), inclusive='both'), 'girdle_min'].value_counts()
#girdle_minSeven = df.loc[df['total_sales_price'].between(f, g, inclusive='right'), 'girdle_min'].value_counts()
#girdle_minEight = df.loc[df['total_sales_price'].between(g, df['total_sales_price'].max(), inclusive='both'), 'girdle_min'].value_counts()
girdle_maxOne = df.loc[df['total_sales_price'].between(0, a, inclusive='both'), 'girdle_max'].value_counts()
girdle_maxTwo = df.loc[df['total_sales_price'].between(a, b, inclusive='right'), 'girdle_max'].value_counts()
girdle_maxThree = df.loc[df['total_sales_price'].between(b, c, inclusive='right'), 'girdle_max'].value_counts()
girdle_maxFour = df.loc[df['total_sales_price'].between(c, d, inclusive='right'), 'girdle_max'].value_counts()
#girdle_maxFive = df.loc[df['total_sales_price'].between(d, e, inclusive='right'), 'girdle_max'].value_counts()
#girdle_maxSix = df.loc[df['total_sales_price'].between(e, df['total_sales_price'].max(), inclusive='both'), 'girdle_max'].value_counts()
#girdle_maxSeven = df.loc[df['total_sales_price'].between(f, g, inclusive='right'), 'girdle_max'].value_counts()
#girdle_maxEight = df.loc[df['total_sales_price'].between(g, df['total_sales_price'].max(), inclusive='both'), 'girdle_max'].value_counts()
train_size = 176704

accuracy = 0
num = 0
carat_weight_varOne = df.loc[df['total_sales_price'].between(0, a, inclusive='right'), 'carat_weight'].var()
carat_weight_meanOne = df.loc[df['total_sales_price'].between(0, a, inclusive='right'), 'carat_weight'].mean()
depth_percent_varOne = df.loc[df['total_sales_price'].between(0, a, inclusive='both'), 'depth_percent'].var()
depth_percent_meanOne = df.loc[df['total_sales_price'].between(0, a, inclusive='both'), 'depth_percent'].mean()
table_percent_varOne = df.loc[df['total_sales_price'].between(0, a, inclusive='both'), 'table_percent'].var()
table_percent_meanOne = df.loc[df['total_sales_price'].between(0, a, inclusive='both'), 'table_percent'].mean()
meas_length_varOne = df.loc[df['total_sales_price'].between(0, a, inclusive='both'), 'meas_length'].var()
meas_length_meanOne = df.loc[df['total_sales_price'].between(0, a, inclusive='both'), 'meas_length'].mean()
meas_width_varOne = df.loc[df['total_sales_price'].between(0, a, inclusive='both'), 'meas_width'].var()
meas_width_meanOne = df.loc[df['total_sales_price'].between(0, a, inclusive='both'), 'meas_width'].mean()
meas_depth_varOne = df.loc[df['total_sales_price'].between(0, a, inclusive='both'), 'meas_depth'].var()
meas_depth_meanOne = df.loc[df['total_sales_price'].between(0, a, inclusive='both'), 'meas_depth'].mean()
carat_weight_varTwo = df.loc[df['total_sales_price'].between(a, b, inclusive='right'), 'carat_weight'].var()
carat_weight_meanTwo = df.loc[df['total_sales_price'].between(a, b, inclusive='right'), 'carat_weight'].mean()
depth_percent_varTwo = df.loc[df['total_sales_price'].between(a, b, inclusive='right'), 'depth_percent'].var()
depth_percent_meanTwo = df.loc[df['total_sales_price'].between(a, b, inclusive='right'), 'depth_percent'].mean()
table_percent_varTwo = df.loc[df['total_sales_price'].between(a, b, inclusive='right'), 'table_percent'].var()
table_percent_meanTwo = df.loc[df['total_sales_price'].between(a, b, inclusive='right'), 'table_percent'].mean()
meas_length_varTwo = df.loc[df['total_sales_price'].between(a, b, inclusive='right'), 'meas_length'].var()
meas_length_meanTwo = df.loc[df['total_sales_price'].between(a, b, inclusive='right'), 'meas_length'].mean()
meas_width_varTwo = df.loc[df['total_sales_price'].between(a, b, inclusive='right'), 'meas_width'].var()
meas_width_meanTwo = df.loc[df['total_sales_price'].between(a, b, inclusive='right'), 'meas_width'].mean()
meas_depth_varTwo = df.loc[df['total_sales_price'].between(a, b, inclusive='right'), 'meas_depth'].var()
meas_depth_meanTwo = df.loc[df['total_sales_price'].between(a, b, inclusive='right'), 'meas_depth'].mean()
carat_weight_varThree = df.loc[df['total_sales_price'].between(b, c, inclusive='right'), 'carat_weight'].var()
carat_weight_meanThree = df.loc[df['total_sales_price'].between(b, c, inclusive='right'), 'carat_weight'].mean()
depth_percent_varThree = df.loc[df['total_sales_price'].between(b, c, inclusive='right'), 'depth_percent'].var()
depth_percent_meanThree = df.loc[df['total_sales_price'].between(b, c, inclusive='right'), 'depth_percent'].mean()
table_percent_varThree = df.loc[df['total_sales_price'].between(b, c, inclusive='right'), 'table_percent'].var()
table_percent_meanThree = df.loc[df['total_sales_price'].between(b, c, inclusive='right'), 'table_percent'].mean()
meas_length_varThree = df.loc[df['total_sales_price'].between(b, c, inclusive='right'), 'meas_length'].var()
meas_length_meanThree = df.loc[df['total_sales_price'].between(b, c, inclusive='right'), 'meas_length'].mean()
meas_width_varThree = df.loc[df['total_sales_price'].between(b, c, inclusive='right'), 'meas_width'].var()
meas_width_meanThree = df.loc[df['total_sales_price'].between(b, c, inclusive='right'), 'meas_width'].mean()
meas_depth_varThree = df.loc[df['total_sales_price'].between(b, c, inclusive='right'), 'meas_depth'].var()
meas_depth_meanThree = df.loc[df['total_sales_price'].between(b, c, inclusive='right'), 'meas_depth'].mean()

carat_weight_varFour = df.loc[df['total_sales_price'].between(c, d, inclusive='right'), 'carat_weight'].var()
carat_weight_meanFour = df.loc[df['total_sales_price'].between(c, d, inclusive='right'), 'carat_weight'].mean()
depth_percent_varFour = df.loc[df['total_sales_price'].between(c, d, inclusive='right'), 'depth_percent'].var()
depth_percent_meanFour = df.loc[df['total_sales_price'].between(c, d, inclusive='right'), 'depth_percent'].mean()
table_percent_varFour = df.loc[df['total_sales_price'].between(c, d, inclusive='right'), 'table_percent'].var()
table_percent_meanFour = df.loc[df['total_sales_price'].between(c, d, inclusive='right'), 'table_percent'].mean()
meas_length_varFour = df.loc[df['total_sales_price'].between(c, d, inclusive='right'), 'meas_length'].var()
meas_length_meanFour = df.loc[df['total_sales_price'].between(c, d, inclusive='right'), 'meas_length'].mean()
meas_width_varFour = df.loc[df['total_sales_price'].between(c, d, inclusive='right'), 'meas_width'].var()
meas_width_meanFour = df.loc[df['total_sales_price'].between(c, d, inclusive='right'), 'meas_width'].mean()
meas_depth_varFour = df.loc[df['total_sales_price'].between(c, d, inclusive='right'), 'meas_depth'].var()
meas_depth_meanFour = df.loc[df['total_sales_price'].between(c, d, inclusive='right'), 'meas_depth'].mean()
'''
carat_weight_varFive = df.loc[df['total_sales_price'].between(d, e, inclusive='right'), 'carat_weight'].var()
carat_weight_meanFive = df.loc[df['total_sales_price'].between(d, e, inclusive='right'), 'carat_weight'].mean()
depth_percent_varFive = df.loc[df['total_sales_price'].between(d, e, inclusive='right'), 'depth_percent'].var()
depth_percent_meanFive = df.loc[df['total_sales_price'].between(d, e, inclusive='right'), 'depth_percent'].mean()
table_percent_varFive = df.loc[df['total_sales_price'].between(d, e, inclusive='right'), 'table_percent'].var()
table_percent_meanFive = df.loc[df['total_sales_price'].between(d, e, inclusive='right'), 'table_percent'].mean()
meas_length_varFive = df.loc[df['total_sales_price'].between(d, e, inclusive='right'), 'meas_length'].var()
meas_length_meanFive = df.loc[df['total_sales_price'].between(d, e, inclusive='right'), 'meas_length'].mean()
meas_width_varFive = df.loc[df['total_sales_price'].between(d, e, inclusive='right'), 'meas_width'].var()
meas_width_meanFive = df.loc[df['total_sales_price'].between(d, e, inclusive='right'), 'meas_width'].mean()
meas_depth_varFive = df.loc[df['total_sales_price'].between(d, e, inclusive='right'), 'meas_depth'].var()
meas_depth_meanFive = df.loc[df['total_sales_price'].between(d, e, inclusive='right'), 'meas_depth'].mean()

carat_weight_varSix = df.loc[df['total_sales_price'].between(e, df['total_sales_price'].max(), inclusive='both'), 'carat_weight'].var()
carat_weight_meanSix = df.loc[df['total_sales_price'].between(e, df['total_sales_price'].max(), inclusive='both'), 'carat_weight'].mean()
depth_percent_varSix = df.loc[df['total_sales_price'].between(e, df['total_sales_price'].max(), inclusive='both'), 'depth_percent'].var()
depth_percent_meanSix = df.loc[df['total_sales_price'].between(e, df['total_sales_price'].max(), inclusive='both'), 'depth_percent'].mean()
table_percent_varSix = df.loc[df['total_sales_price'].between(e, df['total_sales_price'].max(), inclusive='both'), 'table_percent'].var()
table_percent_meanSix = df.loc[df['total_sales_price'].between(e, df['total_sales_price'].max(), inclusive='both'), 'table_percent'].mean()
meas_length_varSix = df.loc[df['total_sales_price'].between(e, df['total_sales_price'].max(), inclusive='both'), 'meas_length'].var()
meas_length_meanSix = df.loc[df['total_sales_price'].between(e, df['total_sales_price'].max(), inclusive='both'), 'meas_length'].mean()
meas_width_varSix = df.loc[df['total_sales_price'].between(e, df['total_sales_price'].max(), inclusive='both'), 'meas_width'].var()
meas_width_meanSix = df.loc[df['total_sales_price'].between(e, df['total_sales_price'].max(), inclusive='both'), 'meas_width'].mean()
meas_depth_varSix = df.loc[df['total_sales_price'].between(e, df['total_sales_price'].max(), inclusive='both'), 'meas_depth'].var()
meas_depth_meanSix = df.loc[df['total_sales_price'].between(e, df['total_sales_price'].max(), inclusive='both'), 'meas_depth'].mean()

carat_weight_varSeven = df.loc[df['total_sales_price'].between(f, g, inclusive='right'), 'carat_weight'].var()
carat_weight_meanSeven = df.loc[df['total_sales_price'].between(f, g, inclusive='right'), 'carat_weight'].mean()
depth_percent_varSeven = df.loc[df['total_sales_price'].between(f, g, inclusive='right'), 'depth_percent'].var()
depth_percent_meanSeven = df.loc[df['total_sales_price'].between(f, g, inclusive='right'), 'depth_percent'].mean()
table_percent_varSeven = df.loc[df['total_sales_price'].between(f, g, inclusive='right'), 'table_percent'].var()
table_percent_meanSeven = df.loc[df['total_sales_price'].between(f, g, inclusive='right'), 'table_percent'].mean()
meas_length_varSeven = df.loc[df['total_sales_price'].between(f, g, inclusive='right'), 'meas_length'].var()
meas_length_meanSeven = df.loc[df['total_sales_price'].between(f, g, inclusive='right'), 'meas_length'].mean()
meas_width_varSeven = df.loc[df['total_sales_price'].between(f, g, inclusive='right'), 'meas_width'].var()
meas_width_meanSeven = df.loc[df['total_sales_price'].between(f, g, inclusive='right'), 'meas_width'].mean()
meas_depth_varSeven = df.loc[df['total_sales_price'].between(f, g, inclusive='right'), 'meas_depth'].var()
meas_depth_meanSeven = df.loc[df['total_sales_price'].between(f, g, inclusive='right'), 'meas_depth'].mean()

carat_weight_varEight = df.loc[
    df['total_sales_price'].between(g, df['total_sales_price'].max(), inclusive='both'), 'carat_weight'].var()
carat_weight_meanEight = df.loc[
    df['total_sales_price'].between(g, df['total_sales_price'].max(), inclusive='both'), 'carat_weight'].mean()
depth_percent_varEight = df.loc[
    df['total_sales_price'].between(g, df['total_sales_price'].max(), inclusive='both'), 'depth_percent'].var()
depth_percent_meanEight = df.loc[
    df['total_sales_price'].between(g, df['total_sales_price'].max(), inclusive='both'), 'depth_percent'].mean()
table_percent_varEight = df.loc[
    df['total_sales_price'].between(g, df['total_sales_price'].max(), inclusive='both'), 'table_percent'].var()
table_percent_meanEight = df.loc[
    df['total_sales_price'].between(g, df['total_sales_price'].max(), inclusive='both'), 'table_percent'].mean()
meas_length_varEight = df.loc[
    df['total_sales_price'].between(g, df['total_sales_price'].max(), inclusive='both'), 'meas_length'].var()
meas_length_meanEight = df.loc[
    df['total_sales_price'].between(g, df['total_sales_price'].max(), inclusive='both'), 'meas_length'].mean()
meas_width_varEight = df.loc[
    df['total_sales_price'].between(g, df['total_sales_price'].max(), inclusive='both'), 'meas_width'].var()
meas_width_meanEight = df.loc[
    df['total_sales_price'].between(g, df['total_sales_price'].max(), inclusive='both'), 'meas_width'].mean()
meas_depth_varEight = df.loc[
    df['total_sales_price'].between(g, df['total_sales_price'].max(), inclusive='both'), 'meas_depth'].var()
meas_depth_meanEight = df.loc[
    df['total_sales_price'].between(g, df['total_sales_price'].max(), inclusive='both'), 'meas_depth'].mean()
'''

def count(dataset, value):
    try:
        return dataset[value]
    except:
        return 0

test_size=0
for test in df2.values:
    print('Index: ' + str(num))

    carat_weightOne = (1 / np.sqrt(2 * np.pi * carat_weight_varOne)) * np.exp(
        -((test[3] - carat_weight_meanOne) ** 2) / (2 * carat_weight_varOne))
    depth_percentOne = (1 / np.sqrt(2 * np.pi * depth_percent_varOne)) * np.exp(
        -((test[8] - depth_percent_meanOne) ** 2) / (2 * depth_percent_varOne))
    table_percentOne = (1 / np.sqrt(2 * np.pi * table_percent_varOne)) * np.exp(
        -((test[9] - table_percent_meanOne) ** 2) / (2 * table_percent_varOne))
    meas_lengthOne = (1 / np.sqrt(2 * np.pi * meas_length_varOne)) * np.exp(
        -((test[10] - meas_length_meanOne) ** 2) / (2 * meas_length_varOne))
    meas_widthOne = (1 / np.sqrt(2 * np.pi * meas_width_varOne)) * np.exp(
        -((test[11] - meas_width_meanOne) ** 2) / (2 * meas_width_varOne))
    meas_depthOne = (1 / np.sqrt(2 * np.pi * meas_depth_varOne)) * np.exp(
        -((test[12] - meas_depth_meanOne) ** 2) / (2 * meas_depth_varOne))
    carat_weightTwo = (1 / np.sqrt(2 * np.pi * carat_weight_varTwo)) * np.exp(
        -((test[3] - carat_weight_meanTwo) ** 2) / (2 * carat_weight_varTwo))
    depth_percentTwo = (1 / np.sqrt(2 * np.pi * depth_percent_varTwo)) * np.exp(
        -((test[8] - depth_percent_meanTwo) ** 2) / (2 * depth_percent_varTwo))
    table_percentTwo = (1 / np.sqrt(2 * np.pi * table_percent_varTwo)) * np.exp(
        -((test[9] - table_percent_meanTwo) ** 2) / (2 * table_percent_varTwo))
    meas_lengthTwo = (1 / np.sqrt(2 * np.pi * meas_length_varTwo)) * np.exp(
        -((test[10] - meas_length_meanTwo) ** 2) / (2 * meas_length_varTwo))
    meas_widthTwo = (1 / np.sqrt(2 * np.pi * meas_width_varTwo)) * np.exp(
        -((test[11] - meas_width_meanTwo) ** 2) / (2 * meas_width_varTwo))
    meas_depthTwo = (1 / np.sqrt(2 * np.pi * meas_depth_varTwo)) * np.exp(
        -((test[12] - meas_depth_meanTwo) ** 2) / (2 * meas_depth_varTwo))
    carat_weightThree = (1 / np.sqrt(2 * np.pi * carat_weight_varThree)) * np.exp(
        -((test[3] - carat_weight_meanThree) ** 2) / (2 * carat_weight_varThree))
    depth_percentThree = (1 / np.sqrt(2 * np.pi * depth_percent_varThree)) * np.exp(
        -((test[8] - depth_percent_meanThree) ** 2) / (2 * depth_percent_varThree))
    table_percentThree = (1 / np.sqrt(2 * np.pi * table_percent_varThree)) * np.exp(
        -((test[9] - table_percent_meanThree) ** 2) / (2 * table_percent_varThree))
    meas_lengthThree = (1 / np.sqrt(2 * np.pi * meas_length_varThree)) * np.exp(
        -((test[10] - meas_length_meanThree) ** 2) / (2 * meas_length_varThree))
    meas_widthThree = (1 / np.sqrt(2 * np.pi * meas_width_varThree)) * np.exp(
        -((test[11] - meas_width_meanThree) ** 2) / (2 * meas_width_varThree))
    meas_depthThree = (1 / np.sqrt(2 * np.pi * meas_depth_varThree)) * np.exp(
        -((test[12] - meas_depth_meanThree) ** 2) / (2 * meas_depth_varThree))

    carat_weightFour = (1 / np.sqrt(2 * np.pi * carat_weight_varFour)) * np.exp(
        -((test[3] - carat_weight_meanFour) ** 2) / (2 * carat_weight_varFour))
    depth_percentFour = (1 / np.sqrt(2 * np.pi * depth_percent_varFour)) * np.exp(
        -((test[8] - depth_percent_meanFour) ** 2) / (2 * depth_percent_varFour))
    table_percentFour = (1 / np.sqrt(2 * np.pi * table_percent_varFour)) * np.exp(
        -((test[9] - table_percent_meanFour) ** 2) / (2 * table_percent_varFour))
    meas_lengthFour = (1 / np.sqrt(2 * np.pi * meas_length_varFour)) * np.exp(
        -((test[10] - meas_length_meanFour) ** 2) / (2 * meas_length_varFour))
    meas_widthFour = (1 / np.sqrt(2 * np.pi * meas_width_varFour)) * np.exp(
        -((test[11] - meas_width_meanFour) ** 2) / (2 * meas_width_varFour))
    meas_depthFour = (1 / np.sqrt(2 * np.pi * meas_depth_varFour)) * np.exp(
        -((test[12] - meas_depth_meanFour) ** 2) / (2 * meas_depth_varFour))
    '''
    carat_weightFive = (1 / np.sqrt(2 * np.pi * carat_weight_varFive)) * np.exp(
        -((test[3] - carat_weight_meanFive) ** 2) / (2 * carat_weight_varFive))
    depth_percentFive = (1 / np.sqrt(2 * np.pi * depth_percent_varFive)) * np.exp(
        -((test[8] - depth_percent_meanFive) ** 2) / (2 * depth_percent_varFive))
    table_percentFive = (1 / np.sqrt(2 * np.pi * table_percent_varFive)) * np.exp(
        -((test[9] - table_percent_meanFive) ** 2) / (2 * table_percent_varFive))
    meas_lengthFive = (1 / np.sqrt(2 * np.pi * meas_length_varFive)) * np.exp(
        -((test[10] - meas_length_meanFive) ** 2) / (2 * meas_length_varFive))
    meas_widthFive = (1 / np.sqrt(2 * np.pi * meas_width_varFive)) * np.exp(
        -((test[11] - meas_width_meanFive) ** 2) / (2 * meas_width_varFive))
    meas_depthFive = (1 / np.sqrt(2 * np.pi * meas_depth_varFive)) * np.exp(
        -((test[12] - meas_depth_meanFive) ** 2) / (2 * meas_depth_varFive))

    carat_weightSix = (1 / np.sqrt(2 * np.pi * carat_weight_varSix)) * np.exp(
        -((test[3] - carat_weight_meanSix) ** 2) / (2 * carat_weight_varSix))
    depth_percentSix = (1 / np.sqrt(2 * np.pi * depth_percent_varSix)) * np.exp(
        -((test[8] - depth_percent_meanSix) ** 2) / (2 * depth_percent_varSix))
    table_percentSix = (1 / np.sqrt(2 * np.pi * table_percent_varSix)) * np.exp(
        -((test[9] - table_percent_meanSix) ** 2) / (2 * table_percent_varSix))
    meas_lengthSix = (1 / np.sqrt(2 * np.pi * meas_length_varSix)) * np.exp(
        -((test[10] - meas_length_meanSix) ** 2) / (2 * meas_length_varSix))
    meas_widthSix = (1 / np.sqrt(2 * np.pi * meas_width_varSix)) * np.exp(
        -((test[11] - meas_width_meanSix) ** 2) / (2 * meas_width_varSix))
    meas_depthSix = (1 / np.sqrt(2 * np.pi * meas_depth_varSix)) * np.exp(
        -((test[12] - meas_depth_meanSix) ** 2) / (2 * meas_depth_varSix))
    
    carat_weightSeven = (1 / np.sqrt(2 * np.pi * carat_weight_varSeven)) * np.exp(
        -((test[3] - carat_weight_meanSeven) ** 2) / (2 * carat_weight_varSeven))
    depth_percentSeven = (1 / np.sqrt(2 * np.pi * depth_percent_varSeven)) * np.exp(
        -((test[8] - depth_percent_meanSeven) ** 2) / (2 * depth_percent_varSeven))
    table_percentSeven = (1 / np.sqrt(2 * np.pi * table_percent_varSeven)) * np.exp(
        -((test[9] - table_percent_meanSeven) ** 2) / (2 * table_percent_varSeven))
    meas_lengthSeven = (1 / np.sqrt(2 * np.pi * meas_length_varSeven)) * np.exp(
        -((test[10] - meas_length_meanSeven) ** 2) / (2 * meas_length_varSeven))
    meas_widthSeven = (1 / np.sqrt(2 * np.pi * meas_width_varSeven)) * np.exp(
        -((test[11] - meas_width_meanSeven) ** 2) / (2 * meas_width_varSeven))
    meas_depthSeven = (1 / np.sqrt(2 * np.pi * meas_depth_varSeven)) * np.exp(
        -((test[12] - meas_depth_meanSeven) ** 2) / (2 * meas_depth_varSeven))
    carat_weightEight = (1 / np.sqrt(2 * np.pi * carat_weight_varEight)) * np.exp(
        -((test[3] - carat_weight_meanEight) ** 2) / (2 * carat_weight_varEight))
    depth_percentEight = (1 / np.sqrt(2 * np.pi * depth_percent_varEight)) * np.exp(
        -((test[8] - depth_percent_meanEight) ** 2) / (2 * depth_percent_varEight))
    table_percentEight = (1 / np.sqrt(2 * np.pi * table_percent_varEight)) * np.exp(
        -((test[9] - table_percent_meanEight) ** 2) / (2 * table_percent_varEight))
    meas_lengthEight = (1 / np.sqrt(2 * np.pi * meas_length_varEight)) * np.exp(
        -((test[10] - meas_length_meanEight) ** 2) / (2 * meas_length_varEight))
    meas_widthEight = (1 / np.sqrt(2 * np.pi * meas_width_varEight)) * np.exp(
        -((test[11] - meas_width_meanEight) ** 2) / (2 * meas_width_varEight))
    meas_depthEight = (1 / np.sqrt(2 * np.pi * meas_depth_varEight)) * np.exp(
        -((test[12] - meas_depth_meanEight) ** 2) / (2 * meas_depth_varEight))
'''

    prob1 = np.log((classOne + 1) / (train_size + 8)) + np.log(
        (count(cutOne,test[0]) + 1) / (classOne + df['cut'].unique().size)) + np.log(
        (count(colorOne,test[1]) + 1) / (classOne + df['color'].unique().size)) + np.log(
        (count(clarityOne,test[2]) + 1) / (classOne + df['clarity'].unique().size)) + np.log(carat_weightOne) + np.log(
        (count(cut_qualityOne,test[4]) + 1) / (classOne + df['cut_quality'].unique().size)) + np.log(
        (count(labOne,test[5]) + 1) / (classOne + df['lab'].unique().size)) + np.log(
        (count(symmetryOne,test[6]) + 1) / (classOne + df['symmetry'].unique().size)) + np.log(
        (count(polishOne,test[7]) + 1) / (classOne + df['polish'].unique().size)) + np.log(depth_percentOne) + np.log(
        table_percentOne) + np.log(meas_lengthOne) + np.log(meas_widthOne) + np.log(meas_depthOne) + np.log(
        (count(girdle_minOne,test[13]) + 1) / (classOne + df['girdle_min'].unique().size)) + np.log(
        (count(girdle_maxOne,test[14]) + 1) / (classOne + df['girdle_max'].unique().size))
    prob2 = np.log((classTwo + 1) / (train_size + 8)) + np.log(
        (count(cutTwo, test[0]) + 1) / (classTwo + df['cut'].unique().size)) + np.log(
        (count(colorTwo, test[1]) + 1) / (classTwo + df['color'].unique().size)) + np.log(
        (count(clarityTwo, test[2]) + 1) / (classTwo + df['clarity'].unique().size)) + np.log(carat_weightTwo) + np.log(
        (count(cut_qualityTwo, test[4]) + 1) / (classTwo + df['cut_quality'].unique().size)) + np.log(
        (count(labTwo, test[5]) + 1) / (classTwo + df['lab'].unique().size)) + np.log(
        (count(symmetryTwo, test[6]) + 1) / (classTwo + df['symmetry'].unique().size)) + np.log(
        (count(polishTwo, test[7]) + 1) / (classTwo + df['polish'].unique().size)) + np.log(depth_percentTwo) + np.log(
        table_percentTwo) + np.log(meas_lengthTwo) + np.log(meas_widthTwo) + np.log(meas_depthTwo) + np.log(
        (count(girdle_minTwo, test[13]) + 1) / (classTwo + df['girdle_min'].unique().size)) + np.log(
        (count(girdle_maxTwo, test[14]) + 1) / (classTwo + df['girdle_max'].unique().size))
    prob3 = np.log((classThree + 1) / (train_size + 8)) + np.log(
        (count(cutThree, test[0]) + 1) / (classThree + df['cut'].unique().size)) + np.log(
        (count(colorThree, test[1]) + 1) / (classThree + df['color'].unique().size)) + np.log(
        (count(clarityThree, test[2]) + 1) / (classThree + df['clarity'].unique().size)) + np.log(
        carat_weightThree) + np.log(
        (count(cut_qualityThree, test[4]) + 1) / (classThree + df['cut_quality'].unique().size)) + np.log(
        (count(labThree, test[5]) + 1) / (classThree + df['lab'].unique().size)) + np.log(
        (count(symmetryThree, test[6]) + 1) / (classThree + df['symmetry'].unique().size)) + np.log(
        (count(polishThree, test[7]) + 1) / (classThree + df['polish'].unique().size)) + np.log(
        depth_percentThree) + np.log(
        table_percentThree) + np.log(meas_lengthThree) + np.log(meas_widthThree) + np.log(meas_depthThree) + np.log(
        (count(girdle_minThree, test[13]) + 1) / (classThree + df['girdle_min'].unique().size)) + np.log(
        (count(girdle_maxThree, test[14]) + 1) / (classThree + df['girdle_max'].unique().size))

    prob4 = np.log((classFour + 1) / (train_size + 8)) + np.log(
        (count(cutFour, test[0]) + 1) / (classFour + df['cut'].unique().size)) + np.log(
        (count(colorFour, test[1]) + 1) / (classFour + df['color'].unique().size)) + np.log(
        (count(clarityFour, test[2]) + 1) / (classFour + df['clarity'].unique().size)) + np.log(
        carat_weightFour) + np.log(
        (count(cut_qualityFour, test[4]) + 1) / (classFour + df['cut_quality'].unique().size)) + np.log(
        (count(labFour, test[5]) + 1) / (classFour + df['lab'].unique().size)) + np.log(
        (count(symmetryFour, test[6]) + 1) / (classFour + df['symmetry'].unique().size)) + np.log(
        (count(polishFour, test[7]) + 1) / (classFour + df['polish'].unique().size)) + np.log(
        depth_percentFour) + np.log(
        table_percentFour) + np.log(meas_lengthFour) + np.log(meas_widthFour) + np.log(meas_depthFour) + np.log(
        (count(girdle_minFour, test[13]) + 1) / (classFour + df['girdle_min'].unique().size)) + np.log(
        (count(girdle_maxFour, test[14]) + 1) / (classFour + df['girdle_max'].unique().size))
    '''
    prob5 = np.log((classFive + 1) / (train_size + 8)) + np.log(
        (count(cutFive, test[0]) + 1) / (classFive + df['cut'].unique().size)) + np.log(
        (count(colorFive, test[1]) + 1) / (classFive + df['color'].unique().size)) + np.log(
        (count(clarityFive, test[2]) + 1) / (classFive + df['clarity'].unique().size)) + np.log(
        carat_weightFive) + np.log(
        (count(cut_qualityFive, test[4]) + 1) / (classFive + df['cut_quality'].unique().size)) + np.log(
        (count(labFive, test[5]) + 1) / (classFive + df['lab'].unique().size)) + np.log(
        (count(symmetryFive, test[6]) + 1) / (classFive + df['symmetry'].unique().size)) + np.log(
        (count(polishFive, test[7]) + 1) / (classFive + df['polish'].unique().size)) + np.log(
        depth_percentFive) + np.log(
        table_percentFive) + np.log(meas_lengthFive) + np.log(meas_widthFive) + np.log(meas_depthFive) + np.log(
        (count(girdle_minFive, test[13]) + 1) / (classFive + df['girdle_min'].unique().size)) + np.log(
        (count(girdle_maxFive, test[14]) + 1) / (classFive + df['girdle_max'].unique().size))
    
    prob6 = np.log((classSix + 1) / (train_size + 8)) + np.log(
        (count(cutSix, test[0]) + 1) / (classSix + df['cut'].unique().size)) + np.log(
        (count(colorSix, test[1]) + 1) / (classSix + df['color'].unique().size)) + np.log(
        (count(claritySix, test[2]) + 1) / (classSix + df['clarity'].unique().size)) + np.log(carat_weightSix) + np.log(
        (count(cut_qualitySix, test[4]) + 1) / (classSix + df['cut_quality'].unique().size)) + np.log(
        (count(labSix, test[5]) + 1) / (classSix + df['lab'].unique().size)) + np.log(
        (count(symmetrySix, test[6]) + 1) / (classSix + df['symmetry'].unique().size)) + np.log(
        (count(polishSix, test[7]) + 1) / (classSix + df['polish'].unique().size)) + np.log(depth_percentSix) + np.log(
        table_percentSix) + np.log(meas_lengthSix) + np.log(meas_widthSix) + np.log(meas_depthSix) + np.log(
        (count(girdle_minSix, test[13]) + 1) / (classSix + df['girdle_min'].unique().size)) + np.log(
        (count(girdle_maxSix, test[14]) + 1) / (classSix + df['girdle_max'].unique().size))
    
    prob7 = np.log((classSeven + 1) / (train_size + 8)) + np.log(
        (count(cutSeven, test[0]) + 1) / (classSeven + df['cut'].unique().size)) + np.log(
        (count(colorSeven, test[1]) + 1) / (classSeven + df['color'].unique().size)) + np.log(
        (count(claritySeven, test[2]) + 1) / (classSeven + df['clarity'].unique().size)) + np.log(
        carat_weightSeven) + np.log(
        (count(cut_qualitySeven, test[4]) + 1) / (classSeven + df['cut_quality'].unique().size)) + np.log(
        (count(labSeven, test[5]) + 1) / (classSeven + df['lab'].unique().size)) + np.log(
        (count(symmetrySeven, test[6]) + 1) / (classSeven + df['symmetry'].unique().size)) + np.log(
        (count(polishSeven, test[7]) + 1) / (classSeven + df['polish'].unique().size)) + np.log(
        depth_percentSeven) + np.log(
        table_percentSeven) + np.log(meas_lengthSeven) + np.log(meas_widthSeven) + np.log(meas_depthSeven) + np.log(
        (count(girdle_minSeven, test[13]) + 1) / (classSeven + df['girdle_min'].unique().size)) + np.log(
        (count(girdle_maxSeven, test[14]) + 1) / (classSeven + df['girdle_max'].unique().size))
    prob8 = np.log((classEight + 1) / (train_size + 8)) + np.log(
        (count(cutEight, test[0]) + 1) / (classEight + df['cut'].unique().size)) + np.log(
        (count(colorEight, test[1]) + 1) / (classEight + df['color'].unique().size)) + np.log(
        (count(clarityEight, test[2]) + 1) / (classEight + df['clarity'].unique().size)) + np.log(
        carat_weightEight) + np.log(
        (count(cut_qualityEight, test[4]) + 1) / (classEight + df['cut_quality'].unique().size)) + np.log(
        (count(labEight, test[5]) + 1) / (classEight + df['lab'].unique().size)) + np.log(
        (count(symmetryEight, test[6]) + 1) / (classEight + df['symmetry'].unique().size)) + np.log(
        (count(polishEight, test[7]) + 1) / (classEight + df['polish'].unique().size)) + np.log(
        depth_percentEight) + np.log(
        table_percentEight) + np.log(meas_lengthEight) + np.log(meas_widthEight) + np.log(meas_depthEight) + np.log(
        (count(girdle_minEight, test[13]) + 1) / (classEight + df['girdle_min'].unique().size)) + np.log(
        (count(girdle_maxEight, test[14]) + 1) / (classEight + df['girdle_max'].unique().size))
        '''
    probs = [prob1, prob2, prob3,prob4]
    chosen_prob = np.max(probs)

    if chosen_prob == prob1:
        df2.at[num,'chosen_class']='a'
        if test[15] <= a:
            accuracy += 1
    elif chosen_prob == prob2:
        df2.at[num,'chosen_class']='b'
        if b >= test[15] > a:
            accuracy += 1
    elif chosen_prob == prob3:
        df2.at[num,'chosen_class']='c'
        if c >= test[15] > b:
            accuracy += 1

    elif chosen_prob == prob4:
        df2.at[num,'chosen_class']='d'
        if d >= test[15] > c:
            accuracy += 1
    '''
    elif chosen_prob == prob5:
        df2.at[num,'chosen_class']='e'
        if e >= test[15] > d:
            accuracy += 1
    
    elif chosen_prob == prob6:
        test[16] = 'f'
        if test[15] > e:
            accuracy += 1
    
    elif chosen_prob == prob7:
        test[16] = 'g'
        if g >= test[15] > f:
            accuracy += 1
    elif chosen_prob == prob8:
        test[16] = 'h'
        if test[15] > g:
            accuracy += 1
    '''
    test_size+=1.0
    print("Accuracy " + str(accuracy / test_size))
    print(df2['chosen_class'].loc[num])
    print(test[17])
    num += 1
df.to_csv('trainset6.csv')
df2.to_csv('testset6.csv')
