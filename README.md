# maskcode
Hide data inside images
<br>

## Installation  
   ```
   pip install git+https://github.com/im-strange/maskcode.git
   ```
<br>

## Usage

### Embedd data
   ```py
   from maskcode import MaskCode
  
   image = "my_image.jpg"
   data = MaskCode(image)

   data.embedd("Hello world!")
   ```
&nbsp;  

### Extract Data
> Note that it will return binary object
   ```py
   from maskcode import MaskCode
  
   image = "my_image.jpg"
   data = MaskCode(image)

   extracted_data = data.extract()
   print(extracted_data)

   ```
&nbsp;  

### Reset embedded data
   ```py
   from maskcode import MaskCode
  
   image = "my_image.jpg"
   data = MaskCode(image)

   data.reset()
   print(data.extract())
   ```
&nbsp;  

