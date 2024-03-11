"""
Tem um Jupyter Notebook falando sobre o Runge-Kutta. Esse daqui eh so
para usar em exemplos.
"""

def runge_kutta_44 (y0, f, t0, tf, n):
  # Lista para salvar os valores aproximados da solucao
  y_ks = [y0]

  # Calcula o tamanho do passo
  h = (tf - t0)/n

  # Determina as variaveis com os valores iniciais
  tk = t0
  yk = y0

  # Agora aplica
  for _ in range(n):
    
    # Para cada passo, precisa calcular os kappa
    kappa_1 = f(tk, yk)
    kappa_2 = f(tk + h/2, yk + h*kappa_1/2)
    kappa_3 = f(tk + h/2, yk + h*kappa_2/2)
    kappa_4 = f(tk + h, yk + h*kappa_3)

    # Aplicando o metodo, ja substituindo y_{k} = y_{k+1}
    yk = yk + h*(kappa_1 + 2*kappa_2 + 2*kappa_3 + kappa_4) / 6

    # Salva a aproximacao
    y_ks.append(yk)

    # O proximo instante calculado sera o anterior + h
    tk = tk + h

  return y_ks