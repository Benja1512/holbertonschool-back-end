#!/usr/bin/python3
import urllib.request
import json
import sys
import csv

def get_all_employees_todo_progress():
    # Lista para almacenar datos de todos los empleados
    all_employees_data = []

    # Obtener información de todos los empleados
    for employee_id in range(1, 11):  # Supongamos que hay 10 empleados
        employee_data = get_employee_todo_progress(employee_id)
        all_employees_data.append(employee_data)

    # Crear el nombre de archivo JSON
    json_filename = "todo_all_employees.json"

    # Escribir datos JSON en el archivo
    with open(json_filename, mode='w', encoding='utf-8') as json_file:
        json.dump(all_employees_data, json_file, ensure_ascii=False, indent=2)

    print(f"JSON file '{json_filename}' creado exitosamente con las tareas completadas de todos los empleados.")

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
        completed_tasks = [{"username": employee_name, "task": task["title"], "completed": task["completed"]} for task in todos]

        return {str(employee_id): completed_tasks}

    except urllib.error.URLError as e:
        print(f"Error al obtener datos del empleado {employee_id}: {e}")
        return {str(employee_id): []}

if __name__ == "__main__":
    # Llamar a la función para obtener y mostrar el progreso de todas las tareas de todos los empleados
    get_all_employees_todo_progress()

