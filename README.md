# 🖱️ Computer Vision Automation Bot

Um script em Python desenvolvido para automação de tarefas de interface gráfica (GUI) com base em **reconhecimento de imagem e visão computacional**. 

O projeto identifica elementos visuais específicos na tela em tempo real, mapeia suas coordenadas e executa ações programadas (como sequências de cliques, movimentação de cursor e pressionamento de teclas atalho).

---

## 🎯 Funcionalidades

* **Detecção Visual Dinâmica:** Localização de elementos na tela com ajuste ajustável de margem de precisão (`confidence`).
* **Tratamento de Exceções:** Sistema configurado com *Fail-Safe* para interrupção de emergência instantânea.
* **Ações em Cascata e Lógica Condicional:** Encadeamento de funções que permitem executar ações sequenciais dependendo do elemento gráfico identificado.
* **Simulação de Comportamento Humano:** Algoritmo que utiliza a biblioteca `numpy` para gerar cliques aleatórios em regiões da tela, reduzindo a previsibilidade dos padrões de movimento.
* **Suporte a Hotkeys:** Execução de atalhos de teclado integrados à interação com a tela.

---

## 🛠️ Tecnologias Utilizadas

* **[Python 3.x](https://www.python.org/):** Linguagem principal do projeto.
* **[PyAutoGUI](https://pyautogui.readthedocs.io/):** Controle de mouse, teclado e captura/localização na tela.
* **[OpenCV (opencv-python)](https://opencv.org/):** Suporte ao algoritmo de correspondência de imagens (*template matching*).
* **[NumPy](https://numpy.org/):** Manipulação de arrays e geração de coordenadas aleatórias para cliques.

---

## 🚀 Como Executar o Projeto

### Pró-requisitos

Certifique-se de ter o Python instalado em sua máquina.
