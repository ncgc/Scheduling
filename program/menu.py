from .scheduling import Scheduling

class Menu:

  def __init__(self):
    pass

  @staticmethod
  def defineProcess(*argv):
    print("Escolha uma opção de escalonamento")
    print("1 - First-Come First-Served (FCFS)")
    print("2 - Shortest Job First(SJF)")
    print("3 - Shortest-Remaining-Time-First (SRTF)")
    print("4 - Round Robin (RR)")
    print("5 - Multinível")
    print("0 - Sair")

    choice = int(input('Opção: '))

    qnt = int(input("Qual a quantidade de processos?"))

    burst = input("Burst manual ou aleatório(M/A)?")

    try:
      Scheduling(choice, qnt, burst)
    except ValueError as e:
      print(e)