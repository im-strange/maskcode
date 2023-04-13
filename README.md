# maskcode
Hide data inside images

## Installation

  ```
  pip install git+https://github.com/im-strange/maskcode.git
  ```
<br>

## Usage

  ```py
  from maskcode import MaskCode
  
  image = "my_image.jpg"
  data = MaskCode(image)

  ```
<br>

### Embedd data

  ```py
  data.embedd("Hello world!")
  ```

### Extract Data
  > Note that it will return binary object

  ```py
  extracted_data = data.extract()
  print(extracted_data)
  ```

  **Output:**

  ```
  b'Hello world!'
  ```

### Reset embedded data

  ```py
  data.reset()
  print(data.extract())
  ```

  **Output:**

  ```
  b''
  ```

