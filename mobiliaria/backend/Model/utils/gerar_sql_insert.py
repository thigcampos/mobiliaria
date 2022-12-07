def gerar_sql_insert_fornecedor(
    nome_fornecedor,
    cnpj_fornecedor,
    email,
    telefone,
    cep,
    logradouro,
    numero,
    complemento,
):
    return """INSERT INTO fornecedores (
                nome_fornecedor,
                cnpj_fornecedor,
                email,
                telefone,
                cep,
                logradouro,
                numero,
                complemento) VALUES ('{}', '{}', '{}','{}','{}','{}','{}','{}')""".format(
        nome_fornecedor,
        cnpj_fornecedor,
        email,
        telefone,
        cep,
        logradouro,
        numero,
        complemento,
    )


def gerar_sql_insert_produto(
    nome_produto,
    categoria,
    preco,
    descricao,
    estoque,
    ficha_tecnica,
    id_fornecedor,
):
    return """INSERT INTO produtos (
        nome_produto,
        categoria,
        preco,
        descricao,
        estoque,
        ficha_tecnica,
        id_fornecedor) VALUES ('{}', '{}', '{}','{}','{}','{}','{}')""".format(
        nome_produto,
        categoria,
        preco,
        descricao,
        estoque,
        ficha_tecnica,
        id_fornecedor,
    )


def gerar_sql_insert_pedido(
    valor_total,
    data_pedido,
    qtde_produto,
    id_produto,
    id_cliente,
):
    return """INSERT INTO pedidos (
        valor_total, 
        data_pedido, 
        qtde_produto,
        id_produto, 
        id_cliente) VALUES ('{}', '{}', '{}','{}','{}')""".format(
        valor_total,
        data_pedido,
        qtde_produto,
        id_produto,
        id_cliente,
    )


def gerar_sql_insert_cliente(
    nome_cliente,
    cpf,
    data_nascimento,
    telefone,
    email,
    cep,
    logradouro,
    numero,
    complemento,
):
    return """INSERT INTO clientes (nome_cliente, cpf, data_nascimento, telefone, email,  cep, logradouro, numero, complemento) VALUES ('{}', '{}', '{}','{}','{}','{}','{}','{}','{}')""".format(
        nome_cliente,
        cpf,
        data_nascimento,
        telefone,
        email,
        cep,
        logradouro,
        numero,
        complemento,
    )
