import math

def calculate_metrics(matrix):
    # Extrair valores da matriz de confusão
    tp, fp, fn, tn = map(int, matrix)

    # Calcular acurácia
    accuracy = (tp + tn) / (tp + fp + fn + tn)
    
    # Calcular precisão
    if tp + fp != 0:
        precision = tp / (tp + fp)
    else:
        precision = 0
    
    return accuracy, precision

def best_performance(matrices):
    best_index = 0
    best_accuracy = 0
    best_precision = 0
    
    # Loop através de cada matriz para calcular as métricas
    for index, matrix in enumerate(matrices):
        accuracy, precision = calculate_metrics(matrix)
        
        # Verificar se as métricas são melhores do que as atuais
        if accuracy + precision > best_accuracy + best_precision:
            best_index = index
            best_accuracy = accuracy
            best_precision = precision
            
    return best_index, best_accuracy, best_precision

def format_number(number):
    formatted_number = f"{number:.2f}"  # Formatar o número com duas casas decimais
    
    # Verificar se o último dígito após o ponto decimal é zero
    if formatted_number[-1] == '0':
        return f"{number:.1f}"  # Se for zero, formatar com uma casa decimal
    else:
        return formatted_number  # Caso contrário, manter a formatação com duas casas decimais


# Entrada do usuário
n = int(input())
matrices = []

for _ in range(n):
    matrix = input().split(',')
    matrices.append(matrix)

# Encontrar a melhor matriz de desempenho
best_index, best_accuracy, best_precision = best_performance(matrices)


# Exibir os resultados
print(f"Índice: {best_index+1}")
print(f"Acurácia: {format_number(best_accuracy)}")  
print(f"Precisão: {format_number(best_precision)}")