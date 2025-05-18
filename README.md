# Controle-Braco

Este projeto permite controlar um conjunto de servos que compõem a mão de um braço robótico utilizando um Raspberry Pi (preferencialmente modelo 5) e um conjunto de cabos.

## Funcionalidades

* Suporte a 6 servos (4 dedos da mão, polegar e pulso)
* Execução como serviço systemd (`hand-control.service`)
* Modo hotspot para criação de rede local com acesso à interface web

## Requisitos

* Raspberry Pi (testado com modelo 5)
* Servos da mão (6 servos)
* Algum Linux com suporte a systemd

## Instalação

1. Faça o boot do Raspberry Pi.
2. Clone este repositório:

   ```bash
   git clone https://github.com/Grupo-de-Pesquisa-em-Algoritmos/controle-braco.git
   ```
3. Acesse a pasta do projeto e instale:

   ```bash
   cd controle-braco
   make install
   ```

## Configuração de pinos

Conecte os servos aos pinos GPIO do Raspberry Pi conforme a tabela abaixo:

| Função         | GPIO PIN |
| -------------- | -------: |
| Dedo indicador |       17 |
| Dedo médio     |       27 |
| Dedo anelar    |       22 |
| Dedo mínimo    |        5 |
| Polegar        |        6 |
| Pulso          |       19 |

## Execução

Para iniciar o serviço:

```bash
systemctl --user start hand-control.service
```

A interface web ficará disponível em:

```
http://127.0.0.1:5000
```

## Modo Hotspot

Caso queira disponibilizar o serviço como ponto de acesso local:

1. Execute o script de hotspot:

   ```bash
   ./start_hotspot.sh
   ```
2. Uma rede Wi-Fi chamada `servo` será criada, com senha `12345678`.
3. Conecte-se à rede e acesse:

   ```
   http://10.42.0.1:5000
   ```
