def division_techo(dividendo, divisor):

    return (dividendo + (divisor / 2)) / divisor

class Heap(object):

    def __init__(self, funcion_comparacion, Array = []):

        self.datos = Array
        self.cantidad_elementos = len(self.datos)        
        self.comparar_prioridad = funcion_comparacion
        self._heapify()       

    def esta_vacio(self):

        return not self.cantidad_elementos

    def cantidad(self):

        return self.cantidad_elementos

    def ver_max(self):

        maximo = 0
        try:
            return self.datos[maximo]

        except IndexError:
            return None

    def encolar(self, elemento):

        self.datos.append(elemento)
        self.cantidad_elementos += 1
        self._upheap(self.cantidad_elementos - 1)
        
        return True

    def _swap_y_continuar(self, posicion_hijo, posicion_padre, upheap):

        
        
        aux = self.datos[posicion_hijo]
        self.datos[posicion_hijo] = self.datos[posicion_padre]
        self.datos[posicion_padre] = aux
        if upheap:

            self._upheap(posicion_padre)

        else:

            self._downheap(posicion_padre)

    def _upheap(self, posicion_actual):

        if posicion_actual == 0:

            return

        padre = division_techo(posicion_actual-2,2)
        if self.comparar_prioridad(self.datos[posicion_actual],self.datos[padre]) > 0:
            self._swap_y_continuar(posicion_actual, padre, True)


    def desencolar(self):

        try:

            prioritario = self.datos.pop(0)
            self.cantidad_elementos -= 1
            if len(self.datos):
                
                ultimo = self.datos.pop(self.cantidad_elementos - 1)    
                self.datos.insert(0, ultimo)
                self._downheap(0)
            
            return prioritario

        except IndexError:

            return None
        
    def _downheap(self, posicion_actual):
    
        pos_h_izquierdo = (2*posicion_actual) + 1
        pos_h_derecho = (2*posicion_actual) + 2
        comparar = self.comparar_prioridad
        datos = self.datos
        if pos_h_izquierdo >= self.cantidad_elementos: #Arbol izquierdista

            return

        elif pos_h_derecho >= self.cantidad_elementos: #solo un hijo izquierdo

            if comparar(datos[posicion_actual], datos[pos_h_izquierdo]) == -1:

                self._swap_y_continuar(posicion_actual, pos_h_izquierdo, False)

        else: #Tiene dos hijos
    
            if comparar(datos[posicion_actual], datos[pos_h_derecho]) > 0:

                if comparar(datos[posicion_actual], datos[pos_h_izquierdo]) > 0:
                    
                    return #los hijos son menores que el

            pos_prioritaria = pos_h_izquierdo
            if comparar(datos[pos_h_izquierdo], datos[pos_h_derecho]) < 0:
                            
                pos_prioritaria = pos_h_derecho #el hijo derecho tenia mas prioridad

            self._swap_y_continuar(posicion_actual, pos_prioritaria, False)


    def _heapify(self):

        inicio = self.cantidad_elementos - 1
        for pos in xrange(inicio, -1, -1):

            self._downheap(pos) 

def heap_sort(arreglo, funcion_comparacion):

    copia_arreglo = list(arreglo)
    ultimo = len(arreglo) - 1
    heap_arr = Heap(funcion_comparacion, copia_arreglo)
    primero = 0
    while ultimo >= 0:
	
        prioritario = heap_arr.datos[primero]
        heap_arr.datos[primero] = heap_arr.datos[ultimo]
        heap_arr.datos[ultimo] = prioritario
        ultimo -= 1
        heap_arr.cantidad_elementos -= 1
        if ultimo < 0: break
        heap_arr._downheap(primero)

    return heap_arr.datos
