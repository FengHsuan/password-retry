# 密碼重試程式
# password = 'a123456'
# 讓使用者重複輸入密碼
# 最多輸入三次
# 如果正確 就印出’登入成功！‘
# 如果不正確 就印出‘密碼錯誤！’

password = 'a123456'
x = 3 #3次機會
while x > 0:
	x = x-1
	pwd = input('請輸入密碼： ')
	if pwd == password:
		print('登入成功')
		break #逃出迴圈
	else:
		print('密碼錯誤！')
		if x > 0 :
			print('還有', x, '次機會')
		else:
			print('沒機會嘗試了！帳號已鎖定')