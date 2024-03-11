"""
Funcoes auxiliares de N-corpos
"""
import numpy as np

def F_ncorpos (m:list, r):
  F_vec = np.zeros((len(m),3))
  for a in range(len(m)):
    for b in range(len(m)):
      if a == b: continue
      rab = r[b] - r[a]
      F_vec[a] += m[a]*m[b]*(rab)/np.linalg.norm(rab)**3
      # F_vec[b] += - F_vec[a]
  return F_vec

def valores_iniciais_lemniscata ():
  r0 = np.array([
    [-0.97000436, 0.24308753, 0.0],
    [ 0.0,        0.0,        0.0],
    [ 0.97000436,-0.24308753, 0.0],
  ])
  v0 = np.array([
    [ 0.4662036850, 0.4323657300, 0.0],
    [-0.93240737,  -0.86473146,   0.0],
    [ 0.4662036850, 0.4323657300, 0.0],
  ])
  m = [1.0,1.0,1.0]
  return m, r0, v0

def energia_total (m, r, v, G:float=1):
  # Energia cinetica
  T = 1/2 * sum(m[i] * np.linalg.norm(v[i])**2 for i in range(len(m)))
  
  # Energia potencial
  U = .0
  for a in range(1,len(m)):
    for b in range(a):
      U += G * m[a] * m[b] / np.linalg.norm(r[a] - r[b])
  
  return T + U