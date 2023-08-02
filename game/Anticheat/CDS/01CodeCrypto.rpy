python early:
    def parse_encrypted(lexer):
        subblock_lexer = lexer.subblock_lexer()
        codes = []
        while subblock_lexer.advance():
            code = subblock_lexer.rest()
            codes.append(code)
        return codes

    def execute_encrypted(parsed_object):
        print(parsed_object)

    renpy.register_statement(
        "encrypted",
        block = True,
        parse = parse_encrypted,
        execute = execute_encrypted
    )