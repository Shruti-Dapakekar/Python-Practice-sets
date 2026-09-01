# wap to fill in a letter template given bello with name and date
letter = '''
            Dear <|Name|>,
            You are selected!
            <|Date|>
            '''
print(letter.replace("<|Name|>", "Shruti").replace("<|Date|>","1/9/2026"))
