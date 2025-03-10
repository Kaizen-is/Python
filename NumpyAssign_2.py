import numpy as np

"""### Masala(1): 2-o'lchamli massiv yaratish

**Masala sharti :** Elementlari 0 dan 9 gacha (9 ning o'zi massiv elementiga kirmaydi), qadami esa 1 ga teng bo'lgan (3, 3) o'lchamli massiv yaratuvchi funksiyani davom ettiring.  

**Yordam :**  `arange`dan foydalanish ishni osonlashtiradi

"""

import numpy as np
def nd_array():
  arr = np.arange(0, 9).reshape(3, 3)
  return arr
print(nd_array())

"""### Yuqoridagi yozgan funksiyangizni tekshirish uchun, quyidagi cellni yuriting.

___
"""

#@title Tekshirish (natijada hech qanday xatolik yuz bermasligi kerak)
"""Funksiyani tekshirish"""
arr = nd_array() # massiv
assert arr.size == 9, f"elementlar sonida xatolik mavjud"  # elementlar soni
assert type(arr) == np.ndarray, f"massiv aniqlanmadi" #numpy array
# elementwise test
test_arr = np.arange(9).reshape(3, 3)
assert arr.shape == (3, 3), f"noto'g'ri qator va ustunlardan foydalanilgan"
assert True in np.in1d(arr, test_arr), f"elementlararo xatolik mavjud"

"""###  Masala(2): Indeks yordamida 2-o'lchamli massivlardan elementlarni  kesib olish
**Masala :** Yuqorida yaratilgan massivning elementlari 6 va 7 ga teng bo'lgan qismini kesib olish funksiyasini davom ettiring.

**Yordam :** 6 va 7 turgan indekslarni aniqlab olib, shu indekslar yordamida kesib oling. **Natija:** array([6, 7]) ko'rinishida bo'lishi kerak.
"""


def sliced_array_2d():
    """Yuqorida yaratilgan massivning elementlari 6 va 7 ga teng bo'lgan
     qismini kesib olish funksiyasi """
    array = nd_array() # yuqoridagi funksiya yordamida array yaratib olish
    return array[2, 0:2]
print(sliced_array_2d())

"""### Yuqoridagi yozgan funksiyangizni tekshirish uchun, quyidagi cellni yuriting."""

#@title Tekshirish (natijada hech qanday xatolik yuz bermasligi kerak)
"""Funksiyani tekshirish"""
sl_arr_2d = sliced_array_2d() # kesib olingan massiv
assert sl_arr_2d.size == 2, f"elementlar sonida xatolik mavjud"  # elementlar soni
assert type(sl_arr_2d) == np.ndarray, f"massiv aniqlanmadi" #numpy array
# elementwise test
test_arr = np.array([6, 7])
assert sl_arr_2d.shape == (2,), f"kesib olingan massiv shaklida xatolik mavjud"
assert True in np.in1d(sl_arr_2d, test_arr), f"elementlararo xatolik mavjud"

"""___

###  Masala(3): Indeks yordamida 3-o'lchamli massivdan elementlarni kesib olish

**Masala :**  3-o'lchamli massivni quyidagi listdan yarating, hamda 12, 13, 15, va 16  elementlarini kesib oluvchi funksiyani davom ettiring.  

                  [[[ 0,  1,  2],
                    [ 3,  4,  5],
                    [ 6,  7,  8]],

                   [[ 9, 10, 11],
                    [12, 13, 14],
                    [15, 16, 17]],

                   [[18, 19, 20],
                    [21, 22, 23],
                    [24, 25, 26]]]

**Yordam :** Avval massivni ikki o'lchamli massivga keltirib, keyin kesib olishni amalga oshiring.


**Natija:**  

             array([[12, 13],
                    [15, 16]])
ko'rinishida bo'lishi kerak.
"""


import numpy as np
def sliced_array_3d():
  arr = np.arange(0, 27).reshape(3, 3, 3)
  new_arr = np.array([arr[1, 1, 0:2], arr[1, 2, 0:2]])
  return new_arr

print(sliced_array_3d())

#@title Tekshirish (natijada hech qanday xatolik yuz bermasligi kerak)
"""Funksiyani tekshirish"""
sl_arr_3d = sliced_array_3d() # kesib olingan massiv
assert sl_arr_3d.size == 4, f"kesib olingan elementlar sonida xatolik" # elementlar soni
assert type(sl_arr_3d) == np.ndarray, f"massiv aniqlanmadi" #numpy array
# elementwise test
test_arr = np.array([[12, 13],
                     [15, 16]])
assert sl_arr_3d.shape == (2,2), f"kesib olingan massiv shaklida xatolik mavjud"
assert True in np.in1d(sl_arr_3d, test_arr), f"elemtlararo xatolik mavjud"

"""___

###  Masala(4): Boolean indeks yordamida 2-o'lchamli massivlardan elementlarni  kesib olish

**Masala :** Bizlarda,  
        
        ['Hasan', 'Husan', 'Javohir', 'Elyor', 'Hasan', 'Javohir', 'Elyor']

**list**dagi kishilar va ularning **ma'lumot**lari
       
      [[5, 6, 1, 1],
       [9, 1, 1, 1],
       [7, 7, 4, 2],
       [1, 5, 1, 9],
       [9, 9, 4, 5],
       [7, 5, 9, 6],
       [5, 3, 7, 4]]
ko'rinishda keltirilgan.


Mana shu ma'lumotlardan **Javohir** va **Elyor** ismlariga tegishli ma'lumotlarni Boolean indekslash yordamida kesib olish funksiyasini davom ettiring.
**Yordam :** Boolean indekslash video darsligiga murojat qiling.
**Natija:** Natija (4, 4) o'lchamli massiv ko'rinishida, hamda dastlabki ikkita qattori quyidagicha

    array([[7, 7, 4, 2],
           [1, 5, 1, 9],
           ...
           ...        ]])
"""

import numpy as np
def boolean_slicing():
  name = np.array(['Hasan', 'Husan', 'Javohir', 'Elyor', 'Hasan', 'Javohir', 'Elyor'])
  data = np.array([[5, 6, 1, 1],
   [9, 1, 1, 1],
   [7, 7, 4, 2],
   [1, 5, 1, 9],
   [9, 9, 4, 5],
   [7, 5, 9, 6],
   [5, 3, 7, 4]])
  user = np.array([data[name == "Javohir"], data[name == "Elyor"]])
  return user

print(boolean_slicing())



import numpy as np
def boolean_slicing():
  name = np.array(['Hasan', 'Husan', 'Javohir', 'Elyor', 'Hasan', 'Javohir', 'Elyor'])
  data = np.array([[5, 6, 1, 1],
   [9, 1, 1, 1],
   [7, 7, 4, 2],
   [1, 5, 1, 9],
   [9, 9, 4, 5],
   [7, 5, 9, 6],
   [5, 3, 7, 4]])
  mask = (name == "Javohir") | (name == "Elyor")
  user = np.array(data[mask])
  return user

print(boolean_slicing())

"""### Yuqoridagi yozgan funksiyangizni tekshirish uchun, quyidagi cellni yuriting."""

#@title Tekshirish (natijada hech qanday xatolik yuz bermasligi kerak)
"""Funksiyani tekshirish"""
bool_idx = boolean_slicing() # kesib olingan massiv
assert bool_idx.size == 16, f"kesib olingan elementlar sonida xatolik mavjud"  # elementlar soni
assert type(bool_idx) == np.ndarray, f"massiv aniqlanmadi" #numpy array
# elementwise test
test_arr = np.array([[7, 7, 4, 2],
                     [1, 5, 1, 9],
                     [7, 5, 9, 6],
                     [5, 3, 7, 4]])
assert bool_idx.shape == (4,4), f"kesib olingan massiv shaklida xatolik mavjud"
assert True in np.in1d(bool_idx, test_arr), f"elemetlararo xatolik mavjud"