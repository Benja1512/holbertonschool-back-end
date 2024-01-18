import urllib.request
import json
import sys
import csv

def get_employee_todo_progress(employee_id):
    # URL del endpoint de la API
    api_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'

    try:
        # Obtener la lista de tareas pendientes del empleado
        with urllib.request.urlopen(api_url) as response:
            todos = json.loads(response.read().decode('utf-8'))

        # Obtener el nombre del empleado
        employee_name = todos[0].get('username') or todos[0].get('name') or 'Desconocido'

        # Contar las tareas completadas y el número total de tareas
        completed_tasks = [task for task in todos if task['completed']]
        number_of_done_tasks = len(completed_tasks)
        total_number_of_tasks = len(todos)

        # Mostrar información del progreso
        print(f"Empleado {employee_name} ha completado tareas ({number_of_done_tasks}/{total_number_of_tasks}):")
        
        # Mostrar los títulos de las tareas completadas
        for task in completed_tasks:
            print(f"\t{task['title']}")

        # Llamar a la función para exportar a CSV
        export_to_csv(employee_id, employee_name, completed_tasks)

    except urllib.error.URLError as e:
        print(f"Error al obtener datos: {e}")

def export_to_csv(employee_id, employee_name, completed_tasks):
    # Crear datos CSV
    csv_data = [["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]]
    for task in completed_tasks:
        task_completed_status = "Completada" if task['completed'] else "Pendiente"
        csv_data.append([employee_id, employee_name, task_completed_status, task['title']])

    # Crear el nombre de archivo CSV
    csv_filename = f"{employee_id}.csv"

    # Escribir datos CSV en el archivo
    with open(csv_filename, mode='w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(csv_data)

    print(f"CSV file '{csv_filename}' creado exitosamente con las tareas completadas para el empleado {employee_name}.")

if __name__ == "__main__":
    # Verificar si se proporciona un ID de empleado como argumento de la línea de comandos
    if len(sys.argv) != 2:
        print("Por favor, proporciona el ID del empleado como parámetro.")
        sys.exit(1)

    # Obtener el ID del empleado desde la línea de comandos
    employee_id = int(sys.argv[1])

    # Llamar a la función para obtener y mostrar el progreso de las tareas
    get_employee_todo_progress(employee_id)

