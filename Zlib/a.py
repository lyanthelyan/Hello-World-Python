import zlib
print('Irá começar agora')
def compress_nbt_file(file_path, target_size):
    # Lê o arquivo .nbt
    with open(file_path, 'rb') as file:
        data = file.read()

    # Comprime os dados usando zlib
    compressed_data = zlib.compress(data)

    # Redimensiona os dados comprimidos para o tamanho alvo
    while len(compressed_data) > target_size:
        # A cada iteração, o nível de compressão é reduzido para alcançar o tamanho alvo
        compressed_data = zlib.compress(data, level=zlib.Z_BEST_COMPRESSION)

    # Grava os dados comprimidos em um novo arquivo
    compressed_file_path = file_path + '.compressed'
    with open(compressed_file_path, 'wb') as compressed_file:
        compressed_file.write(compressed_data)

    print(f"Arquivo comprimido salvo em: {compressed_file_path}")


# Exemplo de uso
nbt_file_path = 'C:\\Users\\T-GAMER\\Documents\\Workspace\\Hello World Python\\Zlib\\castelo_janpones(1).nbt'
target_size = 256 * 1024  # 256 KB

compress_nbt_file(nbt_file_path, target_size)
print('Fim')