# СОЗДАНИЕ ЛОГОТИПОВ ДЛЯ КАТЕГОРИЙ svoefermerstvo.ru

## ВАРИАНТ 1: вручную

### Понадобятся:

- растровый графический редактор (Photoshop/Gimp)
- web-версия [kandinsky 2.2](https://editor.fusionbrain.ai) (бесплатный), [DALL-E](https://labs.openai.com/) (несколько запросов бесплатные, далее 15$ за ~100 запросов по 4 изображения или по 1 редакторскому запросу) или другая графическая нейросеть

1. Предварительно в графическом редакторе создать фон.

### Требовиния к фону:

- квадратный
- белый
- в правом нижнем углу располагается круг
- круг заполнен градиентом от светлого к цвету средней интенсивности или наоборот

[Пример фона](/images/background.png)

2. В веб-интерфейсе нейросети ввести запрос (prompt).
   [Примеры промптов](https://docs.google.com/spreadsheets/d/1e48AkdP-xRRA95jlVZGGv3u4eq4Ktw1Hi-_kEAu-lo0/edit?usp=sharing), через которые были сгенерированы основные категории.

### Примечниие:

[kandinsky 2.2](https://editor.fusionbrain.ai) генерирует более яркие и "глянцевые" изображения, а [DALL-E](https://labs.openai.com/) точнее изображает конкретные реальные предметы (строительные инструменты инструменты, запчасти, садовые инструменты, канцелярские пренадлежности)

3. Выбрать более подходящее изображение и откорректировать его в графическом редакторе (убрать фон, обрезать и тд)

4. Соединить изображение с фоном логотипа.

### Требования к изображению:

- одна часть изображения должна вписываться в круг, другая - выходить из границ круга
  [Пример изображения](/images/image.png)
  В редакторе можно достичь так:
  а) наложить слой с изображением на слой с кругом
  б) поверх выделить круг круговым выделением
  в) инвертировать выделение [Пример фона](/images/remove_outside.png)
  г) стереть лишнее

## ВАРИАНТ 2: используя API kandinsky 2.2

Использовать готовую настройку API в ноутбуке Python
[Здесь](https://colab.research.google.com/github/pytorch/xla/blob/master/contrib/colab/style_transfer_inference.ipynb) или [здесь](https://huggingface.co/kandinsky-community/kandinsky-2-2-prior)
