#!/usr/bin/env python
# -*- coding: utf-8 -*-

fibo = [1,2]    # הסדרה ההתחלתית
total = 0      # משתנה לחישוב הסכום המצטבר


# קחו את האיבר האחרון בסדרה
while fibo[-1] <= 4000000: # ובדקו שהוא קטן מהערך שהוגדר
  if fibo[-1] % 2 == 0:      # במידה והאיבר החדש זוגי:
    total = total + fibo[-1]    # הוסיפו את הערך שלו לסכום המצטבר
  
  fibo.append(fibo[-2] + fibo[-1]) #צרו את האיבר החדש, באמצעות חיבור שני האיברים הקודמים


print(total)
