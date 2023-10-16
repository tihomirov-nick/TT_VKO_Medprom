# TT_VKO_Medprom

Для выполнения использовал библиотеку opencv, функцию medianBlur. Задача заключалась в удалении шума из изображения, представленного в формате TIFF. Для этого я написал функцию remove_noise, которая принимает изображение в качестве входного параметра и применяет медианный фильтр с заданным размером ядра. Размер ядра выбрал равным 3, так как нашел его оптимальным между потерей качества и удалением шума. Так же пробовал использовать функцию GaussianBlur с заданными параметрами - размер ядра (5, 5), стандартное отклонение 0, шум был удален так же хорошо, но при сравнении с medianBlur качество сильно отставало.
