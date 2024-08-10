import click
import json_manager
from datetime import datetime
import uuid

@click.group()
def cli():
    pass

@cli.command()
def list_task():
    data = json_manager.read_json()
    print(data)

@cli.command()
@click.argument('description', required= True)
# @click.option('--status', type=click.Choice(['todo', 'in-progress', 'done'], case_sensitive=False))
@click.pass_context
def add(ctx,description):
    if not description:
        ctx.fail('The description and status are requeired')
    else:

        data = json_manager.read_json()
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        id = str(uuid.uuid4())
        new_task = {
            'id':id,
            'description': description,
            'status': "todo",
            'createdAt': now,
            'updatedAt': now
        }
        
        data.append(new_task)
        json_manager.write_json(data)
        print(f'Task {description} created successfullt with id {id}')

    
@cli.command()
@click.argument("id")
def delete(id):
    # print(id)
    data=json_manager.read_json()
    task = next((x for x in data if x['id'] == id), None)
    for x in data: 
        if x['id'] == id:
            data.remove(x)
            json_manager.write_json(data)
            print(f'Task with id {id} deleted successfully.')
        else:
            print(f'Task with id {id} no found.')

@cli.command()
@click.argument('id')
@click.argument('description', required= True)
def update(id, description):
    data = json_manager.read_json()
    found = False

    for x in data:
        if(x['id'] == id):
            x['description'] = description
            x['updatedAt'] =  datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            found= True
            break
            
    if found:
            json_manager.write_json(data)
            print(f'Task with id {id} updated successfully')
    else:
            print(f'Task with id {id} no found.')

@cli.command()
@click.argument('id')
# @click.option('--status', type=click.Choice(['todo', 'in-progress', 'done'], case_sensitive=False))
def mark_in_progress(id):
    data = json_manager.read_json()
    found = False

    for x in data:
        if(x['id'] == id):
            x['status'] = "in-progress"
            x['updatedAt'] =  datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            found= True
            break
            
    if found:
            json_manager.write_json(data)
            print(f'Task with id {id} updated progress successfully')
    else:
            print(f'Task with id {id} no found.')

@cli.command()
@click.argument('id')
# @click.option('--status', type=click.Choice(['todo', 'in-progress', 'done'], case_sensitive=False))
def mark_done(id):
    data = json_manager.read_json()
    found = False

    for x in data:
        if(x['id'] == id):
            x['status'] = "done"
            x['updatedAt'] =  datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            found= True
            break
            
    if found:
            json_manager.write_json(data)
            print(f'Task with id {id} updated progress successfully')
    else:
            print(f'Task with id {id} no found.')
     
@cli.command()
@click.argument("status", required= False)
def list(status):
    if not status:
        data = json_manager.read_json()
        print(data)
    else:  
     data = json_manager.read_json()
     result = [x for x in data if x["status"] == status]
     if not result:
        print(f"There are no tasks in {status}")
     else:
        print(result)


if __name__ == '__main__':
    cli()