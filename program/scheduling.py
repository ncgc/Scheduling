from enum import Enum
from pyfields import field, make_init

class Scheduling(object):
  choice: int = field(check_type=True, doc='Escolha do processo de escalonamento')
  burst: str = field(check_type=True, doc='Método de burst(automático ou manual')
  qnt: int = field(check_type=True, doc='Quantidade de processos a serem escalonados')
  __init__ = make_init(choice, qnt, burst)

  def getChoice(self):
    return self._choice

  def getBurst(self):
    return self._burst

  def getQnt(self):
    return self.qnt

  @choice.validator
  def validateChoice(self, choice):
    if not 0 <= choice < 6: raise ValueError('should be between 0 or 5')
    self._choice = choice

  @burst.validator
  def validateBurst(self, burst):
    burst = burst.capitalize()
    if burst not in ['A','M']: raise ValueError('should be M or A')
    self._burst = burst

class Choices(Enum):
  FCFS = 1
  SJF = 2
  SRTF = 3
  RR = 4
  MLEVEL = 5
