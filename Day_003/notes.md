Gün 3: Control flow and Logical Operations
## Koşul İfadelerinin Kısaltılması
- Standart kullanım:
  ```python
  if age >= 45 and age <= 55:
- Daha basit kulanımı
if 45 <= age <= 55:if 45 <= age <= 55:

## Karakter Kaçışları (Escaping Characters)
Print ederken veya string oluştururken, çift tırnak (") veya tek tırnak (') kullanmak gerektiğinde, bu karakterlerden kaçınmak için \ (ters slash) kullanılır.
Örnek:
input('You\'re at a cross road. Where do you want to go? \n Type "left" or "right" ')