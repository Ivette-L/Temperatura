from typing import List

class AnalizadorTemperaturas:
    def __init__(self,dias:int=7):
        self.dias=dias
        self.temperaturas:List[float]=[]

    def solicitar_temperatura(self):
        print("ingreso T° diarias\n")
        for dia in range(1,self.dias+1):
            while True:
                try:
                    entrada=input(f"Ingrese T° del dia{dia}:°")
                    temperatura=float(entrada)
                    if temperatura <-100:
                        raise ValueError("La T° no es valida")
                    if temperatura <0:
                        print(f"no salga sin su cafecito, extremo frio")
                    if temperatura >40:
                        print(f"mantengase en la sombra, extremo calor")
                    self.temperaturas.append(temperatura)
                    break
                except ValueError as e:
                    print(f"entrada no valida; {e}")

    def analizar_temperatura(self):
        print("Resumen de Temperaturas\n")
        total=sum(self.temperaturas)
        promedio=total/self.dias
        máxima=max(self.temperaturas)
        minima=min(self.temperaturas)
        dia_max=self.temperaturas.index(máxima)+1
        dia_min=self.temperaturas.index(minima)+1

        print(f"promedio:{promedio:,.1f}")
        print(F"máxima:{máxima:,.1f})(dia{dia_max})")
        print(f"minima:{minima:,.1f})(dia{dia_min})")

def main():
    analizador=AnalizadorTemperaturas()
    analizador.solicitar_temperatura()
    analizador.analizar_temperatura()
    
if __name__ == "__main__":
    main()
    