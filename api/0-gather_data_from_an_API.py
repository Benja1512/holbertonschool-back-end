import urllib.request
import json
import sys

def get_employee_todo_progress(employee_id):
    # URL del endpoint de la API
    api_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'

    try:
        #  1. Obtener la lista de tareas pendientes del empleado
        with urllib.request.urlopen(api_url) as response:
            todos = json.loads(response.read().decode('utf-8'))

        #  2. Obtener el nombre del empleado
        employee_name = todos[0].get('username') or todos[0].get('name') or 'Desconocido'

        # 3. Contar las tareas completadas y el número total de tareas
        completed_tasks = [task for task in todos if task['completed']]
        number_of_done_tasks = len(completed_tasks)
        total_number_of_tasks = len(todos)

        # 4. Mostrar información del progreso
        print(f"Empleado {employee_name} ha completado tareas ({number_of_done_tasks}/{total_number_of_tasks}):")
        
        # 5. Mostrar los títulos de las tareas completadas
        for task in completed_tasks:
            print(f"\t{task['title']}")

        # 6. Levantar el error si con except
    except urllib.error.URLError as e:
        print(f"Error al obtener datos: {e}")

if __name__ == "__main__":
    # 7. Verificar si se proporciona un ID de empleado como argumento de la línea de comandos
    if len(sys.argv) != 2:
        print("Por favor, proporciona el ID del empleado como parámetro.")
        sys.exit(1)

    # 8. Obtener el ID del empleado desde la línea de comandos
    employee_id = int(sys.argv[1])

    # 9. Llamar a la función para obtener y mostrar el progreso de las tareas
    get_employee_todo_progress(employee_id)

