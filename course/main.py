import heapq

def scheduleCourse(courses):
    tempo_atual = 0
    num_cursos = 0
    max_heap = []

    cursos_ordenados = sorted(courses, key = lambda x: x[1]) # Ordenar por deadline

    for curso in cursos_ordenados:
        if tempo_atual + curso[0] <= curso[1]: # Se não ultrapassar o tempo, adiciona na lista de cursos
            tempo_atual = tempo_atual + curso[0]
            heapq.heappush(max_heap, -curso[0])
            num_cursos +=1
        else: # Se ultrapassar, deve trocar o curso que tiver maior duração pelo atual
            if max_heap:
                maior_dur = - max_heap[0]
                if curso[0] < maior_dur:
                    tempo_atual += curso[0] + heapq.heappop(max_heap)
                    heapq.heappush(max_heap, -curso[0])
        
    print(num_cursos)
    return num_cursos

courses = [[2,5],[2,19],[1,8],[1,3]]
scheduleCourse(courses)