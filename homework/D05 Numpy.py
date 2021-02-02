import numpy as np
english_score = np.array([55,89,76,65,48,70])

math_score = np.array([60,85,60,68,np.nan,60])

chinese_score = np.array([65,90,82,72,66,77])

print(np.nanmean(english_score),np.nanmax(english_score),np.nanmin(english_score),np.nanstd(english_score))
print(np.nanmean(math_score),np.nanmax(math_score),np.nanmin(math_score),np.nanstd(math_score))
print(np.nanmean(chinese_score),np.nanmax(chinese_score),np.nanmin(chinese_score),np.nanstd(chinese_score))

math_score[4]=55
print(np.nanmean(math_score),np.nanmax(math_score),np.nanmin(math_score),np.nanstd(math_score))

print(np.corrcoef(chinese_score,math_score))
print(np.corrcoef(chinese_score,english_score))