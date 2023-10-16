# TT_VKO_Medprom

Проект предназначен для обработки изображений в формате TIFF с использованием библиотеки OpenCV. Для решения задачи по удалению шума из изображений была разработана функция `remove_noise`.

## Основные этапы проекта:

1. **Библиотека OpenCV:**
   - Для обработки изображений была использована библиотека OpenCV, предоставляющая множество инструментов для работы с изображениями.

2. **Функция `remove_noise`:**
   - В рамках проекта была разработана функция `remove_noise`, предназначенная для удаления шума с изображения.

3. **Медианный фильтр (`medianBlur`):**
   - Для удаления шума был применен медианный фильтр с заданным размером ядра. 
   - Размер ядра был выбран равным 3, так как он оказался оптимальным для достижения баланса между сохранением качества изображения и удалением шума.

4. **Сравнение с `GaussianBlur`:**
   - В ходе работы над проектом была проведена попытка использовать функцию `GaussianBlur` с параметрами: размер ядра `(5, 5)` и стандартное отклонение `0`.
   - Этот метод также эффективно устранял шум, однако при сравнении с методом `medianBlur` качество изображения значительно уступало.

Проект позволяет эффективно устранять шум на изображениях, сохраняя при этом их качество.
