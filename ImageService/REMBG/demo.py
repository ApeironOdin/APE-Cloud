from rembg import remove, new_session

with open('input.jpg', 'rb') as i:
    with open('output.png', 'wb') as o:
        input = i.read()
        output = remove(input, session=new_session('u2netp'))
        o.write(output)
